FROM nginx:latest
ADD . /web
WORKDIR /web
#RUN apt-get Nginx
#CMD ["nginx", "app.py"]

FROM postgres:latest
ADD . /db
WORKDIR /db
#RUN apt-get postgres
CMD ["pg_ctl -D /var/lib/postgresql/data -l logfile start"]
