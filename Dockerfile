FROM python:3.11.8-bullseye
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 7860
CMD python app.py --port $PORT

