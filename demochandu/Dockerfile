FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev mariadb-connector-c-dev

WORKDIR /django
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt -v
COPY . .
RUN python manage.py migrate
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin1', 'admin1@example.com', 'admin1')" | python manage.py shell
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
