### Docker Compose Construction
I created two dockerfiles for two images to later use two containers. 
One for the MlFlow Server and one for the python training.
Their work is dictated by the docker-compose.yml file that is in this directory

Run this command in the current directory to run the docker-compose file:
```bash
    docker-compose up
```

It will run both containers and perform the training of the ML models. 
The results can be observed in the MlFlow UI.

### Details of the ML training model.
The training is based on the titanic dataset from Kaggle.

In this branch I only used the best model and feature combination that I found in the main branch. 
It will be Catboost optimized with hyperopt based on regular encoded feature without the engineered new feature.
The hyperparameters may differ as I hyperopt has a stochastic component in its searching algorithm.
