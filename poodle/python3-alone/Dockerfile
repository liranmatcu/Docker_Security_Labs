FROM python:3

WORKDIR /usr/src/app

COPY ./code/ ./
# COPY ./python3-alone/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./poodle-poc.py" ]