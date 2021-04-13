FROM python:3.9.4

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

ENV API_ID='1508a9a4840a5574c822d70ca2132032'
ENV API_VERSION='/api/v1'
ENV OPENWEATHER_API_URL='http://api.openweathermap.org/data/2.5/weather'
ENV PROJECT_NAME='WeatherAPI'
ENV REDIS_HOST='redis'
ENV REDIS_PORT='6379'
ENV REDIS_EXPIRATION_TIME='120'
ENV VERSION='0.1'
ENV API_TOKEN='3b719353762f7ddfc080e13556d248e8d8af1a63590b6d17738e4f57ac18a5d1'

CMD ["pytest", "-v"]
