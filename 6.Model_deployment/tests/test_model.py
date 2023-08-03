import requests
import json
import time

# The data you want to predict
data = {"PassengerId": 892, "Pclass": 3, "Name": "Kelly, Mr. James",
        "Sex": "male", "Age": 34.5, "SibSp": 0, "Parch": 0,
        "Ticket": 330911, "Fare": 7.8292, "Cabin": "E46", "Embarked": "Q"}

# Convert the data to JSON format
data_json = json.dumps(data)


start_time = time.time()

# Send a POST request to the API endpoint
response = requests.post("http://localhost:8000/predict", data=data_json, headers={"Content-Type": "application/json"})


end_time = time.time()

# Print the prediction and the time it took
print(f"The request took {end_time - start_time} seconds.")
print(response.text)
