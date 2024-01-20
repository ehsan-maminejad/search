import concurrent.futures
import requests
import os
import sys
import etl.extract as extract
from etl.transform import Transform

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, root_path)


def call_apis(api_urls, caption):
    params = {"caption": caption}
    response = requests.post(api_urls, params=params)
    if response.status_code == 200:
        return response.json()


api_urls = ["https://ai.kukala.ir/text/color/color_manual_set",
            "https://ai.kukala.ir/text/material/material_manual_set",
            "https://ai.kukala.ir/text/attribute/attribute_manual_set",
            "https://ai.kukala.ir/text/brand/brand_manual_set",
            "https://ai.kukala.ir/text/category/category_manual_set"
            ]

color_df = extract.color
brand_df = extract.brand
material_df = extract.material
attribute_df = extract.attribute
category_df = extract.category

transform = Transform()


# Create a ThreadPoolExecutor with a maximum of 4 threads
def tags_extractor(phrase):
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:

        # Submit API calls to the executor
        futures = [executor.submit(call_apis, url, phrase) for url in api_urls]

        # Wait for all API calls to complete
        data = [future.result()['data'][0] for future in concurrent.futures.as_completed(futures)]

        phrase = transform.clean_caption(phrase)
        for item in data:
            if 'ColorId' in item:
                if item['ColorId']:
                    colors = item['ColorId']
                    for color in colors:
                        phrase = phrase.replace(color_df.loc[color_df['Id'] == color, 'color'].values[0], '')
                else:
                    colors = item['ColorId']
            if 'BrandId' in item:
                if item['BrandId'] != -1:
                    brands = [item['BrandId']]
                    try:
                        phrase = phrase.replace(brand_df.loc[brand_df['Id'] == brands[0], 'Title'].values[0], '')
                    except:
                        phrase = phrase.replace(
                            brand_df.loc[brand_df['Id'] == brands[0], 'TitleEn'].values[0].lower(), '')
                else:
                    brands = []
            if 'MaterialId' in item:
                if item['MaterialId']:
                    materials = item['MaterialId']
                    for i in materials:
                        phrase = phrase.replace(material_df.loc[material_df['Id'] == i, 'Title'].values[0], '')
                else:
                    materials = item['MaterialId']

            if 'Attributes' in item:
                if item['Attributes']:
                    attributes = item['Attributes']
                    for i in attributes:
                        phrase = phrase.replace(attribute_df.loc[attribute_df['Id'] == i, 'Title'].values[0], '')
                else:
                    attributes = item['Attributes']

            if 'CategoryId' in item:
                if item['CategoryId'] and item['CategoryId'] != -1:
                    categories = item['CategoryId']
                    category_title = category_df.loc[category_df['Id'] == item['CategoryId'], 'Grouping'].values[0]
                    word_lst = transform.clean_caption(category_title).split()
                    if word_lst:
                        for _word in word_lst:
                            phrase = phrase.replace(_word, '')
                    if transform.get_category_father(categories, category_df) == 6:
                        categories = transform.get_other_categories(categories, category_df)
                    else:
                        categories = [categories]
                else:
                    categories = transform.fetch_similar_categories(phrase, category_df)
                    if categories:
                        phrase = phrase.replace(phrase, '')

        return {'colors': colors, 'brands': brands, 'materials': materials, 'attributes': attributes,
                'categories': categories, 'query': phrase.strip()}
