FROM python:3

WORKDIR /usr/src/app

COPY ./code/ ./
# COPY ./python3-alone/requirements.txt ./
# COPY ./code/parallelization-poodle.py ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./parallelization-poodle.py" ]