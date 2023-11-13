import pandas as pd
from get_qcat import get_query_category
from get_fcat import get_category_father


def get_other_categories(caption: str, category_df):
    """
    input: caption (String)
    output: remaining part of caption which gives no information about category (List), category id(s) (List)
    This is the function that have to be called on the search term.
    The categoryId and remaining of the search term are outputs from get_query_category.
    Then, if the origin of category is همه, all the categoryIds from that title will be the output, as a list.
    Otherwise, the output is the same as the output of get_query_category, but in a list.
    """
    remaining, category_id = get_query_category(caption)
    # if caption doesn't have category, we return it cleaned and tokenized, and categoryId list will be empty
    if category_id == -1:
        return remaining, []
    # reading table "Category" as df

    # if the word ورزشی is in the search term and caption doesn't have a category, we return all of the categoryIds in
    # table "Category" which have word ورزشی in their title

    if category_id == -2:
        category_ids = list(category_df[category_df['Title'].str.contains('ورزشی')].Id)
        return remaining, category_ids

    # if the origin of category is همه, we return all of the categoryIds in table "Category" which have the same
    # category title

    if get_category_father(category_id, category_df) == 6:
        category_title = category_df[category_df.Id == category_id].iloc[0].Title
        similar_df = category_df[category_df.Title == category_title]
        return remaining, list(similar_df.Id)

    return remaining, [category_id]
