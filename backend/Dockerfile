# init a base image
FROM python:3.7.10-slim

RUN mkdir /backend

COPY requirements.txt /backend

WORKDIR /backend

RUN pip install -r requirements.txt

COPY . /backend

#This command is just informative since it does not actually expose any port
EXPOSE $BACKEND_DOCKER_PORT

#CMD ["python","main.py"] #This is a development server. Do not use it in a production k8s_deployment.
#ENTRYPOINT gunicorn --bind 0.0.0.0:$BACKEND_HOST_PORT main:app
#ENTRYPOINT ["sh", "-c","gunicorn --bind 0.0.0.0:$BACKEND_HOST_PORT main:app"]
#RUN python create_app.py db upgrade
#ENTRYPOINT ["bash", "-c","gunicorn --bind 0.0.0.0:$BACKEND_HOST_PORT main:app"]
ENV FLASK_APP "create_app.py"
RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]