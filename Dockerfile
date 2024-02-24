FROM 3.11.8-slim-bullseye
COPY . /code
WORKDIR /code
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
EXPOSE 7860
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
