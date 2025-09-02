FROM python:3.11-slim
WORKDIR /app
COPY data-loader/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY data-loader /app
CMD ["python", "main.py"]
