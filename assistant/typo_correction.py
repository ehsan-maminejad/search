# we are importing our functions
from assistant import word_prediction as wp


def word_suggestion(words,fdist,my_markov):
    """Typo problem correction and word suggestion"""
    try:
        length = len(words.split())

        if length == 1:

            if words:
                predicted_words = wp.word_prediction(words, fdist)
                # print(predicted_words)
                lst = []
                lst1 = []

                for word in predicted_words:
                    suggested_words = my_markov.generate_text(word)
                    # print(suggested_words)
                    if suggested_words:
                        l = len(suggested_words)
                        # print(suggested_words)
                        lst_suggested_words = [f'{word} ' + suggested_words[i][0] for i in range(0, l)]
                        lst += lst_suggested_words
                for bword in lst:
                    t_suggested_words = my_markov.generate_text(bword)
                    if t_suggested_words:
                        l = len(t_suggested_words)
                        # print(suggested_words)
                        t_lst_suggested_words = [f'{bword} ' + t_suggested_words[i][0] for i in range(0, l)]
                        lst1 += t_lst_suggested_words
                if not lst:
                    resp = [500]
                else:
                    resp = predicted_words[:1] + lst[:4] + lst1[:4]
                return resp
            else:
                resp = [500]
                return resp

        elif length == 2:
            lst1 = []
            t_suggested_words = my_markov.generate_text(words)
            if t_suggested_words:
                l = len(t_suggested_words)
                # print(suggested_words)
                t_lst_suggested_words = [f'{words} ' + t_suggested_words[i][0] for i in range(0, l)]
                lst1 += t_lst_suggested_words
            resp = [words] + lst1[:5]
            return resp

        elif length == 3:
            lst = []
            f_suggested_words = my_markov.generate_text(words)
            if f_suggested_words:
                l = len(f_suggested_words)
                # print(suggested_words)
                t_lst_suggested_words = [f'{words} ' + f_suggested_words[i][0] for i in range(0, l)]
                lst += t_lst_suggested_words
            resp = lst[:5]
            return resp

        elif length == 4:
            # lst = []
            # f_suggested_words = my_markov.generate_text(words)
            # if f_suggested_words:
            #     l = len(f_suggested_words)
            #     # print(suggested_words)
            #     t_lst_suggested_words = [f'{words} ' + f_suggested_words[i][0] for i in range(0, l)]
            #     lst += t_lst_suggested_words
            # resp = lst[:5]
            return [words]
        else:
            resp = [500]
            return resp

    except Exception as e:
        print(e)

