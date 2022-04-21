FROM python:3.9-bullseye

WORKDIR /app

RUN mkdir /app/downloads

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY . .

CMD [ "python","main.py" ]
