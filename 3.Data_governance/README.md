I have used as remote repository a folder in my Google Drive.
To set it up I created a Google Cloud Platform account. 
In the GCP I created a service account and enabled the GDrive API.
I downloaded the credentials of the service account in json format.
Finally, I shared editors access of the remote folder to the service account.
To set up GDrive as the DVC remote, I run the following commands.

Please first install dvc and dvc_gdrive:
```bash
    pip install dvc
    pip install dvc_gdrive
```
Initialize a dvc project by using the following command:
```bash
    dvc init
```
Add to the dvc the csv files that you want to push to remote(example):
```bash
    dvc add 3.Data_governance/Pipeline1/data/iris.csv 
```
Then, run the suggested commands(example):
```bash
    git add 3.Data_governance/Pipeline1/data/.gitignore 3.Data_governance/Pipeline1/data/iris.csv.dvc
```
Finally, push the data to the remote repository:
```bash
    dvc push
```
Change the directory to the pipeline folder that you want to use(example):
```bash
    cd 3.Data_governance/Pipeline1
```
Run the repro command to run the dvc pipeline:
```bash
    dvc repro
```
Run the following command to see the resulting metrics of the ml pipelines:
```bash
    dvc metrics show
```
