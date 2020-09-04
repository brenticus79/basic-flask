FROM python:alpine3.12
COPY app.py /app/app.py
WORKDIR  /app
RUN pip install flask
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
