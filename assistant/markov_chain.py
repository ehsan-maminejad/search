import re
from collections import defaultdict, Counter


class MarkovChain:
    def __init__(self):
        self.lookup_dict = defaultdict(list)

    def add_document(self, caption):
        preprocessed_list = self.preprocess(caption)
        pairs = self.__generate_tuple_keys(preprocessed_list)
        for pair in pairs:
            self.lookup_dict[pair[0]].append(pair[1])
        pairs2 = self.__generate_2tuple_keys(preprocessed_list)
        for pair in pairs2:
            self.lookup_dict[tuple([pair[0], pair[1]])].append(pair[2])
        pairs3 = self.__generate_3tuple_keys(preprocessed_list)
        for pair in pairs3:
            self.lookup_dict[tuple([pair[0], pair[1],
                                    pair[2]])].append(pair[3])

    def preprocess(self, caption):

        words = self.clean_caption(''.join(str(df['Caption'].tolist())))
        return words

    def clean_caption(self, caption):

        with open('persian', encoding='utf-8') as f:
            stop_words = f.read().split()

        caption = re.sub('#(_*[آ-ی0-9]*_*\s*)*', '', caption)
        caption = re.sub('\'', '', caption)
        caption = re.sub('\w*\d\w*', '', caption)
        caption = re.sub(' +', ' ', caption)
        caption = re.sub(r'\n: \'\'.*', '', caption)
        caption = re.sub(r'\n!.*', '', caption)
        caption = re.sub(r'^:\'\'.*', '', caption)
        caption = re.sub(r'\n', ' ', caption)
        caption = re.sub(r'[^\w\s]', ' ', caption)
        caption = re.sub('[^آ-ی_ \n,،]','',caption)

        caption_cleaned = re.split('[_ \n,،]+', caption)
        caption_cleaned = [
            word for word in caption_cleaned if word not in stop_words
        ]
        return caption_cleaned

    def __generate_tuple_keys(self, data):
        if len(data) < 1:
            return

        for i in range(len(data) - 1):
            yield [data[i], data[i + 1]]

    def __generate_2tuple_keys(self, data):
        if len(data) < 2:
            return

        for i in range(len(data) - 2):
            yield [data[i], data[i + 1], data[i + 2]]

    def __generate_3tuple_keys(self, data):
        if len(data) < 3:
            return

        for i in range(len(data) - 3):
            yield [data[i], data[i + 1], data[i + 2], data[i + 3]]

    def oneword(self, string):
        return Counter(self.lookup_dict[string]).most_common()[:3]

    def twowords(self, string):
        suggest = Counter(self.lookup_dict[tuple(string)]).most_common()[:3]
        if len(suggest) == 0:
            return self.oneword(string[-1])
        return suggest

    def threewords(self, string):
        suggest = Counter(self.lookup_dict[tuple(string)]).most_common()[:3]
        if len(suggest) == 0:
            return self.twowords(string[-2:])
        return suggest

    def morewords(self, string):
        return self.threewords(string[-3:])

    def generate_text(self, string):
        if len(self.lookup_dict) > 0:
            tokens = string.split(" ")
            if len(tokens) == 1:
                #print("Next word suggestions:", self.oneword(string))
                ans = self.oneword(string)
            elif len(tokens) == 2:
                #print("Next word suggestions:",self.twowords(string.split(" ")))
                ans = self.twowords(string.split(" "))
            elif len(tokens) == 3:
                #print("Next word suggestions:",self.threewords(string.split(" ")))
                ans = self.threewords(string.split(" "))
            elif len(tokens) > 3:
                #print("Next word suggestions:",self.morewords(string.split(" ")))
                ans = self.morewords(string.split(" "))
        return ans