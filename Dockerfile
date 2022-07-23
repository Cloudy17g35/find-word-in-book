FROM python:3.8

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN [ "python3", "-c", "import nltk; nltk.download('stopwords', download_dir='/usr/local/nltk_data')" ]

COPY . .

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]