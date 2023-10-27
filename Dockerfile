FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /amonic-project
COPY . .
RUN  pip install --upgrade pip \ 
    pip install -r requirements.txt
EXPOSE 8000
RUN ["chmod", "+x", "docker-entrypoint.sh"]
ENTRYPOINT [ "./docker-entrypoint.sh" ]