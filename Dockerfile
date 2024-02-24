FROM python:3.11.8-bullseye

# Create a directory to store the file
RUN mkdir /code
WORKDIR /code

# Download the file separately
RUN wget https://github.com/bipin-saha/Visual-Questing-Answering/raw/main/compressed_forest.pkl.gz

# Change permissions explicitly
RUN chmod u+rw compressed_forest.pkl.gz \
    && ls -l  # Print out directory listing to debug permission settings

# Copy the rest of the files
COPY . .

RUN pip install -r requirements.txt

EXPOSE 7860

CMD python app.py --port $PORT
