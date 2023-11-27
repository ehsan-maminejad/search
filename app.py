# we are importing our functions
from flask import Flask, jsonify, request
import pandas as pd
import json
import pickle
import get_query_catid as gc
from tags import tags_extractor

# from assistant import typo_correction as tc
# from assistant.markov_chain import MarkovChain

# from get_fcat import get_category_father as gf

# with open('assistant/fdist20', 'r', encoding='utf8') as f:
#     fdist = json.load(f)


df = pd.read_csv('./components/Category.csv')

app = Flask(__name__)


@app.route('/get_tags')
def get_category():
    """Get Category id
    Based on the given phrase this function returns category id of the phrase
    and if nonsense is searched, returns "عبارت صحیحی جستجو نشده است"
    """
    try:
        word = request.args.get('phrase')
        remaining, category = gc.get_other_categories(word, df)
        if category:
            data = tags_extractor(word, remaining)
            data['categories'] = category
            if category[0] in [1, 2, 3, 4, 5, 632] and not remaining:
                x = list(df[df["CategoryId"] == category[0]].Id)
                l1 = []
                for i in range(len(x)):
                    l1.append(df[[df["CategoryId"] == i for i in x][i]].Id)
                l2 = []
                for something in l1:
                    for s in something:
                        if not (df[df["CategoryId"] == s].Id.empty):
                            for _a, _b in (list(df[df["CategoryId"] == s].Id.items())):
                                l2.append(_b)
                        else:
                            l2.append(s)
                data['categories'] = l2
                # resp = jsonify(id=l2, query=remaining,
                #                message=f"Category id of {word} is {l2} and remain phrase is {remaining} !")
                resp = data
                resp.status_code = 200
                return resp
            elif category[0] in [1, 2, 3, 4, 5, 632] and remaining:
                # resp = jsonify(id=[], query=word,
                #                message=f"Category id of {word} is {[]} and remain phrase is {word} !")
                resp = jsonify(data)
                resp.status_code = 200
                return resp

            elif category and category[0] not in [6]:
                # resp = jsonify(data, query=remaining,
                #                message=f"Category id of {word} is {category} and remain phrase is {remaining} !")
                resp = jsonify(data)
                resp.status_code = 200
                return resp
            else:
                resp = jsonify(message=f"عبارت صحیحی جستجو نشده است.")
                resp.status_code = 500
                return resp

        elif remaining:
            data = tags_extractor(word, remaining)
            data['categories'] = []
            # resp = jsonify(id=[], query=word,
            #                message=f"Category id of {word} is {[]} and remain phrase is {word} !")
            resp = jsonify(data)
            resp.status_code = 200
            return resp

    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run("0.0.0.0", port=80, debug=True)
