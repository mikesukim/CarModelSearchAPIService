FROM python:3.8-slim-buster

WORKDIR /cymatrix_challenge

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN pytest
CMD [ "python3", "-m" , "flask", "--app", "src/app","run", "--host=0.0.0.0", "--port=8000"]