import clean_caption as cc


# output: list, categoryId. list is the remaining words (as tokens) of the query which don't have effect on category.
# remain, cID = get_query_category(txt)
def get_query_category(caption):
    caption_arr = cc.clean_caption(caption)
    # tokenizing clean caption
    # 3 for loops, each for one layer
    # first layer: woman, man, child, other
    for word1 in caption_arr:
        if word1 in ['زنانه', 'زنونه', 'خانم', 'خانوم']:

            i = caption_arr.index(word1)
            if i == 0:
                caption_arr.remove(word1)
                return caption_arr, 1
            # second layer: clothes, shoes, bag
            caption_arr.remove(word1)
            for word2 in caption_arr:
                i = caption_arr.index(word2)
                if i > 0 and caption_arr[i-1] == 'پیج':
                    continue

                # women clothes
                if word2 in ['کتشلوار', 'کت']:
                    caption_arr.remove(word2)
                    return caption_arr, 485
                if word2 == 'ست':
                    if i < len(caption_arr)-1:
                        if len(caption_arr)-i > 5:
                            next_words = caption_arr[i+1:i+6]
                        else:
                            next_words = caption_arr[i+1:len(caption_arr)]
                        # if any(i in ['رسمی', 'مجلسی', 'کت', 'دامن'] for i in next_words):
                        #     caption_arr.remove(word1)
                        #     return caption_arr, 189
                        if any(i in ['ورزشی', 'اسپورت', 'گرمکن', 'لگ', 'لگینگ'] for i in next_words):
                            caption_arr.remove(word2)
                            return caption_arr, 222
                        if any(i in ['لباسزیر', 'شورت', 'شرت', 'سوتین'] for i in next_words):
                            caption_arr.remove(word2)
                            return caption_arr, 233
                        if any(i in ['گردنبند', 'دستبند', 'انگشتر', 'گوشواره', 'آویز', 'پابند', 'زیورآلات',
                                     'بدلیجات'] for i in next_words):
                            caption_arr.remove(word2)
                            return caption_arr, 280
                    else:
                        caption_arr.remove(word2)
                        return caption_arr, 625

                if word2 in ['پیرهن', 'ماکسی', 'پیراهن']:
                    caption_arr.remove(word2)
                    if i < len(caption_arr) and caption_arr[i] in ['بارداری', 'حاملگی']:
                        caption_arr.remove(caption_arr[i])
                        return caption_arr, 469
                    return caption_arr, 486
                if word2 == 'لباس':
                    caption_arr.remove(word2)
                    if i < len(caption_arr):
                        word3 = caption_arr[i]
                        if caption_arr[i] in ['مجلسی', 'رسمی']:
                            caption_arr.remove(word3)
                            return caption_arr, 484
                        if caption_arr[i] in ['ورزشی', 'اسپورت']:
                            caption_arr.remove(word3)
                            return caption_arr, 36
                        if caption_arr[i] == 'خواب':
                            caption_arr.remove(word3)
                            return caption_arr, 190
                        if caption_arr[i] == 'راحتی':
                            caption_arr.remove(word3)
                            # if i < len(caption_arr) and caption_arr[i] in ['بارداری', 'حاملگی']:
                            #     caption_arr.remove(caption_arr[i])
                            #     return caption_arr, 205
                            return caption_arr, 191
                        if caption_arr[i] == 'شنا':
                            caption_arr.remove(word3)
                            return caption_arr, 507
                        if caption_arr[i] in ['بارداری', 'حاملگی']:
                            caption_arr.remove(word3)
                            return caption_arr, 31
                    return caption_arr, 7

                if word2 == 'ربدوشامبر':
                    caption_arr.remove(word2)
                    return caption_arr, 617

                if word2 == 'مانتو':
                    caption_arr.remove(word2)
                    if i < len(caption_arr) and caption_arr[i] in ['بارداری', 'حاملگی']:
                        caption_arr.remove(caption_arr[i])
                        return caption_arr, 497
                    return caption_arr, 489
                if word2 == 'پانچو':
                    caption_arr.remove(word2)
                    return caption_arr, 490
                if word2 == 'شنل':
                    if all(w not in ['ادکلن', 'عطر'] for w in caption_arr):
                        caption_arr.remove(word2)
                        # شنل زنانه
                        return caption_arr, 491

                if word2 == 'چادر':
                    if all(w not in ['کوهنوردی', 'کمپ', 'کمپینگ', 'مسافرتی'] for w in caption_arr):
                        caption_arr.remove(word2)
                        return 493
                    else:
                        return -1

                if word2 == 'مقنعه':
                    caption_arr.remove(word2)
                    # مقنعه زنانه
                    return caption_arr, 494
                if word2 == 'توربان':
                    caption_arr.remove(word2)
                    return caption_arr, 495

                if word2 == ['لباسزیر', 'شورت', 'سوتین']:
                    if i < len(caption_arr)-1 and caption_arr[i+1] in ['بارداری', 'حاملگی']:
                        caption_arr.remove(word2)
                        return caption_arr, 498

                if word2 in ['اسلش', 'شلوار']:
                    caption_arr.remove(word2)
                    if i < len(caption_arr) and caption_arr[i] in ['بارداری', 'حاملگی']:
                        caption_arr.remove(caption_arr[i])
                        return caption_arr, 203
                    return caption_arr, 198
                if word2 in ['سرهمی', 'اورال', 'اورآل']:
                    caption_arr.remove(word2)
                    if i < len(caption_arr) and caption_arr[i] in ['بارداری', 'حاملگی']:
                        caption_arr.remove(caption_arr[i])
                        return caption_arr, 203
                    return caption_arr, 199
                if word2 in ['ژاکت']:
                    caption_arr.remove(word2)
                    return caption_arr, 200
                if word2 in ['بافت']:
                    # caption_arr.remove(word2)
                    return caption_arr, 667
                if word2 in ['پولیور', 'پلیور']:
                    caption_arr.remove(word2)
                    return caption_arr, 201
                if word2 in ['بارداری', 'حاملگی']:
                    caption_arr.remove(word2)
                    return caption_arr, 31
                if word2 == 'کاپشن':
                    caption_arr.remove(word2)
                    return caption_arr, 208
                if word2 == 'پالتو':
                    caption_arr.remove(word2)
                    return caption_arr, 209
                if word2 in ['بارانی', 'بارونی']:
                    caption_arr.remove(word2)
                    return caption_arr, 210
                if word2 in ['جلیقه', 'وست', 'ژیله']:
                    caption_arr.remove(word2)
                    return caption_arr, 503
                if word2 in ['پافر']:
                    caption_arr.remove(word2)
                    # پافر زنانه
                    return caption_arr, 500
                if word2 in ['بلوز', 'بولوز', 'بولیز']:
                    caption_arr.remove(word2)
                    if i < len(caption_arr) and caption_arr[i] in ['بارداری', 'حاملگی']:
                        caption_arr.remove(caption_arr[i])
                        return caption_arr, 206
                    return caption_arr, 212
                if word2 == 'شومیز':
                    caption_arr.remove(word2)
                    if i < len(caption_arr) and caption_arr[i] in ['بارداری', 'حاملگی']:
                        caption_arr.remove(caption_arr[i])
                        return caption_arr, 206
                    return caption_arr, 213
                if word2 == 'بادی':
                    caption_arr.remove(word2)
                    return caption_arr, 509
                if word2 == 'شلوارک':
                    caption_arr.remove(word2)
                    return caption_arr, 215
                if word2 in ['شرتک', 'شورتک']:
                    caption_arr.remove(word2)
                    return caption_arr, 216
                if word2 == 'دامن':
                    caption_arr.remove(word2)
                    if i < len(caption_arr) and caption_arr[i] in ['بارداری', 'حاملگی']:
                        caption_arr.remove(caption_arr[i])
                        return caption_arr, 207
                    return caption_arr, 504
                if word2 in ['سارافن', 'سارافون']:
                    caption_arr.remove(word2)
                    return caption_arr, 502
                if word2 in ['لگینگ', 'لگ']:
                    caption_arr.remove(word2)
                    return caption_arr, 505
                if word2 in ['ساپرت', 'ساپورت']:
                    caption_arr.remove(word2)
                    return caption_arr, 514
                if word2 == 'کاور':
                    caption_arr.remove(word2)
                    return caption_arr, 220
                if word2 == 'گرمکن':
                    caption_arr.remove(word2)
                    return caption_arr, 221
                if word2 == 'نیمتنه':
                    caption_arr.remove(word2)
                    if i < len(caption_arr):
                        if caption_arr[i] in ['ورزشی', 'اسپورت']:
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 223
                    return caption_arr, 230
                if word2 in ['دستکش', 'دسکش']:
                    caption_arr.remove(word2)
                    # if i < len(caption_arr):
                    #     if caption_arr[i] in ['ورزشی', 'اسپورت', 'دروازه', 'بدنسازی']:
                    #         caption_arr.remove(caption_arr[i])
                    #         return caption_arr, 224
                    return caption_arr, 53
                if word2 == 'هدبند':
                    caption_arr.remove(word2)
                    # if i < len(caption_arr):
                    #     if caption_arr[i] in ['ورزشی', 'اسپورت']:
                    #         caption_arr.remove(caption_arr[i])
                    #         return caption_arr, 224
                    return caption_arr, 252
                if word2 in ['سوییشرت', 'سوئیشرت', 'سویشرت']:
                    caption_arr.remove(word2)
                    return caption_arr, 225
                if word2 == 'هودی':
                    caption_arr.remove(word2)
                    return caption_arr, 226
                if word2 == 'تیشرت':
                    caption_arr.remove(word2)
                    if i < len(caption_arr) and caption_arr[i] in ['بارداری', 'حاملگی']:
                        caption_arr.remove(caption_arr[i])
                        return caption_arr, 204
                    return caption_arr, 227
                if word2 == 'پولوشرت':
                    caption_arr.remove(word2)
                    if i < len(caption_arr) and caption_arr[i] in ['بارداری', 'حاملگی']:
                        caption_arr.remove(caption_arr[i])
                        return caption_arr, 204
                    return caption_arr, 228
                if word2 == 'تاپ':
                    caption_arr.remove(word2)
                    return caption_arr, 229
                if word2 in ['شورت', 'شرت', 'لامبادا']:
                    caption_arr.remove(word2)
                    return caption_arr, 231
                if word2 == 'سوتین':
                    caption_arr.remove(word2)
                    return caption_arr, 232
                if word2 == 'تونیک':
                    caption_arr.remove(word2)
                    return caption_arr, 499
                if word2 in ['بیکینی', 'مایو', 'بکینی']:
                    caption_arr.remove(word2)
                    return caption_arr, 507
                if word2 in ['لباسزیر', 'زیرپوش']:
                    caption_arr.remove(word2)
                    return caption_arr, 42

                # women shoes
                if word2 in ['نیمبوت', 'نیمساق']:
                    caption_arr.remove(word2)
                    return caption_arr, 43
                if word2 in ['بوت']:
                    caption_arr.remove(word2)
                    return caption_arr, 517
                if word2 in ['چکمه']:
                    caption_arr.remove(word2)
                    return caption_arr, 518
                if word2 == 'گیوه':
                    caption_arr.remove(word2)
                    return caption_arr, 45
                if word2 in ['دمپایی']:
                    if 'عطر' not in caption_arr:
                        caption_arr.remove(word2)
                        return caption_arr, 519
                if word2 in ['صندل']:
                    if 'عطر' not in caption_arr:
                        caption_arr.remove(word2)
                        return caption_arr, 520
                if word2 == 'پاشنه':
                    caption_arr.remove(word2)
                    return caption_arr, 47
                if word2 in ['کتانی', 'کتونی']:
                    caption_arr.remove(word2)
                    return caption_arr, 515
                if word2 == 'کفش' and i < len(caption_arr)-1 and (caption_arr[i+1] in ['ورزشی', 'اسپورت']):
                    caption_arr.remove(word2)
                    caption_arr.remove(caption_arr[i])
                    return caption_arr, 515
                if word2 == 'کالج':
                    caption_arr.remove(word2)
                    return caption_arr, 49
                if word2 == 'کفش':
                    if caption_arr[i+1] == 'پاشنه':
                        caption_arr.remove(word2)
                        caption_arr.remove('پاشنه')
                        return caption_arr, 47
                    else:
                        caption_arr.remove(word2)
                        return caption_arr, 516

                # women accessories
                if word2 == 'کیف':
                    caption_arr.remove(word2)
                    if i < len(caption_arr):
                        if caption_arr[i] == 'پول':
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 235
                    return caption_arr, 234
                if word2 == 'کوله':
                    caption_arr.remove(word2)
                    return caption_arr, 236
                if word2 in ['چمدان', 'چمدون']:
                    caption_arr.remove(word2)
                    return caption_arr, 237
                if word2 == 'عینک':
                    caption_arr.remove(word2)
                    return caption_arr, 51
                if word2 in ['پاپوش', 'جوراب']:
                    caption_arr.remove(word2)
                    return caption_arr, 511
                if word2 == 'جورابشلواری':
                    caption_arr.remove(word2)
                    return caption_arr, 512
                if word2 == 'ساق':
                    caption_arr.remove(word2)
                    return caption_arr, 513
                if word2 == 'کمربند':
                    caption_arr.remove(word2)
                    return caption_arr, 54
                if word2 == 'گردنبند':
                    caption_arr.remove(word2)
                    return caption_arr, 241
                if word2 == 'دستبند':
                    caption_arr.remove(word2)
                    return caption_arr, 242
                if word2 == 'انگشتر':
                    caption_arr.remove(word2)
                    return caption_arr, 243
                if word2 == 'گوشواره':
                    caption_arr.remove(word2)
                    return caption_arr, 244
                if word2 == 'پیرسینگ':
                    caption_arr.remove(word2)
                    return caption_arr, 245
                # if word2 == 'آویز':
                #     caption_arr.remove(word2)
                #     return caption_arr, 246
                if word2 == 'پابند':
                    caption_arr.remove(word2)
                    return caption_arr, 247
                if word2 in ['گل', 'سنجاق']:
                    if i < len(caption_arr)-1:
                        if caption_arr[i+1] == 'سینه':
                            caption_arr.remove(word2)
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 248
                        if caption_arr[i+1] == 'سر':
                            caption_arr.remove(word2)
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 250
                if word2 in ['زیورآلات', 'بدلیجات']:
                    caption_arr.remove(word2)
                    return caption_arr, 55
                if word2 == 'کش':
                    if i < len(caption_arr)-1:
                        if caption_arr[i+1] == 'سر':
                            caption_arr.remove(word2)
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 249
                if word2 in ['کلیپس', 'کیلیپس']:
                    caption_arr.remove(word2)
                    return caption_arr, 251
                if word2 == 'کلاه':
                    if (i < len(caption_arr)-1 and caption_arr[i+1] != 'دار') or i == len(caption_arr)-1:
                        caption_arr.remove(word2)
                        return caption_arr, 253
                if word2 in ['شال']:
                    caption_arr.remove(word2)
                    return caption_arr, 254
                if word2 in ['اسکارف', 'روسری']:
                    caption_arr.remove(word2)
                    return caption_arr, 255
                if word2 == 'مینیسکارف':
                    caption_arr.remove(word2)
                    return caption_arr, 522

                if word2 == 'تلسر':
                    caption_arr.remove(word2)
                    return caption_arr, 521

                if word2 == 'ساعت':
                    caption_arr.remove(word2)
                    return caption_arr, 59

            return caption_arr, 1
            #     if word2 == 'ست':
            #         return 176
        if word1 in ['مردونه', 'مردانه']:
            i = caption_arr.index(word1)
            if i == 0:
                caption_arr.remove(word1)
                return caption_arr, 2
            caption_arr.remove(word1)
            for word2 in caption_arr:
                i = caption_arr.index(word2)
                if i > 0 and caption_arr[i-1] == 'پیج':
                    continue

                # men clothes
                if word2 in ['کتک','کت']:
                    caption_arr.remove(word2)
                    return caption_arr, 525
                if word2 == 'کتشلوار':
                    caption_arr.remove(word2)
                    return caption_arr, 524
                if word2 == 'ست':
                    if i < len(caption_arr)-1:
                        if len(caption_arr)-i > 5:
                            next_words = caption_arr[i+1:i+6]
                        else:
                            next_words = caption_arr[i+1:len(caption_arr)]
                        # if any(i in ['رسمی', 'مجلسی', 'کت'] for i in next_words):
                        #     caption_arr.remove(word2)
                        #     return caption_arr, 259
                        if any(i in ['ورزشی', 'اسپورت', 'گرمکن', 'لگ', 'لگینگ'] for i in next_words):
                            caption_arr.remove(word2)
                            return caption_arr, 271
                        if any(i in ['لباسزیر', 'شورت', 'شرت'] for i in next_words):
                            caption_arr.remove(word2)
                            return caption_arr, 279
                    caption_arr.remove(word2)
                    return caption_arr,561
                        # if any(i in ['گردنبند', 'دستبند', 'انگشتر', 'گوشواره', 'آویز', 'زیورآلات', 'بدلیجات'] for i in
                        #        next_words):
                        #     caption_arr.remove(word2)
                        #     return caption_arr, 293
                if word2 in ['پیرهن', 'پیراهن']:
                    caption_arr.remove(word2)
                    return caption_arr, 66
                if word2 == 'لباس':
                    caption_arr.remove(word2)
                    if i < len(caption_arr):
                        # if caption_arr[i] in ['مجلسی', 'رسمی']:
                        #     caption_arr.remove(caption_arr[i])
                        #     return caption_arr, 61
                        if caption_arr[i] in ['ورزشی', 'اسپورت']:
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 68
                        # if caption_arr[i] == 'خواب':
                        #     caption_arr.remove(caption_arr[i])
                        #     return caption_arr, 260
                        if caption_arr[i] == 'راحتی':
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 666
                        if caption_arr[i] == 'شنا':
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 526
                    return caption_arr, 10
                if word2 == 'ربدوشامبر':
                    caption_arr.remove(word2)
                    return caption_arr, 527
                if word2 in ['اسلش', 'شلوار']:
                    caption_arr.remove(word2)
                    return caption_arr, 63
                if word2 in ['ژاکت']:
                    caption_arr.remove(word2)
                    return caption_arr, 262
                if word2 in ['پولیور', 'پلیور']:
                    caption_arr.remove(word2)
                    return caption_arr, 263
                if word2 == 'کاپشن':
                    caption_arr.remove(word2)
                    return caption_arr, 264
                if word2 == 'پالتو':
                    caption_arr.remove(word2)
                    return caption_arr, 265
                if word2 in ['بارانی', 'بارونی']:
                    caption_arr.remove(word2)
                    return caption_arr, 266
                if word2 in ['جلیقه', 'پافر', 'ژیله', 'وست']:
                    caption_arr.remove(word2)
                    return caption_arr, 267
                if word2 in ['بلوز', 'بولوز', 'بولیز']:
                    caption_arr.remove(word2)
                    return caption_arr, 72
                if word2 == 'شلوارک':
                    caption_arr.remove(word2)
                    return caption_arr, 67
                if word2 in ['لگینگ', 'لگ', 'ساپرت', 'ساپورت']:
                    caption_arr.remove(word2)
                    return caption_arr, 268
                if word2 == 'کاور':
                    caption_arr.remove(word2)
                    return caption_arr, 269
                if word2 == 'گرمکن':
                    caption_arr.remove(word2)
                    return caption_arr, 270
                if word2 in ['دستکش', 'دسکش']:
                    caption_arr.remove(word2)
                    # if i < len(caption_arr):
                    #     if caption_arr[i] in ['ورزشی', 'اسپورت', 'دروازه', 'بدنسازی']:
                    #         caption_arr.remove(caption_arr[i])
                    #         return caption_arr, 272
                    return caption_arr, 85
                # if word2 == 'هدبند':
                #     if i < len(caption_arr)-1:
                #         if caption_arr[i+1] in ['ورزشی', 'اسپورت']:
                #             caption_arr.remove(word2)
                #             caption_arr.remove(caption_arr[i])
                #             return caption_arr, 272
                if word2 in ['سوییشرت', 'سوئیشرت', 'سویشرت']:
                    caption_arr.remove(word2)
                    return caption_arr, 273
                if word2 == 'هودی':
                    caption_arr.remove(word2)
                    return caption_arr, 274
                if word2 == 'تیشرت':
                    caption_arr.remove(word2)
                    return caption_arr, 275
                if word2 == 'پولوشرت':
                    caption_arr.remove(word2)
                    return caption_arr, 276
                if word2 == 'تاپ':
                    caption_arr.remove(word2)
                    return caption_arr, 71
                if word2 in ['شورت', 'شرت']:
                    caption_arr.remove(word2)
                    return caption_arr, 277
                if word2 == 'مایو':
                    caption_arr.remove(word2)
                    return caption_arr, 526
                if word2 in ['رکابی', 'زیرپوش']:
                    caption_arr.remove(word2)
                    return caption_arr, 278
                if word2 == 'لباسزیر':
                    caption_arr.remove(word2)
                    return caption_arr, 74

                # men shoes
                if word2 in ['نیمبوت', 'نیمساق']:
                    caption_arr.remove(word2)
                    return caption_arr, 75
                if word2 in ['بوت', 'چکمه', 'پوتین']:
                    caption_arr.remove(word2)
                    return caption_arr, 76
                if word2 == 'گیوه':
                    caption_arr.remove(word2)
                    return caption_arr, 77
                if word2 in ['دمپایی']:
                    if 'عطر' not in caption_arr:
                        caption_arr.remove(word2)
                        return caption_arr, 78
                if word2 in ['صندل']:
                    if 'عطر' not in caption_arr:
                        caption_arr.remove(word2)
                        return caption_arr, 530
                if word2 == 'کفش' and i < len(caption_arr)-1 and (caption_arr[i+1] in ['رسمی', 'مجلسی']):
                    caption_arr.remove(word2)
                    caption_arr.remove(caption_arr[i])
                    return caption_arr, 79
                if word2 in ['کتانی', 'کتونی'] or (
                        word2 == 'کفش' and i < len(caption_arr)-1 and (
                        caption_arr[i+1] in ['ورزشی', 'اسپورت'])):
                    # return
                    caption_arr.remove(word2)
                    return caption_arr, 528
                if word2 == 'کالج':
                    caption_arr.remove(word2)
                    return caption_arr, 81
                if word2 == 'کفش':
                    caption_arr.remove(word2)
                    return caption_arr, 529

                # men accessories
                if word2 == 'کیف':
                    caption_arr.remove(word2)
                    if i < len(caption_arr):
                        if caption_arr[i] == 'پول':
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 282
                    return caption_arr, 281
                if word2 == 'کوله':
                    caption_arr.remove(word2)
                    return caption_arr, 283
                if word2 in ['چمدان', 'چمدون']:
                    caption_arr.remove(word2)
                    return caption_arr, 284
                if word2 == 'عینک':
                    caption_arr.remove(word2)
                    return caption_arr, 83
                if word2 in ['جوراب']:
                    caption_arr.remove(word2)
                    return caption_arr, 566
                if word2 == 'کمربند':
                    caption_arr.remove(word2)
                    return caption_arr, 458
                if word2 == 'ساسبند':
                    caption_arr.remove(word2)
                    return caption_arr, 459
                if word2 == 'گردنبند':
                    caption_arr.remove(word2)
                    return caption_arr, 287
                if word2 == 'دستبند':
                    caption_arr.remove(word2)
                    return caption_arr, 288
                if word2 == 'انگشتر':
                    caption_arr.remove(word2)
                    return caption_arr, 289
                # if word2 == 'گوشواره':
                #     caption_arr.remove(word2)
                #     return caption_arr, 290
                # if word2 == 'پیرسینگ':
                #     caption_arr.remove(word2)
                #     return caption_arr, 291
                # if word2 == 'آویز':
                #     caption_arr.remove(word2)
                #     return caption_arr, 292
                if word2 == 'دکمه' and (i < len(caption_arr)-1 and caption_arr[i+1] == 'سردست'):
                    caption_arr.remove(word2)
                    caption_arr.remove(caption_arr[i])
                    return caption_arr, 294
                if word2 in ['زیورآلات', 'بدلیجات']:
                    caption_arr.remove(word2)
                    return caption_arr, 87
                # if word2 in ['شالگردن', 'شال']:
                #     caption_arr.remove(word2)
                #     return caption_arr, 88
                if word2 == 'کلاه':
                    if (i < len(caption_arr)-1 and caption_arr[i+1] != 'دار') or i == len(caption_arr)-1:
                        caption_arr.remove(word2)
                        return caption_arr, 89
                if word2 in ['کراوات', 'کروات']:
                    caption_arr.remove(word2)
                    return caption_arr, 295
                if word2 == 'پاپیون':
                    caption_arr.remove(word2)
                    return caption_arr, 296
                if word2 == 'ساعت':
                    caption_arr.remove(word2)
                    return caption_arr, 91
                if word2 == 'بافت':
                    return caption_arr, 668
            return caption_arr, 2

        if word1 in ['دخترانه', 'دخترونه']:
            i = caption_arr.index(word1)
            if i == 0:
                caption_arr.remove(word1)
                return caption_arr, 3
            caption_arr.remove(word1)
            for word2 in caption_arr:
                # caption_arr.remove(word1)
                # girls clothes
                if word2 == 'کت':
                    caption_arr.remove(word2)
                    return caption_arr, 297
                if word2 == 'ست':
                    if i < len(caption_arr)-1:
                        if len(caption_arr)-i > 5:
                            next_words = caption_arr[i+1:i+6]
                        else:
                            next_words = caption_arr[i+1:len(caption_arr)]
                        # if any(i in ['رسمی', 'مجلسی', 'کت', 'دامن'] for i in next_words):
                        #     caption_arr.remove(word2)
                        #     return caption_arr, 298
                        if any(i in ['ورزشی', 'اسپورت', 'گرمکن', 'لگ', 'لگینگ'] for i in next_words):
                            caption_arr.remove(word2)
                            return caption_arr, 315
                        if any(i in ['لباسزیر', 'شورت', 'شرت', 'سوتین'] for i in next_words):
                            caption_arr.remove(word2)
                            return caption_arr, 330
                    caption_arr.remove(word2)
                    return caption_arr, 627
                if word2 in ['پیرهن', 'پیراهن']:
                    caption_arr.remove(word2)
                    return caption_arr, 624
                if word2 == 'لباس':
                    caption_arr.remove(word2)
                    if i < len(caption_arr):
                        if caption_arr[i] in ['مجلسی', 'رسمی']:
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 102
                        if caption_arr[i] in ['ورزشی', 'اسپورت']:
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 99
                        if caption_arr[i] in ['راحتی', 'خواب']:
                            caption_arr.remove(caption_arr[i])
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 93
                        if caption_arr[i] == 'شنا':
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 533
                    return caption_arr, 13
                if word2 in ['اسلش', 'شلوار']:
                    caption_arr.remove(word2)
                    return caption_arr, 304
                if word2 in ['سرهمی', 'اورال', 'اورآل']:
                    caption_arr.remove(word2)
                    return caption_arr, 305
                if word2 in ['ژاکت']:
                    caption_arr.remove(word2)
                    return caption_arr, 310
                if word2 in ['پولیور', 'پلیور']:
                    caption_arr.remove(word2)
                    return caption_arr, 311
                if word2 == 'کاپشن':
                    caption_arr.remove(word2)
                    return caption_arr, 324
                if word2 == 'پالتو':
                    caption_arr.remove(word2)
                    return caption_arr, 325
                if word2 in ['بارانی', 'بارونی']:
                    caption_arr.remove(word2)
                    return caption_arr, 326
                if word2 in ['پافر']:
                    caption_arr.remove(word2)
                    return caption_arr, 327
                if word2 in ['جلیقه', 'ژیله', 'وست']:
                    caption_arr.remove(word2)
                    return caption_arr,528
                if word2 in ['بلوز', 'بولوز', 'بولیز']:
                    caption_arr.remove(word2)
                    return caption_arr, 321
                if word2 == 'شومیز':
                    caption_arr.remove(word2)
                    return caption_arr, 322
                if word2 == 'شلوارک':
                    caption_arr.remove(word2)
                    return caption_arr, 306
                if word2 in ['شرتک', 'شورتک']:
                    caption_arr.remove(word2)
                    return caption_arr, 307
                if word2 == 'دامن':
                    caption_arr.remove(word2)
                    return caption_arr, 536
                if word2 in ['سارافن', 'سارافون']:
                    caption_arr.remove(word2)
                    return caption_arr, 623
                if word2 in ['لگینگ', 'لگ', 'ساپرت', 'ساپورت']:
                    caption_arr.remove(word2)
                    return caption_arr, 312
                # if word2 == 'کاور':
                #     caption_arr.remove(word2)
                #     return caption_arr, 313
                if word2 == 'گرمکن':
                    caption_arr.remove(word2)
                    return caption_arr, 314
                if word2 == 'نیمتنه':
                    caption_arr.remove(word2)
                    if i < len(caption_arr):
                        if caption_arr[i] in ['ورزشی', 'اسپورت']:
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 316
                    return caption_arr, 533
                if word2 in ['دستکش', 'دسکش']:
                    caption_arr.remove(word2)
                    # if i < len(caption_arr):
                    #     if caption_arr[i] in ['ورزشی', 'اسپورت', 'دروازه', 'بدنسازی']:
                    #         caption_arr.remove(caption_arr[i])
                    #         return caption_arr, 317
                    return caption_arr, 110
                if word2 == 'هدبند':
                    caption_arr.remove(word2)
                    # if i < len(caption_arr):
                    #     if caption_arr[i] in ['ورزشی', 'اسپورت']:
                    #         caption_arr.remove(caption_arr[i])
                    #         return caption_arr, 317
                    return caption_arr, 348
                if word2 in ['سوییشرت', 'سویشرت', 'سوئیشرت']:
                    caption_arr.remove(word2)
                    return caption_arr, 308
                if word2 == 'هودی':
                    caption_arr.remove(word2)
                    return caption_arr, 309
                if word2 == 'تیشرت':
                    caption_arr.remove(word2)
                    return caption_arr, 301
                if word2 == 'پولوشرت':
                    caption_arr.remove(word2)
                    return caption_arr, 302
                if word2 == 'تاپ':
                    caption_arr.remove(word2)
                    return caption_arr, 532
                if word2 in ['شورت', 'شرت']:
                    caption_arr.remove(word2)
                    return caption_arr, 328
                if word2 == 'سوتین':
                    caption_arr.remove(word2)
                    return caption_arr, 329
                if word2 == 'تونیک':
                    caption_arr.remove(word2)
                    return caption_arr, 323
                if word2 in ['بیکینی', 'مایو', 'بکینی']:
                    caption_arr.remove(word2)
                    return caption_arr, 535
                if word2 in ['لباسزیر', 'زیرپوش']:
                    caption_arr.remove(word2)
                    return caption_arr, 105
                if word2 == 'بادی':
                    caption_arr.remove(word2)
                    return caption_arr, 534
                if word2 == 'شنل':
                    if all(w not in ['ادکلن', 'عطر'] for w in caption_arr):
                        # return 195
                        caption_arr.remove(word2)
                        return caption_arr, 488

                # girls shoes
                if word2 in ['کتانی', 'کتونی']:
                    caption_arr.remove(word2)
                    return caption_arr, 537
                if word2 == 'کفش' and i < len(caption_arr)-1 and (caption_arr[i+1] in ['ورزشی', 'اسپورت']):
                    caption_arr.remove(word2)
                    caption_arr.remove(caption_arr[i])
                    return caption_arr, 537
                if word2 in ['کفش', 'پاشنه']:
                    if 'عطر' not in caption_arr:
                        caption_arr.remove(word2)
                        return caption_arr,538
                if word2 in ['بوت', 'نیمبوت', 'چکمه', 'چکمه', 'نیمساق']:
                    if 'عطر' not in caption_arr:
                        caption_arr.remove(word2)
                        return caption_arr, 539

                # girls accessories
                if word2 == 'کیف':
                    caption_arr.remove(word2)
                    if i < len(caption_arr):
                        if caption_arr[i] == 'پول':
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 332
                    return caption_arr, 331
                if word2 == 'کوله':
                    caption_arr.remove(word2)
                    return caption_arr, 333
                # if word2 in ['چمدان', 'چمدون']:
                #     caption_arr.remove(word2)
                #     return caption_arr, 334
                if word2 == 'عینک':
                    caption_arr.remove(word2)
                    return caption_arr, 108
                if word2 in ['پاپوش', 'جوراب']:
                    caption_arr.remove(word2)
                    return caption_arr, 568
                if word2 == 'جورابشلواری':
                    caption_arr.remove(word2)
                    return caption_arr, 569
                if word2 == 'ساق':
                    caption_arr.remove(word2)
                    return caption_arr, 570
                # if word2 == 'کمربند':
                #     caption_arr.remove(word2)
                #     return caption_arr, 111
                if word2 == 'گردنبند':
                    caption_arr.remove(word2)
                    return caption_arr, 338
                if word2 == 'دستبند':
                    caption_arr.remove(word2)
                    return caption_arr, 339
                if word2 == 'انگشتر':
                    caption_arr.remove(word2)
                    return caption_arr, 340
                if word2 == 'گوشواره':
                    caption_arr.remove(word2)
                    return caption_arr, 341
                # if word2 == 'آویز':
                #     caption_arr.remove(word2)
                #     return caption_arr, 342
                if word2 in ['گل', 'سنجاق']:
                    if i < len(caption_arr)-1:
                        # if caption_arr[i+1] == 'سینه':
                        #     caption_arr.remove(word2)
                        #     caption_arr.remove(caption_arr[i])
                        #     return caption_arr, 344
                        if caption_arr[i+1] == 'سر':
                            caption_arr.remove(word2)
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 346
                if word2 in ['زیورآلات', 'بدلیجات']:
                    caption_arr.remove(word2)
                    return caption_arr, 112
                if word2 == 'کش':
                    if i < len(caption_arr)-1:
                        if caption_arr[i+1] == 'سر':
                            caption_arr.remove(word2)
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 345

                if word2 == 'تلسر':
                    caption_arr.remove(word2)
                    return caption_arr, 541

                if word2 in ['کلیپس', 'کیلیپس']:
                    caption_arr.remove(word2)
                    return caption_arr, 251
                if word2 == 'کلاه':
                    if (i < len(caption_arr)-1 and caption_arr[i+1] != 'دار') or i == len(caption_arr)-1:
                        caption_arr.remove(word2)
                        return caption_arr, 349
                if word2 in ['شالگردن', 'شال']:
                    caption_arr.remove(word2)
                    return caption_arr, 350
                if word2 == 'ساعت':
                    caption_arr.remove(word2)
                    return caption_arr, 115
                # if word2 == 'ماسک':
                #     caption_arr.remove(word2)
                #     return caption_arr, 116
                # if word2 == 'ست':
                #     return 178
            return caption_arr, 3

        if word1 in ['پسرانه', 'پسرونه']:
            i = caption_arr.index(word1)
            if i == 0:
                caption_arr.remove(word1)
                return caption_arr, 4
            caption_arr.remove(word1)
            for word2 in caption_arr:
                # boys clothes
                if word2 in ['کتک','کت']:
                    caption_arr.remove(word2)
                    return caption_arr, 545
                if word2 == 'کتشلوار':
                    caption_arr.remove(word2)
                    return caption_arr, 544

                if word2 == 'ست':
                    if i < len(caption_arr)-1:
                        if len(caption_arr)-i > 5:
                            next_words = caption_arr[i+1:i+6]
                        else:
                            next_words = caption_arr[i+1:len(caption_arr)]
                        # if any(i in ['رسمی', 'مجلسی', 'کت'] for i in next_words):
                        #     caption_arr.remove(word2)
                        #     return caption_arr, 352
                        if any(i in ['ورزشی', 'اسپورت', 'گرمکن', 'لگ', 'لگینگ'] for i in next_words):
                            caption_arr.remove(word2)
                            return caption_arr, 369
                        if any(i in ['لباسزیر', 'شورت', 'شرت'] for i in next_words):
                            caption_arr.remove(word2)
                            return caption_arr, 377
                    caption_arr.remove(word2)
                    return caption_arr, 628
                        # if any(i in ['گردنبند', 'دستبند', 'انگشتر', 'آویز', 'زیورآلات', 'بدلیجات'] for i in next_words):
                        #     caption_arr.remove(word2)
                        #     return caption_arr, 388
                if word2 in ['پیرهن', 'پیراهن']:
                    caption_arr.remove(word2)
                    return caption_arr, 124
                if word2 == 'لباس':
                    caption_arr.remove(word2)
                    if i < len(caption_arr):
                        # if caption_arr[i] in ['مجلسی', 'رسمی']:
                        #     caption_arr.remove(caption_arr[i])
                        #     return caption_arr, 126
                        if caption_arr[i] in ['ورزشی', 'اسپورت']:
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 123
                        # if caption_arr[i] == 'خواب':
                        #     caption_arr.remove(caption_arr[i])
                        #     return caption_arr, 353
                        # if caption_arr[i] == 'راحتی':
                        #     caption_arr.remove(caption_arr[i])
                        #     return caption_arr, 354
                        if caption_arr[i] == 'شنا':
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 542
                    return caption_arr, 16
                if word2 in ['اسلش', 'شلوار']:
                    caption_arr.remove(word2)
                    return caption_arr, 358
                if word2 in ['سرهمی', 'اورال', 'اورآل']:
                    caption_arr.remove(word2)
                    return caption_arr, 359
                if word2 in ['ژاکت']:
                    caption_arr.remove(word2)
                    return caption_arr, 364
                if word2 in ['پولیور', 'پلیور']:
                    caption_arr.remove(word2)
                    return caption_arr, 365
                if word2 == 'کاپشن':
                    caption_arr.remove(word2)
                    return caption_arr, 371
                if word2 == 'پالتو':
                    caption_arr.remove(word2)
                    return caption_arr, 372
                if word2 in ['بارانی', 'بارونی']:
                    caption_arr.remove(word2)
                    return caption_arr, 373
                if word2 in ['وست', 'جلیقه', 'ژیله']:
                    caption_arr.remove(word2)
                    return caption_arr, 374
                if word2 in ['بلوز', 'بولوز', 'بولیز']:
                    caption_arr.remove(word2)
                    return caption_arr, 125
                if word2 == 'شلوارک':
                    caption_arr.remove(word2)
                    return caption_arr, 360
                if word2 in ['شرتک', 'شورتک']:
                    caption_arr.remove(word2)
                    return caption_arr, 361
                # if word2 in ['لگینگ', 'لگ', 'ساپرت', 'ساپورت']:
                #     caption_arr.remove(word2)
                #     return caption_arr, 366
                # if word2 == 'کاور':
                #     caption_arr.remove(word2)
                #     return caption_arr, 367
                if word2 == 'گرمکن':
                    caption_arr.remove(word2)
                    return caption_arr, 368
                # if word2 in ['دستکش', 'دسکش']:
                #     caption_arr.remove(word2)
                #     if i < len(caption_arr):
                #         if caption_arr[i] in ['ورزشی', 'اسپورت', 'دروازه', 'بدنسازی']:
                #             caption_arr.remove(caption_arr[i])
                #             return caption_arr, 370
                #     return caption_arr, 134
                # if word2 == 'هدبند':
                #     if i < len(caption_arr)-1:
                #         if caption_arr[i+1] in ['ورزشی', 'اسپورت']:
                #             caption_arr.remove(word2)
                #             caption_arr.remove(caption_arr[i])
                #             return caption_arr, 370
                if word2 in ['سوییشرت', 'سویشرت', 'سوئیشرت ']:
                    caption_arr.remove(word2)
                    return caption_arr, 362
                if word2 == 'هودی':
                    caption_arr.remove(word2)
                    return caption_arr, 363
                if word2 == 'تیشرت':
                    caption_arr.remove(word2)
                    return caption_arr, 355
                if word2 == 'پولوشرت':
                    caption_arr.remove(word2)
                    return caption_arr, 356
                if word2 == 'تاپ':
                    caption_arr.remove(word2)
                    return caption_arr, 357
                if word2 in ['شورت', 'شرت']:
                    caption_arr.remove(word2)
                    return caption_arr, 375
                if word2 == 'مایو':
                    caption_arr.remove(word2)
                    return caption_arr, 542
                if word2 in ['رکابی', 'زیرپوش']:
                    caption_arr.remove(word2)
                    return caption_arr, 376
                if word2 == 'لباسزیر':
                    caption_arr.remove(word2)
                    return caption_arr, 129

                # boys shoes
                if word2 in ['کتانی', 'کتونی']:
                    caption_arr.remove(word2)
                    return caption_arr, 546
                if word2 == 'کفش' and i < len(caption_arr)-1 and (caption_arr[i+1] in ['ورزشی', 'اسپورت']):
                    caption_arr.remove(word2)
                    caption_arr.remove(caption_arr[i])
                    return caption_arr, 546
                if word2 in ['صندل', 'دمپایی']:
                    caption_arr.remove(word2)
                    return caption_arr, 549

                if word2 in ['بوت', 'نیمبوت']:
                    caption_arr.remove(word2)
                    return caption_arr, 548

                if word2 in ['کفش', 'چکمه', 'پاشنه', 'نیمساق']:
                    if 'عطر' not in caption_arr:
                        caption_arr.remove(word2)
                        # return 17
                        return caption_arr, 547

                # boys accessories
                if word2 == 'کیف':
                    caption_arr.remove(word2)
                    if i < len(caption_arr):
                        if caption_arr[i] == 'پول':
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 379
                    return caption_arr, 378
                if word2 == 'کوله':
                    caption_arr.remove(word2)
                    return caption_arr, 380
                # if word2 in ['چمدان', 'چمدون']:
                #     caption_arr.remove(word2)
                #     return caption_arr, 381
                if word2 == 'عینک':
                    caption_arr.remove(word2)
                    return caption_arr, 132
                if word2 in ['پاپوش', 'جوراب']:
                    caption_arr.remove(word2)
                    return caption_arr, 571
                # if word2 == 'ساق':
                #     caption_arr.remove(word2)
                #     return caption_arr, 383
                if word2 == 'کمربند':
                    caption_arr.remove(word2)
                    return caption_arr, 579
                if word2 == 'ساسبند':
                    caption_arr.remove(word2)
                    return caption_arr, 580
                if word2 in ['کراوات', 'کروات']:
                    caption_arr.remove(word2)
                    return caption_arr, 461
                if word2 == 'پاپیون':
                    caption_arr.remove(word2)
                    return caption_arr, 462
                if word2 == 'ساعت':
                    caption_arr.remove(word2)
                    return caption_arr, 138
            return caption_arr, 4

        if word1 in ['نوزاد', 'نوزادی']:
            i = caption_arr.index(word1)
            if i == 0:
                caption_arr.remove(word1)
                return caption_arr, 632
            caption_arr.remove(word1)
            for word2 in caption_arr:
                # babies clothes
                if word2 == 'ست':
                    caption_arr.remove(word2)
                    return caption_arr, 636
                if word2 in ['پیرهن', 'پیراهن']:
                    caption_arr.remove(word2)
                    return caption_arr, 640
                if word2 == 'لباس':
                    caption_arr.remove(word2)
                    if i < len(caption_arr):
                        if caption_arr[i] in ['راحتی', 'خواب']:
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 637
                    return caption_arr, 633
                if word2 in ['بادی']:
                    caption_arr.remove(word2)
                    # return 412
                    return caption_arr, 645

                if word2 == 'دامن':
                    caption_arr.remove(word2)
                    return caption_arr, 652
                if word2 in ['سارافن', 'سارافون']:
                    caption_arr.remove(word2)
                    return caption_arr, 653
                if word2 == 'کاپشن':
                    caption_arr.remove(word2)
                    return caption_arr, 654
                if word2 in ['سوییشرت', 'سوئیشرت', 'سویشرت']:
                    caption_arr.remove(word2)
                    return caption_arr, 655
                if word2 == 'هودی':
                    caption_arr.remove(word2)
                    return caption_arr, 656
                if word2 == 'تیشرت':
                    caption_arr.remove(word2)
                    return caption_arr, 657
                if word2 == 'پولوشرت':
                    caption_arr.remove(word2)
                    return caption_arr, 658
                if word2 == 'تاپ':
                    caption_arr.remove(word2)
                    return caption_arr, 659
                if word2 in ['شورت', 'لباسزیر', 'زیرپوش', 'شرت']:
                    caption_arr.remove(word2)
                    return caption_arr, 644
                if word2 in ['پاپوش', 'جوراب']:
                    caption_arr.remove(word2)
                    return caption_arr, 660
                if word2 == 'جورابشلواری':
                    caption_arr.remove(word2)
                    return caption_arr, 661
                if word2 in ['اسلش', 'شلوار']:
                    caption_arr.remove(word2)
                    # return 413
                    return caption_arr, 662
                if word2 in ['سرهمی', 'اورال', 'اورآل']:
                    caption_arr.remove(word2)
                    return caption_arr, 663

                # babies shoes
                if word2 in ['کتانی', 'کتونی'] or (
                        word2 == 'کفش' and i < len(caption_arr)-1):
                    caption_arr.remove(word2)
                    return caption_arr, 647
                if word2 in ['کفش', 'بوت', 'نیمبوت', 'چکمه']:
                    if 'عطر' not in caption_arr:
                        caption_arr.remove(word2)
                        return caption_arr, 647
                if word2 in ['صندل', 'دمپایی', 'پاپوش']:
                    if 'عطر' not in caption_arr:
                        caption_arr.remove(word2)
                        return caption_arr, 648

                    # babies accessories
                    if word2 in ['دستکش', 'دسکش']:
                        caption_arr.remove(word2)
                        return caption_arr, 650
                    if word2 in ['کیف', 'کوله', 'چمدان', 'ساک', 'چمدون']:
                        caption_arr.remove(word2)
                        return caption_arr, 649
                    if word2 == 'هدبند':
                        caption_arr.remove(word2)
                        return caption_arr, 665
                    if word2 == 'کلاه':
                        if (i < len(caption_arr)-1 and caption_arr[i+1] != 'دار') or i == len(caption_arr)-1:
                            # return 470
                            caption_arr.remove(word2)
                            return caption_arr, 664
                if 'لباس' in caption_arr:
                    caption_arr.remove(word2)
                    return caption_arr, 633
            return caption_arr, 632

        if word1 in ['بچگانه', 'کودک', 'کودکانه', 'بچگونه']:
            i = caption_arr.index(word1)
            if i == 0:
                caption_arr.remove(word1)
                return caption_arr, 5
            caption_arr.remove(word1)
            for word2 in caption_arr:
                i = caption_arr.index(word2)
                if word2 == 'ست':
                    caption_arr.remove(word2)
                    return caption_arr, 564
                if word2 in ['پیرهن', 'پیراهن']:
                    caption_arr.remove(word2)
                    return caption_arr, 147
                if word2 == 'لباس':
                    caption_arr.remove(word2)
                    if i < len(caption_arr):
                        if caption_arr[i] in ['مجلسی', 'رسمی']:
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 147
                        elif caption_arr[i] in ['ورزشی', 'شنا', 'مایو']:
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 414
                        elif caption_arr[i] in ['شورت', 'شرت', 'زیرپوش']:
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 152
                        elif caption_arr[i] == 'راحتی':
                            caption_arr.remove(caption_arr[i])
                            return caption_arr, 141
                if word2 in ['سرهمی', 'اورال', 'اورآل', 'اسلش', 'شلوار']:
                    caption_arr.remove(word2)
                    return caption_arr, 413
                if word2 in ['ژاکت']:
                    caption_arr.remove(word2)
                    return caption_arr, 143
                if word2 == 'کاپشن':
                    caption_arr.remove(word2)
                    return caption_arr, 400
                if word2 == 'پالتو':
                    caption_arr.remove(word2)
                    return caption_arr, 401
                if word2 in ['بارانی', 'بارونی']:
                    caption_arr.remove(word2)
                    return caption_arr, 402
                if word2 in ['جلیقه', 'ژیله']:
                    caption_arr.remove(word2)
                    return caption_arr, 631
                if word2 in ['بلوز', 'بولوز', 'بولیز']:
                    caption_arr.remove(word2)
                    return caption_arr, 403
                if word2 == 'شلوارک':
                    caption_arr.remove(word2)
                    return caption_arr, 146
                if word2 == 'دامن':
                    caption_arr.remove(word2)
                    return caption_arr, 394
                if word2 in ['سارافن', 'سارافون']:
                    caption_arr.remove(word2)
                    return caption_arr, 395
                if word2 in ['دستکش', 'دسکش']:
                    caption_arr.remove(word2)
                    return caption_arr, 467
                #         if word2 == 'هدبند':
                #             return 21
                if word2 in ['سوییشرت', 'سویشرت', 'سوئیشرت']:
                    caption_arr.remove(word2)
                    return caption_arr, 369
                if word2 == 'هودی':
                    caption_arr.remove(word2)
                    return caption_arr, 397
                if word2 == 'تیشرت':
                    caption_arr.remove(word2)
                    return caption_arr, 406
                #         if word2 == 'پولوشرت':
                #             return 407
                if word2 == 'تاپ':
                    caption_arr.remove(word2)
                    return caption_arr, 408
                if word2 in ['پاپوش', 'جوراب']:
                    caption_arr.remove(word2)
                    return caption_arr, 409
                if word2 == 'جورابشلواری':
                    caption_arr.remove(word2)
                    return caption_arr, 410

                # kids shoes
                if word2 in ['کتانی', 'کتونی'] or (
                        word2 == 'کفش' and i < len(caption_arr)-1 and (
                        caption_arr[i+1] in ['ورزشی', 'اسپورت'])):
                    caption_arr.remove(word2)
                    return caption_arr, 598

                if word2 in ['صندل', 'دمپایی']:
                    if 'عطر' not in caption_arr:
                        caption_arr.remove(word2)
                        return caption_arr, 599
                if word2 in ['بوت', 'نیمبوت']:
                    if 'عطر' not in caption_arr:
                        caption_arr.remove(word2)
                        return caption_arr, 600

                # kids accessories
                if word2 in ['کوله', 'کیف']:
                    caption_arr.remove(word2)
                    return caption_arr, 464
                if word2 == 'عینک':
                    caption_arr.remove(word2)
                    return caption_arr, 465
                if word2 == 'کلاه':
                    if (i < len(caption_arr)-1 and caption_arr[i+1] != 'دار') or i == len(caption_arr)-1:
                        caption_arr.remove(word2)
                        return caption_arr, 470
                if word2 == 'ساعت':
                    caption_arr.remove(word2)
                    return caption_arr, 472
                if word2 in ['دستکش', 'دسکش']:
                    caption_arr.remove(word2)
                    return caption_arr, 467
            #caption_arr.remove(word2)
            return caption_arr, 5

    for word in caption_arr:
        i = caption_arr.index(word)
        if i > 0 and caption_arr[i-1] == 'پیج':
            continue
        # other clothes
        if word == 'ست':
            if i < len(caption_arr)-1:
                if len(caption_arr)-i > 5:
                    next_words = caption_arr[i+1:i+6]
                else:
                    next_words = caption_arr[i+1:len(caption_arr)]
                if any(i in ['ورزشی', 'گرمکن', 'لگ', 'لگینگ'] for i in next_words):
                    caption_arr.remove(word)
                    return caption_arr, 438
                if any(i in ['لباسزیر', 'شورت', 'شرت'] for i in next_words):
                    caption_arr.remove(word)
                    return caption_arr, 574
                if 'سوتین' in next_words:
                    caption_arr.remove(word)
                    return caption_arr, 233
                if any(i in ['گردنبند', 'دستبند', 'انگشتر', 'گوشواره', 'آویز', 'پابند', 'زیورآلات',
                             'بدلیجات'] for i in next_words):
                    caption_arr.remove(word)
                    return caption_arr, 457
            caption_arr.remove(word)
            return caption_arr, 630

        if word == 'ربدوشامبر':
            caption_arr.remove(word)
            return caption_arr, 619

        if word in ['پیرهن', 'پیراهن']:
            if i < len(caption_arr)-1 and caption_arr[i+1] in ['بارداری', 'حاملگی']:
                caption_arr.remove(word)
                return caption_arr, 496
            caption_arr.remove(word)
            return caption_arr, 155
        if word == 'لباس':
            if i < len(caption_arr)-1:
                if caption_arr[i+1] in ['مجلسی', 'رسمی']:
                    caption_arr.remove(word)
                    return caption_arr, 486
                if caption_arr[i+1] in ['ورزشی']:
                    caption_arr.remove(word)
                    return caption_arr, 163
                if caption_arr[i+1] == 'خواب':
                    caption_arr.remove(word)
                    # return 418
                    return caption_arr,190
                if caption_arr[i+1] == 'راحتی':
                    caption_arr.remove(word)
                    caption_arr.remove('راحتی')
                    return caption_arr, 419
                if caption_arr[i+1] == 'شنا':
                    caption_arr.remove(word)
                    return caption_arr, 168
                if caption_arr[i+1] in ['بارداری', 'حاملگی']:
                    caption_arr.remove(word)
                    return caption_arr, 31
            caption_arr.remove(word)
            return caption_arr, 22
        if word == 'مانتو':
            if i < len(caption_arr)-1 and caption_arr[i+1] in ['بارداری', 'حاملگی']:
                caption_arr.remove(word)
                # return 202
                return caption_arr, 497
            # return 192
            caption_arr.remove(word)
            return caption_arr, 489
        if word == 'پانچو':
            caption_arr.remove(word)
            # return 193
            return caption_arr, 490
        if word == 'شنل':
            if all(w not in ['ادکلن', 'عطر', 'کفش', 'کیف'] for w in caption_arr):
                caption_arr.remove(word)
                # return 195
                return caption_arr, 491

        if word == 'چادر':
            if all(w not in ['کوهنوردی', 'کمپ', 'مسافرتی', 'کمپینگ'] for w in caption_arr):
                # return 196
                caption_arr.remove(word)
                return caption_arr, 493
            else:
                return -1

        if word == 'مقنعه':
            caption_arr.remove(word)
            # return 197
            return caption_arr, 494
        if word == 'توربان':
            caption_arr.remove(word)
            return caption_arr, 495
        if word in ['اسلش', 'شلوار']:
            if i < len(caption_arr)-1 and caption_arr[i+1] in ['بارداری', 'حاملگی']:
                caption_arr.remove(word)
                return caption_arr, 203
            caption_arr.remove(word)
            return caption_arr, 420
        if word in ['سرهمی', 'اورال', 'اورآل']:
            if i < len(caption_arr)-1 and caption_arr[i+1] in ['بارداری', 'حاملگی']:
                caption_arr.remove(word)
                return caption_arr, 203
            caption_arr.remove(word)
            return caption_arr, 421

        # if word in ['بافت', 'ژاکت']:
        if word in ['ژاکت']:
            caption_arr.remove(word)
            return caption_arr, 422
        if word in ['پولیور', 'پلیور']:
            caption_arr.remove(word)
            return caption_arr, 423
        if word in ['بارداری', 'حاملگی']:
            caption_arr.remove(word)
            return caption_arr, 31
        if word == 'کاپشن':
            caption_arr.remove(word)
            return caption_arr, 424
        if word == 'پالتو':
            caption_arr.remove(word)
            return caption_arr, 425
        if word in ['بارانی', 'بارونی']:
            caption_arr.remove(word)
            return caption_arr, 426
        if word in ['جلیقه', 'ژیله']:
            caption_arr.remove(word)
            return caption_arr, 427
        if word in ['پافر']:
            caption_arr.remove(word)
            return caption_arr, 670
        if word in ['وست']:
            caption_arr.remove(word)
            return caption_arr, 503
        if word in ['بلوز', 'بولوز', 'بولیز']:
            if i < len(caption_arr)-1 and caption_arr[i+1] in ['بارداری', 'حاملگی']:
                caption_arr.remove(word)
                return caption_arr, 206
            caption_arr.remove(word)
            return caption_arr, 428
        if word == 'شومیز':
            if i < len(caption_arr)-1 and caption_arr[i+1] in ['بارداری', 'حاملگی']:
                caption_arr.remove(word)
                return caption_arr, 206
            caption_arr.remove(word)
            return caption_arr, 213
        if word == 'شلوارک':
            caption_arr.remove(word)
            return caption_arr, 431
        if word in ['شرتک', 'شورتک']:
            caption_arr.remove(word)
            return caption_arr, 432
        if word == 'دامن':
            if i < len(caption_arr)-1 and caption_arr[i+1] in ['بارداری', 'حاملگی']:
                caption_arr.remove(word)
                return caption_arr, 207
            caption_arr.remove(word)
            return caption_arr, 504
        if word in ['سارافن', 'سارافون', 'سارافان']:
            caption_arr.remove(word)
            # return 434
            return caption_arr, 502
        if word in ['لگینگ', 'لگ']:
            caption_arr.remove(word)
            return caption_arr, 505
        if word in ['لگینگ', 'لگ', 'ساپرت', 'ساپورت']:
            caption_arr.remove(word)
            return caption_arr, 514
        if word == 'کاور':
            caption_arr.remove(word)
            return caption_arr, 436
        if word == 'گرمکن':
            caption_arr.remove(word)
            return caption_arr, 437
        if word == 'نیمتنه':
            if i < len(caption_arr)-1:
                if caption_arr[i+1] in ['ورزشی', 'اسپورت']:
                    caption_arr.remove(word)
                    return caption_arr, 223
            caption_arr.remove(word)
            return caption_arr, 230
        if word in ['دستکش', 'دسکش']:
            caption_arr.remove(word)
            return caption_arr, 181
        if word == 'هدبند':
            caption_arr.remove(word)
            return caption_arr, 252
        if word in ['سوییشرت', 'سوئیشرت', 'سویشرت']:
            caption_arr.remove(word)
            return caption_arr, 440
        if word == 'هودی':
            caption_arr.remove(word)
            return caption_arr, 441
        if word == 'تیشرت':
            if i < len(caption_arr)-1 and caption_arr[i+1] in ['بارداری', 'حاملگی']:
                caption_arr.remove(word)
                return caption_arr, 204
            caption_arr.remove(word)
            return caption_arr, 442
        if word == 'پولوشرت':
            if i < len(caption_arr)-1 and caption_arr[i+1] in ['بارداری', 'حاملگی']:
                caption_arr.remove(word)
                return caption_arr, 204
            caption_arr.remove(word)
            return caption_arr, 443
        if word == 'تاپ':
            caption_arr.remove(word)
            return caption_arr, 444
        if word == 'بادی':
            caption_arr.remove(word)
            return caption_arr, 565
        if word in ['شورت', 'شرت']:
            caption_arr.remove(word)
            return caption_arr, 575
        if word == 'سوتین':
            caption_arr.remove(word)
            return caption_arr, 232
        # if word == 'تونیک':
        #     return 430
        if word in ['بیکینی', 'بکینی']:
            caption_arr.remove(word)
            return caption_arr, 507
        if word == 'مایو':
            caption_arr.remove(word)
            return caption_arr, 168
        if word == 'لامبادا':
            caption_arr.remove(word)
            return caption_arr, 231
        if word in ['رکابی', 'زیرپوش']:
            caption_arr.remove(word)
            return caption_arr, 278
        if word == 'کت':
            caption_arr.remove(word)
            return caption_arr, 620
        if word == 'بافت':
            return caption_arr, 669

        # other shoes
        # if word == 'کفش' and i < len(caption_arr)-1 and (caption_arr[i+1] in ['ساق', 'ساقدار']):
        #     caption_arr.remove(word)
        #     return caption_arr, 170
        if word ==  'کفش' and i < len(caption_arr)-1:
            if  caption_arr[i+1] == 'پاشنه':
                caption_arr.remove(word)
                caption_arr.remove('پاشنه')
                return  caption_arr,47
            elif caption_arr[i+1] in ['ساق', 'ساقدار']:
                caption_arr.remove(word)
                return caption_arr, 170


            # return 43
        if word in ['نیمبوت']:
            caption_arr.remove(word)
            return caption_arr, 170
            # return 43
        if word == 'بوت':
            caption_arr.remove(word)
            return caption_arr, 171
        if word == 'چکمه':
            caption_arr.remove(word)
            return caption_arr, 518
        if word == 'گیوه':
            caption_arr.remove(word)
            return caption_arr, 172
        if word in ['دمپایی']:
            if 'عطر' not in caption_arr:
                caption_arr.remove(word)
                return caption_arr, 173
        if word in ['صندل']:
            if 'عطر' not in caption_arr:
                caption_arr.remove(word)
                return caption_arr, 576
        if word == 'پاشنه':
            caption_arr.remove(word)
            return caption_arr, 47
        if word == 'کفش' and i < len(caption_arr)-1 and (caption_arr[i+1] in ['رسمی', 'مجلسی']):
            caption_arr.remove(word)
            return caption_arr, 79
        if word in ['کتانی', 'کتونی'] or (
                word == 'کفش' and i < len(caption_arr)-1 and (caption_arr[i+1] in ['ورزشی', 'اسپورت'])):
            caption_arr.remove(word)
            return caption_arr, 577
        if word == 'کالج':
            caption_arr.remove(word)
            return caption_arr, 176
        if word == 'کفش':
            caption_arr.remove(word)
            return caption_arr, 23

        # other accessories
        if word == 'کیف':
            if i < len(caption_arr)-1:
                if caption_arr[i+1] == 'پول':
                    caption_arr.remove(word)
                    return caption_arr, 446
            caption_arr.remove(word)
            return caption_arr, 445
        if word == 'کوله':
            caption_arr.remove(word)
            return caption_arr, 447
        if word in ['چمدان', 'چمدون']:
            caption_arr.remove(word)
            return caption_arr, 448
        if word == 'عینک':
            caption_arr.remove(word)
            return caption_arr, 179
        if word in ['پاپوش', 'جوراب']:
            caption_arr.remove(word)
            return caption_arr, 573
        if word == 'جورابشلواری':
            caption_arr.remove(word)
            return caption_arr, 512
        if word == 'ساق' and caption_arr[i+1] != 'کفش':
            caption_arr.remove(word)
            return caption_arr, 513
        if word == 'کمربند':
            caption_arr.remove(word)
            return caption_arr, 182
        if word == 'ساسبند':
            caption_arr.remove(word)
            return caption_arr, 459
        if word == 'گردنبند':
            caption_arr.remove(word)
            return caption_arr, 452
        if word == 'دستبند':
            caption_arr.remove(word)
            return caption_arr, 242
        if word == 'انگشتر':
            caption_arr.remove(word)
            return caption_arr, 454
        if word == 'گوشواره':
            caption_arr.remove(word)
            return caption_arr, 244
        if word == 'پیرسینگ':
            caption_arr.remove(word)
            return caption_arr, 245
        if word == 'پابند':
            caption_arr.remove(word)
            return caption_arr, 247
        if word == 'دکمه' and (i < len(caption_arr)-1 and caption_arr[i+1] == 'سردست'):
            caption_arr.remove(word)
            return caption_arr, 294
        if word in ['گل', 'سنجاق']:
            if i < len(caption_arr)-1:
                if caption_arr[i+1] == 'سینه':
                    caption_arr.remove(word)
                    return caption_arr, 248
                if caption_arr[i+1] == 'سر':
                    caption_arr.remove(word)
                    return caption_arr, 250
        if word in ['زیورآلات', 'بدلیجات']:
            caption_arr.remove(word)
            return caption_arr, 183
        if word == 'کش':
            if i < len(caption_arr)-1:
                if caption_arr[i+1] == 'سر':
                    caption_arr.remove(word)
                    return caption_arr, 249
        if word in ['کلیپس', 'کیلیپس']:
            caption_arr.remove(word)
            return caption_arr, 251
        if word == 'کلاه':
            if (i < len(caption_arr)-1 and caption_arr[i+1] != 'دار') or i == len(caption_arr)-1:
                caption_arr.remove(word)
                return caption_arr, 184
        if word in ['شال']:
            caption_arr.remove(word)
            return caption_arr, 254
        if word == 'تلسر':
            caption_arr.remove(word)
            return caption_arr,521
        if word in ['اسکارف', 'روسری']:
            caption_arr.remove(word)
            return caption_arr, 255
        if word == 'مینیسکارف':
            caption_arr.remove(word)
            return caption_arr, 522
        if word in ['کراوات', 'کروات']:
            caption_arr.remove(word)
            return caption_arr, 295
        if word == 'پاپیون':
            caption_arr.remove(word)
            return caption_arr, 296
        if word == 'ساعت':
            caption_arr.remove(word)
            return caption_arr, 186
        if word == 'تونیک':
            caption_arr.remove(word)
            return caption_arr, 499

        if word == 'ورزشی':
            caption_arr.remove(word)
            return caption_arr, -2
    else:
        return caption_arr, -1
