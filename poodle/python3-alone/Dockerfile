FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ../code/parallelization-poodle.py ./

COPY ../code/ ./

CMD [ "python", "./parallelization-poodle.py" ]