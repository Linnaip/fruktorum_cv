FROM python:3.11.4-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .
CMD ["gunicorn", "savelink.wsgi:application", "--bind", "0:8000" ]