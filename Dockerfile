FROM python:3.10-slim

WORKDIR /app

COPY sample_api.py .

RUN pip install flask

EXPOSE 5000

CMD ["python", "sample_api.py"]
