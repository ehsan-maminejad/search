from fastapi import FastAPI, HTTPException
from etl.load import tags_extractor
from typing import Optional
from utils import logger
import os
import sys
import copy

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_path)
app = FastAPI()


@app.get("/get_tags")
def get_category(phrase: Optional[str] = None):
    try:
        if phrase is None:
            raise HTTPException(status_code=400, detail="No phrase provided")

        data = tags_extractor(phrase)
        if data:
            if data['query']:
                log_data = copy.copy(data)
                log_data['status_code'] = 200
                log_data['phrase'] = phrase
                logger.run(log_data)
            return data
        elif all(isinstance(value, list) and not value for value in data.values()):
            data = {'status_code': 404, 'phrase': phrase}
            logger.run(data)
            raise HTTPException(status_code=404, detail="عبارت صحیحی جستجو نشده است.")
        else:
            data = {'status_code': 500, 'phrase': phrase}
            logger.run(data)
            raise HTTPException(status_code=500, detail="عبارت صحیحی جستجو نشده است.")
    except Exception as e:
        d = {'status_code': 500, 'error': str(e), 'phrase': phrase}
        logger.run(d)
        raise HTTPException(status_code=500, detail=f"عبارت صحیحی جستجو نشده است. Error: {str(e)}")


if __name__ == '__main__':
    app.run("0.0.0.0", port=80, debug=True)
