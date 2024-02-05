FROM repo.kukala.ir/ai/python:customized

COPY ./requirements.txt ./requirements.txt


RUN echo "[global]\nextra-index-url = https://e.maminejad:d0KgNffMZItoxQ7G@repo.kukala.ir/repository/kukalapythonrepo/simple\ntrusted-host = repo.kukala.ir/repository/kukalapythonrepo" > /etc/pip.conf


RUN pip install -r ./requirements.txt

WORKDIR /app
#
COPY ./ /app/

EXPOSE 80

CMD ["python","app.py"]