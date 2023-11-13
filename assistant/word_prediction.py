# import libraries
# import nltk

"""def word_prediction(string,fdist):
    lst = []
    for i in range(len(fdist)):
        distance = nltk.edit_distance(string, fdist[str(i)])
        if distance <= 2 and fdist[str(i)].startswith(string):
            lst.append(fdist[str(i)])
            if len(lst) >= 3:
                break
    return lst[:3]"""


# def word_prediction(string, fdist):
#     lst0 = []
#     lst1 = []
#     lst2 = []
#     for i in range(len(fdist)):
#         distance = nltk.edit_distance(string, fdist[str(i)])
#         if distance <= 1 and fdist[str(i)].startswith(string):
#             lst0.append(fdist[str(i)])
#             if lst0:
#                 #print(lst0)
#                 break
#     for i in range(len(fdist)):
#         distance = nltk.edit_distance(string, fdist[str(i)])
#         if distance <= 2 and fdist[str(i)].startswith(string):
#             if fdist[str(i)] not in lst0:
#                 lst1.append(fdist[str(i)])
#                 if len(lst1) >= 2:
#                     #print(lst1)
#                     break
#     for i in range(len(fdist)):
#         distance = nltk.edit_distance(string, fdist[str(i)])
#         if distance <= 1:
#             if not lst0 + lst1:
#                 lst2.append(fdist[str(i)])
#                 if lst2:
#                     #print(lst2)
#                     break
#
#     return lst0 + lst1[:2] + lst2[:2]