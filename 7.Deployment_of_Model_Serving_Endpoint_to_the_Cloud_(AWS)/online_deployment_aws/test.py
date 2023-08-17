import boto3
import time
import json

# Initialize a SageMaker runtime client
sagemaker_runtime = boto3.client('sagemaker-runtime')

# Endpoint name
endpoint_name = "classification-deployment-endpoint"

# The example of data point
test_data = ('{"PassengerId": 892, "Pclass": 3, "Name": "Kelly, Mr. James", "Sex": "male", "Age": 34.5, "SibSp": 0, '
           '"Parch": 0, "Ticket": 330911, "Fare": 7.8292, "Cabin": "E46", "Embarked": "Q"}')

start_time = time.time()

# Invoke the SageMaker endpoint
response = sagemaker_runtime.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType='application/json',
    Body=test_data
)

end_time = time.time()

# Calculate the time taken
time_taken = end_time - start_time
# Read the prediction result
result = response['Body'].read().decode()

# Specify the file name
file_name = "result.json"

# Save dictionary as JSON file
with open(file_name, 'w') as file:
    json.dump(result, file, indent=4)  # indent is optional, it just makes the file more readable

print(f"Data saved to {file_name}")
print(f"The request took {round(time_taken, 2)} seconds.")
print(result)
