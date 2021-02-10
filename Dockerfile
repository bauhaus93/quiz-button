FROM python:3.9

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN flask db upgrade && python create_tables.py
CMD ["./run_gunicorn.sh"]
