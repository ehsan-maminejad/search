# Use the Python 3.9 image
FROM repo.kukala.ir/ai/python:customized


# Add the trusted host to the pip configuration
RUN mkdir -p /etc/pip && echo "[global]\nextra-index-url=https://repo.kukala.ir/repository/kukalapythonrepo/" > /etc/pip/pip.conf
# Set the working directory to /Ezshop/get_category_id
COPY ./requirements.txt ./requirements.txt

#Pip command without proxy setting
RUN pip install -r ./requirements.txt

WORKDIR /app
#
COPY ./ /app/

EXPOSE 80

CMD ["python","app.py"]