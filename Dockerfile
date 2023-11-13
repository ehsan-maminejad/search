# Use the Python 3.9 image
FROM repo.kukala.ir/ai/python:customized

# Set the working directory to /Ezshop/get_category_id
WORKDIR /Ezshop/get_query_catid

# Copy the current directory contents into the container at /Ezshop 
COPY requirements.txt requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0


#Pip command without proxy setting
RUN pip install -r requirements.txt

# Expose port 4030
EXPOSE 80

COPY . .

CMD ["python","app.py","flask"]