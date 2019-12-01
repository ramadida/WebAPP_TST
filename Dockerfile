FROM python:3.6.5


WORKDIR .
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
