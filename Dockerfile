FROM python:3.11.8-bullseye

# Create a directory to store the files
RUN mkdir /code
WORKDIR /code

# Copy the rest of the files
COPY . .

RUN pip install -r requirements.txt

EXPOSE 7860

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
