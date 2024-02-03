# Use the Python 3.9 image
FROM repo.kukala.ir/ai/python:customized

# Set the working directory to /Ezshop/get_category_id
COPY ./requirements.txt ./requirements.txt

#Pip command without proxy setting
RUN pip install -r ./requirements.txt

WORKDIR /app
#
COPY ./ /app/

EXPOSE 80

CMD ["python","app.py"]