from flask import Flask, jsonify, request
import os
import sys
from etl.load import tags_extractor

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_path)
app = Flask(__name__)


@app.route('/get_tags')
def get_category():
    try:
        phrase = request.args.get('phrase')
        data = tags_extractor(phrase)
        if data:
            resp = jsonify(data)
            resp.status_code = 200
            return resp
        else:
            resp = jsonify(message=f"عبارت صحیحی جستجو نشده است.")
            resp.status_code = 500
            return resp
    #todo: add log to catch and analysis errors
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run("0.0.0.0", port=80, debug=True)
