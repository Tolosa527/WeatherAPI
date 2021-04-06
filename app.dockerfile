FROM python:3.8

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8080"]