import etl.extract as extract
import re


class Transform:
    def clean_caption(self, caption):

        caption = re.sub(r'\bزیور آلات\b', 'زیورآلات', caption)
        caption = re.sub(r'\bنوزاد\b', 'نوزادی', caption)
        caption = re.sub(r'\bربدو شامبر\b', 'ربدوشامبر', caption)
        caption_arr = re.split('[_ \n,،]+', caption)
        caption_arr = [word[:-2] if word.endswith("ها") else word[:-3] if word.endswith("های") else word for word in
                       caption_arr]
        caption_arr = [word for word in caption_arr if word not in extract.stop_words['word'].to_list()]
        return ' '.join(caption_arr)

    def get_category_father(self, category: int, category_df):
        valid_categories = list(range(1, 7)) + [632]
        if category is not None:
            # reach a category.py in valid categories.
            if category in valid_categories:
                return category
            # we need to reach to the father of each category.py, until we reach any of the valid categories.
            while category > 6:
                father_df = category_df[category_df.Id == category].iloc[0]
                father = father_df.CategoryId
                category = father
            # reach a category.py in valid categories.
            if category in valid_categories:
                return category

    def get_other_categories(self, parent_id, category_df):

        if parent_id == -2:
            category_ids = list(category_df[category_df['Title'].str.contains('ورزشی')].Id)
            return category_ids

        else:
            category_title = category_df[category_df.Id == parent_id].iloc[0].Title
            similar_df = category_df[category_df.Title == category_title]
            return list(similar_df.Id)

    def fetch_similar_categories(self, phrase, category_df):
        similar_categories = category_df[
            category_df['Grouping'].str.contains(r'\b' + phrase + r'\b', regex=True, na=False)]
        lst_similar_categories = list(similar_categories['Id'])
        return lst_similar_categories
