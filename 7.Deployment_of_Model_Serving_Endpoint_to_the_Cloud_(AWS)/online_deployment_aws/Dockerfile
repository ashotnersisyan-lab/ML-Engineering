# The python version
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt to do the package installation
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir

# Install cron
#RUN apt-get update && apt-get -y install cron

#RUN pip install awscli
#RUN --mount=type=secret,id=aws,target=/root/.aws/credentials aws s3 cp s3://demo-classification-model/model-pipeline/

# Add the current directory contents into the container at /app
COPY .. /app

# Copy the cron.txt file and give execution rights
#COPY cron.txt /etc/cron.d/cron-job
#RUN chmod 0644 /etc/cron.d/cron-job
#RUN crontab /etc/cron.d/cron-job

# Run the training script
# RUN python classification/train.py

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the application when the container launches
# CMD ["uvicorn", "prediction:app", "--host", "0.0.0.0", "--port", "8080"]

ENTRYPOINT ["python", "-m", "prediction"]
