FROM python:3.8.7-slim-buster

COPY . /app
WORKDIR /app
ENV PYTHONPATH=/app
ENV PYTHONBUFFERED=1

RUN pip install pip==21.2.4 && \
    pip install pip --upgrade && \
    pip install -r requirements.txt

CMD ["python", "main.py"]