# init a base image
FROM python:3.7.10-slim

RUN mkdir /frontend

COPY requirements.txt /frontend

WORKDIR /frontend

RUN pip install -r requirements.txt

COPY . /frontend

#This command is just informative, since it does not actually expose any port
EXPOSE $FRONTEND_PORT

#CMD ["python","main.py"] #This is a development server. Do not use it in a production k8s_deployment.
CMD gunicorn --bind 0.0.0.0:$FRONTEND_PORT main:app

