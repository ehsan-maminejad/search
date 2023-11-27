import concurrent.futures
import requests
import pandas as pd


def call_apis(api_urls, caption):
    params = {"caption": caption}
    response = requests.post(api_urls, params=params)
    if response.status_code == 200:
        return response.json()


api_urls = ["http://ai.kukala.ir/color/color_manual_set",
            "http://ai.kukala.ir/material/material_manual_set",
            "http://ai.kukala.ir/attribuite/attribute_manual_set",
            "http://ai.kukala.ir/brand/brand_manual_set"
            ]

color_df = pd.read_csv('./components/color_modified.csv')
brand_df = pd.read_csv('./components/Brand.csv')
material_df = pd.read_csv('./components/material_modified.csv')
attribute_df = pd.read_csv('./components/Attribute.csv')


# Create a ThreadPoolExecutor with a maximum of 4 threads
def tags_extractor(caption, remaining):
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # Submit API calls to the executor
        futures = [executor.submit(call_apis, url, caption) for url in api_urls]

        # Wait for all API calls to complete
        data = [future.result()['data'][0] for future in concurrent.futures.as_completed(futures)]

        for item in data:
            if 'ColorId' in item:
                if item['ColorId']:
                    colors = item['ColorId']
                    for color in colors:
                        remaining.remove(color_df.loc[color_df['Id'] == color, 'color'].values[0])
                else:
                    colors = item['ColorId']
            if 'BrandId' in item:
                if item['BrandId'] != -1:
                    brands = [item['BrandId']]
                    try:
                        remaining.remove(brand_df.loc[brand_df['Id'] == brands[0], 'Title'].values[0])
                    except:
                        remaining.remove(brand_df.loc[brand_df['Id'] == brands[0], 'TitleEn'].values[0].lower())
                else:
                    brands = []
            if 'MaterialId' in item:
                if item['MaterialId']:
                    materials = item['MaterialId']
                    for i in materials:
                        remaining.remove(material_df.loc[material_df['Id'] == i, 'Title'].values[0])
                else:
                    materials = item['MaterialId']

            if 'Attributes' in item:
                if item['Attributes']:
                    attributes = item['Attributes']
                    for i in attributes:
                        remaining.remove(attribute_df.loc[attribute_df['Id'] == i, 'Title'].values[0])
                else:
                    attributes = item['Attributes']

        return {'colors': colors, 'brands': brands, 'materials': materials, 'attributes': attributes,
                'query': remaining}
