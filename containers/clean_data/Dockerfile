FROM python:3.10
WORKDIR /app
COPY clean.py .
COPY input.json .
RUN pip install --no-cache-dir
CMD ["python", "clean.py"]
