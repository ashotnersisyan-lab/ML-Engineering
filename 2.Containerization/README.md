In this homework I created a docker file to create an image that would run the python project. 
I took the machine learning solution from my homeworks and turned a Google colab into a python file.

Improvements:
I removed the print statement that were not needed and left the results only. 
To make the docker image lighter I changed some of the dependencies and left out verstack==3.7.1, ydata_profiling==4.2.0.
Inside the dockerfile I added creation of user.
I added a .dockerignore file that would specify to leave out the data from the docker image.
The data is accessed in the run command of the docker mentioned in the readme file.
I also specified the version in the docker build command.
