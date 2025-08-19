FROM python
COPY requirement.txt .
RUN pip install -r requirement.txt
COPY  ./web/static /home/myapp/static/
COPY  ./web/templates /home/myapp/templates/
COPY  ./web/app.py /home/myapp/
EXPOSE 5050
CMD python /home/myapp/app.py