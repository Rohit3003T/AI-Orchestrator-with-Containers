FROM python:3.10
WORKDIR /app
COPY sentiment.py .
COPY input.json .
RUN pip install textblob
CMD ["python", "sentiment.py"]
