FROM python:3.11.8-bullseye

# Create a directory to store the files
RUN mkdir /code
WORKDIR /code

# Download the compressed file separately
RUN wget https://github.com/bipin-saha/Visual-Questing-Answering/raw/main/compressed_forest.pkl.gz

# Change permissions explicitly for both input and output files
RUN chmod u+rw compressed_forest.pkl.gz \
    && touch uncompressed_forest.pkl \
    && chmod u+rw uncompressed_forest.pkl \
    && ls -l  # Print out directory listing to debug permission settings

# Copy the rest of the files
COPY . .

RUN pip install -r requirements.txt

EXPOSE 7860

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
