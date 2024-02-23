FROM python:3.12-alpine

WORKDIR /backend

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python3 backend/manage.py makemigrations

RUN python3 backend/manage.py migrate

CMD ["python3", "manage.py", "runserver", "0000:8000"]
