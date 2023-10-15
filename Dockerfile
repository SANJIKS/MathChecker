FROM python:3.10 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

COPY . .

RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput


CMD [ "python", "manage.py migrate" ]