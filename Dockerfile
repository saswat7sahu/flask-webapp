FROM  python:3.9.19-alpine
WORKDIR /app
COPY . /app/
RUN pip install -r recuirments.txt
EXPOSE 3000
CMD [ "python" "./app.py" ]