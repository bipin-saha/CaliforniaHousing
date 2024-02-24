FROM python:3.11.8-bullseye
COPY . /code
WORKDIR /code
RUN pip install requirements.txt
EXPOSE 7860
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
