def get_category_father(category: int, category_df):
    """
    input: the id of category.py of the post (Integer), table 'Category' (DataFrame)
    output: the id of father of the category.py
    Since the category.py structure is hierarchical, we need the categoryId of the father of the category.py to find out if
    its gender/age is obvious or not(همه).
    """

    # valid categories are in first layer:
    # زنانه: 1
    # مردانه: 2
    # دخترانه: 3
    # پسرانه: 4
    # کودکانه و نوزاد: 5
    # همه: 6

    valid_categories = list(range(1, 7))+[632]
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