## Running Commands
I run these command to create the image of the docker:
```bash
    docker build -t deployment:1.0 . --network=host
```
After which I run the docker which runs online prediction model based on fast api
```bash
    docker run -p 8000:80 deployment:1.0
```

## Package Description

Here is a solution to the Titanic Kaggle problem 
and serving the ML pipeline as a backend server to give online and batch predictions.

When the docker is built the train.py script runs and creates a training pipeline. 
The pipeline is saved at the classification/model/ as a pkl file saving the 
artifacts of the model and preprocessing steps. 
Later the pipeline.pkl file is used to predict the new results based on incoming data points.
The same artifacts are used both for online and batch predictions.

### Online prediction

For the online prediction serving I have used Fast API. 
The server receives a request with a json file that includes the data 
for which the prediction is generated and sent as a response.

After running the docker you can send the request 
to the "http://localhost:8000/predict" url and start using the service.

I have included a small python code that sends an example request 
to the server and prints the results and the time it took to respond.
After running the docker you can just run the tests/test_model.py script 
and check the results.

### Batch prediction

For batch prediction I wrote the script batch_prediction.py. 
It takes the test.csv from the data directory and predicts the target value for the whole batch.
The results are saved as another csv file in the data directory named predictions.csv
For automatic triggering the script I wrote a small cron.txt file that runs the script every day 
on a specific time. Depending on a specific need we can change the time. The docker image automatically 
runs the cron.txt file when building the image.

### Building as Package

To build the service as a package I followed the official guidelines and created a package at TestPyPi.
You can find the package under the link: https://test.pypi.org/project/titanic-prediction-model/0.0.1/
