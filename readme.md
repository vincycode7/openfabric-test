# AI Junior Developer (Intern) Test 
Welcome! and thank you for applying! 
## Instruction Manual:

This program can be run in two ways - using Docker or running the Python script.

### Running with Docker:

1. Install Docker on your machine if not already installed.

2. Clone or download the repository to your local machine.

3. Open a terminal and navigate to the root directory of the project.

4. Run the following command to build the Docker container:

    `docker build -t openfabric-intern:1.0 .`

5. Once the build process is complete, start the container in detach mode using the following command:

    `docker run -d -p 5000:5000 openfabric-intern:1.0`

6. To stop and remove the running container, run 
    `docker ps` 
    then pick the <container-id> of the running container
    
7. Run docker stop <container-id> && docker rm <containerid>

This will start the server and you can access the API endpoint by visiting http://localhost:5000 in your web browser or running queries via tools like Postman.

Running with Python:

1. Install Python 3 on your machine if not already installed.

2. Clone or download the repository to your local machine.

3. Open a terminal and navigate to the root directory of the project.

3. Run the following command to install the required Python packages:

    `pip install -r requirements.txt`

4. Once the installation is complete, start the server by running the following command:

    `./start.sh` or `python ignite.py`

This will start the server and you can access the API endpoint by visiting http://localhost:5000 in your web browser or running queries via tools like Postman.


## Requirement
The current project has the blueprint structure of an AI App. 

Your mission is to implement an 💬NLP chatbot **answering questions about science**. 

You will add your logic to the `main.py` file inside the `execute` function. 
```python
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for text in request.text:        
        response = '' # <<< --Your magic goes here
        output.append(response)

    return SimpleText(dict(text=output))
```
## Constraints and restrictions
You are free to use any package or library you see feet as long as you follow these rules:
* 👎 You can't call any external service (e.g. chatGPT) 
* 👎 You can't copy and paste from other peoples work 

## Run
The application can be executed in two different ways:
* locally by running the `start.sh` 
* on in a docker container using `Dockerfile` 

## Submission
Your solution must be uploaded on GitHub, and submit us the link in **max 1 week** after receiving the task.

## Note
Keep in mind that this is the project that will be used to evaluate your skills.
So we do expect you to make sure that the app is fully functional and doesn't have any obvious missing pieces.