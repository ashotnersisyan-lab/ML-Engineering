# The python version
FROM python:3.10

ADD . .
# ADD train.py .
# ADD requirements.txt .

# Install production dependencies.
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python ./train.py
