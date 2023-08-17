# Deployment of pretrained model on AWS
Here I will deploy the model from previous homework 6.Model_deployment on the AWS using Sagemaker, 
I will also use services S3 and ECR(Elastic Container Registry).


## AWS creation of an IAM role and authentication of the device
First I create an IAM role that will be responsible for the deployment.
Later I created the Access key that was used to authenticate the device and be able to use the aws cli.

Install the aws cli following the official guide: [Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

After installation configure your keys to be able to access aws services using command lines on your device.

```bash
aws configure
AWS Access Key ID [None]: accesskey  # You should get this key on AWS side
AWS Secret Access Key [None]: secretkey  # You should get this key on AWS side
Default region name [None]: us-east-1
Default output format [None]: json
```


## Model training and saving on the cloud
First I trained the model using the training script from previous 
homework(will not go much in details as it was already covered).

After getting the pipeline.pkl I saved it in the classification/model/ directory.
To be able to use the model later in Sagemaker we need to zip it into a tar.gz file.
for that I have writen the script change_the_format.py, to run the script
please change the directory to the classification/model/ and run the following command:

```bash
python -m change_the_format
```

As a result we will get the pipeline.tar.gz file. Now we create a bucket in S3 service and upload 
the file into that bucket. Later we will use it to unpack the model pipeline into the working image.


## Upload your image for serving the model to ECR

In this step we will upload the image to the ECR.
\
Please change the directory to the online_deployment_aws and run the following commands:

Login to AWS ECR:
```bash
docker login -u AWS -p $(aws ecr get-login-password --region us-east-1) 178781415093.dkr.ecr.us-east-1.amazonaws.com
```
Build the image that you are going to use:
```bash
docker build -t demo-classification-deployment .
```
Tag the image:
```bash
docker tag demo-classification-deployment:latest 178781415093.dkr.ecr.us-east-1.amazonaws.com/demo-classification-deployment:latest
```
Push the docker image to the ECR:
```bash
docker push 178781415093.dkr.ecr.us-east-1.amazonaws.com/demo-classification-deployment:latest
```
You can see your image uploaded in the Amazon Elastic Container Registry under the Repositories.

## Create a Sagemaker model and start an endpoint

To create a Sagemaker model and start an endpoint I have used the AWS Console (UI).


Step 1: Setup and Pre-requisites

Make sure you have the necessary IAM roles set up for Amazon SageMaker, Amazon S3, and Amazon ECR.
\
Ensure you have a model artifact stored in an S3 bucket.
\
Ensure you have a Docker image for inference stored in Amazon ECR.

Step 2: Open Amazon SageMaker in AWS Console

Log in to the AWS Management Console.
\
Navigate to the SageMaker service.

Step 3: Create a Model

In the SageMaker dashboard, under the Inference section on the left panel, click on Models.
\
Click on Create model.
\
In the Model name field, provide a unique name for your model.
\
For the IAM role, either choose an existing role or create a new role. Ensure that the role 
has the necessary permissions for SageMaker, S3, and ECR.
\
Under the Container definition section:
\
Choose the Provide model artifacts and inference image location option.
\
In the Location of inference code image, enter the ECR URI of your Docker image.
\
In the Location of model artifacts, enter the S3 path where your model artifact resides.
\
After filling in all details, click on Create.

Step 4: Create an Endpoint Configuration

On the left panel, under the Inference section, click on Endpoint configurations.
\
Click on Create endpoint configuration.
\
Provide a name for the endpoint configuration.
\
Under the Production variants section:
\
Click on Add model.

Select the model you created in Step 3.

Provide a name for the variant, select the desired instance type, and set the initial instance count.
\
Click on Create endpoint configuration.

Step 5: Create and Deploy an Endpoint

On the left panel, under the Inference section, click on Endpoints.
\
Click on Create endpoint.
\
Provide a name for the endpoint.
\
Select the endpoint configuration you created in Step 4 from the drop-down list.
\
Click on Create endpoint.
\
After a few minutes, AWS SageMaker will deploy the model and the status of the endpoint will change from Creating to InService. Once it's InService, you can use the endpoint to make real-time predictions using your model.



## Test the results

To test the endpoint please change the directory to the online_deployment_aws and run the following command:

```bash
python -m test
```

You will see this lines printed and the result saved to result.json file.

```bash
Data saved to result.json
The request took 0.71 seconds.
{"Survived":0}
```
