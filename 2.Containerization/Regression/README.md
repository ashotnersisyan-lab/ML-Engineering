I run these command to create the image of the docker:
```bash
    docker build -t reg_docker:1.0 .
```
After which I run the docker which runs the train.py file 
```bash
    docker run -v "$(pwd)/data:/data" --name reg_docker reg_docker:1.0 
```
