import concurrent.futures
from kukala_category import startup as category_setup
from kukala_material import startup as material_setup
from kukala_color import startup as color_setup
from kukala_attribute import startup as attribute_setup
from kukala_brand import startup as brand_setup
import etl.extract as extract
from etl.transform import Transform

color_df = extract.color
brand_df = extract.brand
material_df = extract.material
attribute_df = extract.attribute
category_df = extract.category

color_dict = color_df.set_index('Id')['color'].to_dict()
brand_dict = brand_df.set_index('Id')[['Title', 'TitleEn']].to_dict('index')
material_dict = material_df.set_index('Id')['Title'].to_dict()
attribute_dict = attribute_df.set_index('Id')['Title'].to_dict()
category_dict = category_df.set_index('Id')['Grouping'].to_dict()

transform = Transform()


# Create a ThreadPoolExecutor with a maximum of 4 threads
def tags_extractor(phrase):
    data = [{'_id': 1, 'cleaned_caption': phrase}]
    data[0]["category_id"] = category_setup.run(data)[0]["CategoryId"]

    functions = [material_setup.run, color_setup.run, attribute_setup.run, brand_setup.run]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Run each function concurrently
        for function in functions:
            executor.submit(function, data)

    for item in data:
        if 'ColorId' in item and item['ColorId']:
            colors = item['ColorId']
            for color in colors:
                phrase = phrase.replace(color_dict.get(color, ''), '')
        else:
            colors = []

        if 'BrandId' in item and item['BrandId'] != -1:
            brands = [item['BrandId']]
            brand_info = brand_dict.get(brands[0], {})
            phrase = phrase.replace(brand_info.get('Title', ''), '')
            phrase = phrase.lower().replace(brand_info.get('TitleEn', ''), '')
        else:
            brands = []

        if 'MaterialId' in item and item['MaterialId']:
            materials = item['MaterialId']
            for i in materials:
                phrase = phrase.replace(material_dict.get(i, ''), '')
        else:
            materials = []

        if 'Attributes' in item and item['Attributes']:
            attributes = item['Attributes']
            for i in attributes:
                phrase = phrase.replace(attribute_dict.get(i, ''), '')
        else:
            attributes = []

        if 'CategoryId' in item:
            if item['CategoryId'] and item['CategoryId'] != -1:
                categories = item['CategoryId']
                category_title = category_dict.get(item['CategoryId'], '')
                word_lst = transform.clean_caption(category_title).split()
                if word_lst:
                    for _word in word_lst:
                        phrase = phrase.replace(_word, '')
                if transform.get_category_father(categories, category_df) == 6:
                    categories = transform.get_other_categories(categories, category_df)
                else:
                    categories = [categories]
            elif item['CategoryId'] == -1 and phrase and 'ساعت' in phrase.split():
                keep_items = ['مردانه', 'زنانه', 'پسرانه', 'دخترانه', 'بچگانه', 'ساعت']
                filtered_list = [item for item in phrase.split() if item in keep_items]
                categories = transform.fetch_similar_categories(' '.join(filtered_list), category_df)
                if categories:
                    for watch_words in filtered_list:
                        phrase = phrase.replace(watch_words, '')
            elif item['CategoryId'] == -1 and 'search_category_id' in item:
                category_title = category_dict.get(item['search_category_id'], '')
                word_lst = transform.clean_caption(category_title).split()
                if word_lst:
                    for _word in word_lst:
                        phrase = phrase.replace(_word, '')
                categories = transform.fetch_similar_categories(category_title, category_df)
            else:
                categories = transform.fetch_similar_categories(phrase, category_df)
                if categories:
                    phrase = phrase.replace(phrase, '')

            if phrase:
                cleaned_phrase = transform.clean_caption(phrase)
                if cleaned_phrase:
                    phrase = cleaned_phrase.strip().split()
                else:
                    phrase = []
            else:
                phrase = []

            return {'colors': colors, 'brands': brands, 'materials': materials, 'attributes': attributes,
                    'categories': categories, 'query': phrase}
