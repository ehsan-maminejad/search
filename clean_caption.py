import re
from unidecode import unidecode


def get_stop_words():
    with open('persian', encoding='utf-8') as f:
        content = f.read()
        stop_words = content.split()
    return stop_words


def remove_hashtags(caption):
    caption = re.sub('#(_*[a-zآ-ی0-9]*_*)+', '', caption)
    return caption


def clean_caption(caption):
    stop_words = get_stop_words()
    caption = remove_hashtags(caption)

    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\u3030"
                               u"\xb9"
                               "]+", flags=re.UNICODE)
    caption = emoji_pattern.sub(r' ', caption)

    ### 1 - with no persian number###
    caption = re.split('', caption)
    for i in range(len(caption)):
        if unidecode(caption[i]).isnumeric():
            caption[i] = unidecode(caption[i])
    caption = ''.join(caption)


    ### 2 - some extra stafs###
    caption = re.sub('\n+', ' ', caption)
    caption = caption.replace('\u200c', " ")  # halfspace to space
    caption = caption.replace('ي', "ی")
    caption = re.sub(r' +', ' ', caption)  # remove extra spaces
    caption = re.sub(r'[ـ\r]', '', caption)  # remove keshide, carriage returns
    caption = re.sub(r'\n\n+', '\n\n', caption)  # remove extra newlines
    caption = re.sub(r'[\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652]', '',
                     caption)  # remove FATHATAN, DAMMATAN, KASRATAN, FATHA, DAMMA, KASRA, SHADDA, SUKUN
    caption = caption.replace('ك', "ک")
    caption = caption.replace('أ', 'ا')

    caption = re.sub('\'', '', caption)
    # caption = re.sub('\w*\d\w*', '', caption) # removes any alphanumeric word
    caption = re.sub(' +', ' ', caption)
    caption = re.sub(r'\n: \'\'.*', '', caption)
    caption = re.sub(r'\n!.*', '', caption)
    caption = re.sub(r'^:\'\'.*', '', caption)
    caption = re.sub(r'\n', ' ', caption)
    caption = re.sub(r'[^\w\s]', ' ', caption)
    # caption = re.sub('[^آ-ی_ \n,،]', '', caption)

    caption = re.sub(r'\bتی شرت\b', 'تیشرت', caption)
    caption = re.sub(r'\bپولو شرت\b', 'پولوشرت', caption)
    caption = re.sub(r'\bنیم تنه\b', 'نیمتنه', caption)
    caption = re.sub(r'\bزیر پوش\b', 'زیرپوش', caption)
    caption = re.sub(r'\bلباس زیر\b', 'لباسزیر', caption)
    caption = re.sub(r'\bپا پوش\b', 'پاپوش', caption)
    caption = re.sub(r'\bسر همی\b', 'سرهمی', caption)
    caption = re.sub(r'\bسویی شرت\b', 'سوییشرت', caption)
    caption = re.sub(r'\bسوئی شرت\b', 'سوییشرت', caption)
    caption = re.sub(r'\bنیم بوت\b', 'نیمبوت', caption)
    caption = re.sub(r'\bاسپرت\b', 'اسپورت', caption)
    caption = re.sub(r'\bگرم کن\b', 'گرمکن', caption)
    caption = re.sub(r'\bهد بند\b', 'هدبند', caption)
    caption = re.sub(r'\bجوراب شلواری\b', 'جورابشلواری', caption)
    caption = re.sub(r'\bکمر بند\b', 'کمربند', caption)
    caption = re.sub(r'\bگردن بند\b', 'گردنبند', caption)
    caption = re.sub(r'\bدست بند\b', 'دستبند', caption)
    caption = re.sub(r'\bگوشوار\b', 'گوشواره', caption)
    caption = re.sub(r'\bگوش وار\b', 'گوشواره', caption)
    caption = re.sub(r'\bگوش واره\b', 'گوشواره', caption)
    caption = re.sub(r'\bپا بند\b', 'پابند', caption)
    caption = re.sub(r'\bساس بند\b', 'ساسبند', caption)
    caption = re.sub(r'\bسر دست\b', 'سردست', caption)
    caption = re.sub(r'\bنیم ساق\b', 'نیمساق', caption)
    caption = re.sub(r'\bمینی اسکارف\b', 'مینیسکارف', caption)
    caption = re.sub(r'\bتل سر\b', 'تلسر', caption)
    caption = re.sub(r'\bکت شلوار\b', 'کتشلوار', caption)
    caption = re.sub(r'\bکت و شلوار\b', 'کتشلوار', caption)
    caption = re.sub(r'\bکت تک\b', 'کتک', caption)
    # caption = re.sub(r'\bپاشنه دار\b', 'پاشنه', caption)
    # caption = re.sub(r'\bپاشنه بلند\b', 'پاشنه', caption)
    caption = re.sub(r'\bکوله پشتی\b', 'کوله', caption)
    # caption = re.sub(r'\bکت\b', 'کتک', caption)

    # modifying colors
    # replacing similar words and handling two words color
    caption = re.sub(r'\bسورمه ای\b', 'سرمه', caption)
    caption = re.sub(r'\bسرمه ای\b', 'سرمه', caption)
    caption = re.sub(r'\bسورمه\b', 'سرمه', caption)

    # handling blue colors
    caption = re.sub(r'\bابی\b', 'آبی', caption)
    caption = re.sub(r'\bآبی آسمانی\b', 'آبیاس', caption)
    caption = re.sub(r'\bآبی روشن\b', 'آبیرو', caption)
    caption = re.sub(r'\bآبی نفتی\b', 'آبینف', caption)
    caption = re.sub(r'\bآبی فیروزه ای\b', 'آبیفیرو', caption)
    caption = re.sub(r'\bآبی کاربنی\b', 'آبیکار', caption)
    caption = re.sub(r'\bآبی کمرنگ\b', 'آبیکم', caption)

    # handling green colors
    caption = re.sub(r'\bسبز روشن\b', 'سبزروش', caption)
    caption = re.sub(r'\bسبز ارتشی\b', 'سبزار', caption)
    caption = re.sub(r'\bسبز آبی\b', 'سبزاب', caption)
    caption = re.sub(r'\bسبز کله غازی\b', 'سبزکلغ', caption)
    caption = re.sub(r'\bآبی آسمانی\b', 'آبیاس', caption)

    # handling gray colors
    caption = re.sub(r'\bتوسی\b', 'طوسی', caption)
    caption = re.sub(r'\bطوسی روشن\b', 'طوسیرو', caption)
    caption = re.sub(r'\bطوسی تیره\b', 'طوسیتی', caption)

    # handling other colors
    caption = re.sub(r'\bسرخ آبی\b', 'سرخابی', caption)
    caption = re.sub(r'\bفیروزه ای\b', 'فیروزا', caption)
    caption = re.sub(r'\bقهوه ای\b', 'قهوها', caption)
    caption = re.sub(r'\bگوجه ای\b', 'گوجا', caption)
    caption = re.sub(r'\bنقره ای\b', 'نقرا', caption)
    caption = re.sub(r'\bنوک مدادی\b', 'نوکمدادی', caption)
    caption = re.sub(r'\bمدادی\b', 'نوکمدادی', caption)
    caption = re.sub(r'\bپوست پیازی\b', 'پوستپیاز', caption)
    caption = re.sub(r'\bنسکافه ای\b', 'نسکافا', caption)
    caption = re.sub(r'\bکرم\b', 'کرمی', caption)
    caption = re.sub(r'\bسیاه\b', 'مشکی', caption)
    caption = re.sub(r'\bبادمجونی\b', 'بادمجانی', caption)

    # handling the word "رنگ"
    caption = re.sub(r'\bرنگبندی\b', 'رنگ', caption)
    caption = re.sub(r'\bرنگ بندی\b', 'رنگ', caption)
    caption = re.sub(r'\bرنکبندی\b', 'رنگ', caption)
    caption = re.sub(r'\bرنگهای\b', 'رنگ', caption)
    caption = re.sub(r'\b1 رنگ\b', 'تک رنگ', caption)
    caption = re.sub(r'\b2 رنگ\b', 'دو رنگ', caption)
    caption = re.sub(r'\b3 رنگ\b', 'سه رنگ', caption)
    caption = re.sub(r'\b4 رنگ\b', 'چهار رنگ', caption)
    caption = re.sub(r'\b4رنگ\b', 'چهار رنگ', caption)
    caption = re.sub(r'\b5 رنگ\b', 'پنج رنگ', caption)
    caption = re.sub(r'\b5رنگ\b', 'پنج رنگ', caption)
    caption = re.sub(r'\b6 رنگ\b', 'شش رنگ', caption)
    caption = re.sub(r'\b7 رنگ\b', 'هفت رنگ', caption)
    caption = re.sub(r'\b8 رنگ\b', 'هشت رنگ', caption)
    caption = re.sub(r'\b9 رنگ\b', 'نه رنگ', caption)
    caption = re.sub(r'\bرنگ های\b', 'رنگ', caption)

    # handling similar words
    caption = re.sub(r'\bتصویر\b', 'تصاویر', caption)
    caption = re.sub(r'\bعکس\b', 'تصاویر', caption)
    caption = re.sub(r'\bذغالی\b', 'زغالی', caption)

    caption = re.sub(r'\bآدیداس\b', 'ادیداس', caption)

    ### replacing similar words and handling two words material

    # handling کرپ material
    caption = re.sub(r'\bکرپ اسکاچی\b', 'کرپاسکاچ', caption)
    caption = re.sub(r'\bکرپ فلورانس\b', 'کرپفلور', caption)
    caption = re.sub(r'\bکرپ ژرژت\b', 'کرپژرژ', caption)
    caption = re.sub(r'\bکرپ کش\b', 'کرپکش', caption)
    caption = re.sub(r'\bکرپ باربی\b', 'کرپبارب', caption)
    caption = re.sub(r'\bکرپ مازراتی\b', 'کرپمازرا', caption)
    caption = re.sub(r'\bکرپ دیور\b', 'کرپدیور', caption)
    caption = re.sub(r'\bکرپ گاباردین\b', 'کرپگابار', caption)
    caption = re.sub(r'\bکرپ کاترینا\b', 'کرپکاترین', caption)
    caption = re.sub(r'\bکرپ مقنعه ای\b', 'کرپمق', caption)
    caption = re.sub(r'\bکرپ می سی نو\b', 'کرپمیسینو', caption)
    caption = re.sub(r'\bکرپ گلنس\b', 'کرپگلنس', caption)
    caption = re.sub(r'\bکرپ فرانسوی\b', 'کرپفرانس', caption)
    caption = re.sub(r'\bکرپ غواصی\b', 'کرپغواص', caption)
    caption = re.sub(r'\bکرپ پلاس\b', 'کرپلاس', caption)
    caption = re.sub(r'\bکرپ کریشه\b', 'کرپکریش', caption)
    caption = re.sub(r'\bکرپ بوگاتی\b', 'کربوگات', caption)
    caption = re.sub(r'\bکرپ میشل\b', 'کرمیشل', caption)
    caption = re.sub(r'\bکرپ گریت\b', 'کرگریت', caption)
    caption = re.sub(r'\bکرپ جودون\b', 'کرپجودو', caption)
    caption = re.sub(r'\bکرپ یاخما\b', 'کریاخما', caption)
    caption = re.sub(r'\bکرپ شنی\b', 'کرشنی', caption)
    caption = re.sub(r'\bکرپ حریر\b', 'کرپحر', caption)

    # handling ملانژ material
    caption = re.sub(r'\bملانژ خاویاری\b', 'ملانژخاویار', caption)
    caption = re.sub(r'\bملانژ پنبه\b', 'ملانژپنبه', caption)

    # handling کریشه material
    caption = re.sub(r'\bکریشه پفکی\b', 'کریشپفک', caption)
    caption = re.sub(r'\bکریشه نخی\b', 'کریشنخ', caption)

    # handling پنبه material
    caption = re.sub(r'\bپنبه کش\b', 'پنبکش', caption)
    caption = re.sub(r'\bپنبه لاکرا\b', 'پنلاک', caption)
    caption = re.sub(r'\bپنبه ویسکوز\b', 'پنویسکو', caption)

    # handling چرم material
    caption = re.sub(r'\bچرم مصنوعی\b', 'چرمصنوع', caption)
    caption = re.sub(r'\bچرم بیاله\b', 'چرمبیاله', caption)
    caption = re.sub(r'\bچرم حوله ای\b', 'چرمحوله', caption)
    caption = re.sub(r'\bچرم صنعتی\b', 'چرمصنعت', caption)

    # handling نخ material
    caption = re.sub(r'\bنخ پنبه\b', 'نخپنبه', caption)
    caption = re.sub(r'\bنخ بامبو\b', 'نخبامبو', caption)
    caption = re.sub(r'\bنخ استرچ\b', 'نخاسترچ', caption)
    caption = re.sub(r'\bنخی سنگشور\b', 'نخیسنگ', caption)
    caption = re.sub(r'\bنخ سنگشور\b', 'نخیسنگ', caption)
    caption = re.sub(r'\bنخی\b', 'نخ', caption)
    caption = re.sub(r'\bنخ اکرولیک\b', 'نخاکرولیک', caption)
    caption = re.sub(r'\bنخ ملانژ\b', 'نخملانژ', caption)
    caption = re.sub(r'\bنخ ژاکارد\b', 'نخژاکارد', caption)

    # handling مخمل material
    caption = re.sub(r'\bمخمل سوییت\b', 'مخسوییت', caption)
    caption = re.sub(r'\bمخمل کبریتی\b', 'مخکبریتی', caption)

    # handling کرکی material
    caption = re.sub(r'\bکرکی\b', 'توکرکی', caption)

    # handling لمه material
    caption = re.sub(r'\bلمه سیمی\b', 'لمسیمی', caption)
    caption = re.sub(r'\bسوپر لمه\b', 'سوپرلمه', caption)
    caption = re.sub(r'\bلمه بیزو\b', 'لمبیزو', caption)

    # handling کتان material
    caption = re.sub(r'\bکتون\b', 'کتان', caption)
    caption = re.sub(r'\bکتان کش\b', 'کتکش', caption)
    caption = re.sub(r'\bکتان پنبه\b', 'کتپنبه', caption)

    # handling other materials
    caption = re.sub(r'\bسوپر سافت\b', 'سوپرسافت', caption)
    caption = re.sub(r'\bحوله ای\b', 'حولا', caption)
    caption = re.sub(r'\bتور کش\b', 'تورکش', caption)
    caption = re.sub(r'\bتور کشی\b', 'تورکش', caption)
    caption = re.sub(r'\bابر و بادی\b', 'ابروبادی', caption)
    caption = re.sub(r'\bابرو بادی\b', 'ابروبادی', caption)
    caption = re.sub(r'\bابر وبادی\b', 'ابروبادی', caption)
    caption = re.sub(r'\bابروباد\b', 'ابروبادی', caption)
    caption = re.sub(r'\bوال اسلپ\b', 'والاسپ', caption)
    caption = re.sub(r'\bمیکرو جودون\b', 'میکروجودون', caption)
    caption = re.sub(r'\bغواصی گلاسکو\b', 'غواصیگلاس', caption)
    caption = re.sub(r'\bداکرون میله ای\b', 'داکرومیل', caption)
    caption = re.sub(r'\bجین کاغذی\b', 'جینکاغذ', caption)
    caption = re.sub(r'\bکانیوم ترک\b', 'کانیترک', caption)
    caption = re.sub(r'\bفانریپ کش\b', 'فانکش', caption)
    caption = re.sub(r'\bفانریپ کشی\b', 'فانکش', caption)
    caption = re.sub(r'\bجودون کشی\b', 'جودونکش', caption)
    caption = re.sub(r'\bجودون کش\b', 'جودونکش', caption)
    caption = re.sub(r'\bگیپور نشمیل\b', 'گیپنشمیل', caption)
    caption = re.sub(r'\bبنگال کش\b', 'بنگالکش', caption)
    caption = re.sub(r'\bبنگال کشی\b', 'بنگالکش', caption)
    caption = re.sub(r'\bاماس\b', 'آماس', caption)
    caption = re.sub(r'\bلنین\b', 'لینن', caption)
    caption = re.sub(r'\bاسترچ\b', 'استرج', caption)
    caption = re.sub(r'\bفیلامنت\b', 'فلامنت', caption)
    caption = re.sub(r'\bکاور پارچه ای\b', ' ', caption)
    caption = re.sub(r'\bپارچه ای\b', 'پارچهای', caption)
    caption = re.sub(r'\bدورس ملانژ\b', 'دورسملانژ', caption)
    caption = re.sub(r'\bتاری پودی\b', 'تاریپودی', caption)
    caption = re.sub(r'\bنخ اکریليک\b', 'نخاکریليک', caption)
    caption = re.sub(r'\bجین کشی\b', 'جینکشی', caption)



    ### handeling attributes ###
    caption = re.sub(r'\bیقه دار\b', 'یقهدار', caption)
    caption = re.sub(r'\bیقه اسکی\b', 'یقهاسکی', caption)
    caption = re.sub(r'\bیقه گرد\b', 'یقهگرد', caption)
    caption = re.sub(r'\bآستین بلند\b', 'آستینبلند', caption)
    caption = re.sub(r'\bاستین بلند\b', 'آستینبلند', caption)
    caption = re.sub(r'\bآستین کوتاه\b', 'آستینکوتاه', caption)
    caption = re.sub(r'\bاستین کوتاه\b', 'آستینکوتاه', caption)
    caption = re.sub(r'\bآستین حلقه\b', 'آستینحلقه', caption)
    caption = re.sub(r'\bیقه هفت\b', 'یقههفت', caption)
    caption = re.sub(r'\bطرح ترمه\b', 'طرحترمه', caption)
    caption = re.sub(r'\bچارخونه\b', 'چهارخونه', caption)
    caption = re.sub(r'\bچهار خونه\b', 'چهارخونه', caption)
    caption = re.sub(r'\bحوله ای\b', 'حولهای', caption)
    caption = re.sub(r'\bیقه قایقی\b', 'یقهقایقی', caption)
    caption = re.sub(r'\bیقه مردانه\b', 'یقهمردانه', caption)
    caption = re.sub(r'\bآستین\b', 'استین', caption)
    caption = re.sub(r'\bاستین پفی\b', 'استینپفی', caption)
    caption = re.sub(r'\bاستین کلوش\b', 'استینکلوش', caption)
    caption = re.sub(r'\bسوزن دوزی\b', 'سوزندوزی', caption)
    caption = re.sub(r'\bچاپ زول\b', 'چاپزول', caption)
    caption = re.sub(r'\bشش جیب\b', 'شش جیب', caption)
    caption = re.sub(r'\bپاشنه بلند\b', 'پاشنهبلند', caption)


    ### handeling brands ###
    caption = re.sub(r'\bدولچه گابانا\b', 'دولچهگابانا', caption)
    caption = re.sub(r'\bلویی ویتون\b', 'لوییویتون', caption)
    caption = re.sub(r'\bرالف رولن پولو\b', 'رالفرولنپولو', caption)
    caption = re.sub(r'\bورا وانگ\b', 'وراوانگ', caption)
    caption = re.sub(r'\bویکتوریا سکرت\b', 'ویکتوریاسکرت', caption)
    caption = re.sub(r'\bمیو میو\b', 'میومیو', caption)
    caption = re.sub(r'\bتام فورد\b', 'تامفورد', caption)
    caption = re.sub(r'\bاندر ارمور\b', 'اندرارمور', caption)
    caption = re.sub(r'\bنیو بالانس\b', 'نیوبالانس', caption)
    caption = re.sub(r'\bکی سوِییس\b', 'کیسوِییس', caption)
    caption = re.sub(r'\bکانورس ال استار\b', 'کانورسالاستار', caption)
    caption = re.sub(r'\bچرم درسا\b', 'چرمدرسا', caption)
    caption = re.sub(r'\bچرم مشهد\b', 'چرممشهد', caption)
    caption = re.sub(r'\bپارینه چرم\b', 'پارینهچرم', caption)
    caption = re.sub(r'\bمارال چرم\b', 'مارالچرم', caption)
    caption = re.sub(r'\bچرم پاندورا\b', 'چرمپاندورا', caption)
    caption = re.sub(r'\bچرم ارا\b', 'چرمارا', caption)
    caption = re.sub(r'\bشهر چرم\b', 'شهرچرم', caption)
    caption = re.sub(r'\bچرم نگار\b', 'چرمنگار', caption)
    caption = re.sub(r'\bشیما کفش\b', 'شیماکفش', caption)
    caption = re.sub(r'\bجک اند جونز\b', 'جکاندجونز', caption)
    caption = re.sub(r'\bروبرتو کاوالی\b', 'روبرتوکاوالی', caption)
    caption = re.sub(r'\bسله بن\b', 'سلهبن', caption)
    caption = re.sub(r'\bار ان اس\b', 'اراناس', caption)
    caption = re.sub(r'\bال سی من\b', 'السیمن', caption)
    caption = re.sub(r'\bایران برک\b', 'ایرانبرک', caption)
    caption = re.sub(r'\bال سی وایکیکی\b', 'السیوایکیکی', caption)
    caption = re.sub(r'\bجین وست\b', 'جینوست', caption)
    caption = re.sub(r'\bهیتو استایل\b', 'هیتواستایل', caption)
    caption = re.sub(r'\bویکند اند استارز\b', 'ویکندانداستارز', caption)
    caption = re.sub(r'\bایران نخ باف\b', 'ایراننخباف', caption)
    caption = re.sub(r'\bانار گل\b', 'انارگل', caption)
    caption = re.sub(r'\bایران پاکو\b', 'ایرانپاکو', caption)
    caption = re.sub(r'\bبادی اسپینر\b', 'بادیاسپینر', caption)
    caption = re.sub(r'\bبانی نو\b', 'بانینو', caption)
    caption = re.sub(r'\bپاتن جامه\b', 'پاتنجامه', caption)
    caption = re.sub(r'\bتن درست\b', 'تندرست', caption)
    caption = re.sub(r'\bتن پوش سنتی پارسی\b', 'تنپوشسنتیپارسی', caption)
    caption = re.sub(r'\bتن پوش خاورمیانه\b', 'تنپوشخاورمیانه', caption)
    caption = re.sub(r'\bتن پوش دارکوب\b', 'تنپوشدارکوب', caption)
    caption = re.sub(r'\bتن پوش طوبی آرتمیس\b', 'تنپوشطوبیآرتمیس', caption)
    caption = re.sub(r'\bتن پوش کاردستی\b', 'تنپوشکاردستی', caption)
    caption = re.sub(r'\bتن پوش ماهرو\b', 'تنپوشماهرو', caption)
    caption = re.sub(r'\bتن پوش طبیعی جایدن\b', 'تنپوشطبیعیجایدن', caption)
    caption = re.sub(r'\bتن پوش هـ دو چشم\b', 'تنپوشهـدوچشم', caption)
    caption = re.sub(r'\bجامه پوش آرا\b', 'جامهپوشآرا', caption)
    caption = re.sub(r'\bچرم کاکتوس\b', 'چرمکاکتوس', caption)
    caption = re.sub(r'\bچرم وانیک\b', 'چرموانیک', caption)
    caption = re.sub(r'\bخانه مد راد\b', 'خانهمدراد', caption)
    caption = re.sub(r'\bدنیس تریکو\b', 'دنیس تریکو', caption)
    caption = re.sub(r'\bدست دوست\b', 'دست دوست', caption)
    caption = re.sub(r'\bسیمین دخت\b', 'سیمیندخت', caption)
    caption = re.sub(r'\bکانی راش\b', 'کانیراش', caption)
    caption = re.sub(r'\bکانون تولید ایران\b', 'کانونتولیدایران', caption)
    caption = re.sub(r'\bمیس اسپورت\b', 'میساسپورت', caption)
    caption = re.sub(r'\bنوین چرم\b', 'نوینچرم', caption)
    caption = re.sub(r'\bنون و ر\b', 'نونور', caption)
    caption = re.sub(r'\bهپی لند\b', 'هپیلند', caption)
    caption = re.sub(r'\bسو فیور توگتر\b', 'سوفیورتوگتر', caption)
    caption = re.sub(r'\bاچ اند ام\b', 'اچاندام', caption)
    caption = re.sub(r'\bکوکو شنل\b', 'کوکوشنل', caption)
    caption = re.sub(r'\bتویین لایف\b', 'تویینلایف', caption)
    caption = re.sub(r'\bاسپرینگ فیلد\b', 'اسپرینگفیلد', caption)
    caption = re.sub(r'\bفرویت او د لوم\b', 'فرویتاودلوم', caption)
    caption = re.sub(r'\bبلک لیبری\b', 'بلکلیبری', caption)
    caption = re.sub(r'\bسوجی باگی\b', 'سوجیباگی', caption)
    caption = re.sub(r'\bهوکا وان وان\b', 'هوکاوانان', caption)
    caption = re.sub(r'\bنایکی\b', 'نایک', caption)
    caption = re.sub(r'\ریبوک\b', 'ریباک', caption)
    caption = re.sub(r'\bبچه گانه\b', 'بچگانه', caption)

    caption_arr = re.split('[_ \n,،]+', caption)
    caption_arr = [word[:-2] if word.endswith("ها") else word[:-3] if word.endswith("های") else word for word in
                   caption_arr]
    caption_arr = [word for word in caption_arr if word not in stop_words]
    return caption_arr