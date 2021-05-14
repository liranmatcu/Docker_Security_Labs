FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY parallelization-poodle.py ./

COPY . .

CMD [ "python", "./parallelization-poodle.py" ]