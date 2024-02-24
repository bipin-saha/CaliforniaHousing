FROM python:3.11.8-bullseye

COPY . /code
ADD https://github.com/bipin-saha/Visual-Questing-Answering/blob/main/compressed_forest.pkl.gz /code/compressed_forest.pkl.gz

WORKDIR /code

# Change permissions explicitly
RUN chmod u+rw compressed_forest.pkl.gz \
    && ls -l  # Print out directory listing to debug permission settings

RUN pip install -r requirements.txt

EXPOSE 7860

CMD python app.py --port $PORT
