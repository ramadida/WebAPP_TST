FROM python:3.6.5


RUN apt-get update -y && \
    apt-get install -y python-pip python-dev



WORKDIR /main
WORKDIR /bioskop_api


RUN pip install certifi
RUN pip install chardet
RUN pip install Click
RUN pip install Flask
RUN pip install idna
RUN pip install itsdangerous
RUN pip install Jinja2
RUN pip install MarkupSafe
RUN pip install oauthlib
RUN pip install PySocks
RUN pip install requests
RUN pip install requests-oauthlib
RUN pip install six
RUN pip install tmdbv3api
RUN pip install tweepy
RUN pip install urllib3
RUN pip install werkzeug

COPY . /main
COPY . /bioskop_api

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
CMD [ "bioskop_api.py" ]
