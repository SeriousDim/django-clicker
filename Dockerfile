FROM python:3.7
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN pip install -r requirements.txt

EXPOSE 8000

# to run in browser, type localhost instead 127.0.0.1 or 0.0.0.0
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
