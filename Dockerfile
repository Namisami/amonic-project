FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /amonic-project
RUN  pip install --upgrade pip 
COPY requirements.txt /amonic-project/
RUN pip install -r requirements.txt
COPY . /amonic-project/
EXPOSE 8000
RUN touch db.sqlite3
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
