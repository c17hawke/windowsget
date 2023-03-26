# python cli template

Documentation: `https://c17hawke.github.io/<repo-name>/<add project board link if any>`

## STEPS -

### STEP 01: Create new repository using this template

by choosing this as a project template while creating a new repository

### STEP 02: Clone the new repository or use codespaces

- To clone you can use the following command -

    ```bash
    git clone https://github.com/c17hawke/<repo-name>
    ```

> NOTE: update the repo-name here

- Click on create code spaces or select available codespaces.

### STEP 03: IMPORTANT: Create `.env` file in the root of the project and paste the following content -

```ini
# update the following values as per your project
PROJECT_NAME=<PROJECT_NAME>
REPO_NAME=<REPO_NAME>
AUTHOR_USER_NAME=<AUTHOR_USER_NAME>
AUTHOR_NAME=<AUTHOR_NAME>
PACKAGE_NAME=<PACKAGE_NAME>
AUTHOR_EMAIL=<AUTHOR_EMAIL>
COMMAND_NAME=${PACKAGE_NAME} # update as per your need, Here it is assumed that command name is package name
SITE_AUTHOR=${AUTHOR_USER_NAME} # update as per your need, Here it is assumed that site author is author user name
GITHUB_USER_NAME=${AUTHOR_USER_NAME} # update as per your need, Here it is assumed that github user name is author user name
PYTHON_VERSION=<PYTHON_VERSION>  
YEAR=<YEAR>
```

> **WARNING: if this step is skipped then exception will be raised**

### STEP 04: Run the template.py file

> NOTE: make sure you have dotenv installed before running the following command. To install it simply run the following command -

```bash
pip install python-dotenv
```

use template.py to create the other required files by running the following command -

```bash
python template.py
```

### STEP 05: Add a `LICENSE` file

- Go to your github repository and click on `Add file` and then select `Create new file`.
- Now start typing the name of the file as `LICENSE` and then you'll see the option of selecting the desired template.

NOTE: You can choose MIT License if you are not sure.

> This completes the basic skeleton of the project!!

### STEP 06: Create and install dependencies -

- It is assumed that `anaconda` or `miniconda` is intalled in the system. If not then please do your setup by following this tutorial - [How to do the basic setup for any python, ML, DL, projects on windows10 or 11?](https://youtu.be/bVM-QujJ0AI)

- Update the `requirements_dev.txt` and `requirements.txt` files with the project requirements (i.e. required libraries)
- Now run the `init_setup.sh` file by running the following command -

    ```bash
    bash init_setup.sh   
    ```

NOTE: if in case you face difficulty in running the init_setup.sh file then you can run the command mentioned in it one by one in the terminal to get the same result.

> This completes the environment setup of the project!!

### STEP 07: Now you can start the development by activating the environment

- To activate the environment run the following command -

    ```bash
    conda activate ./env
    ```

### Create Dockerfile for running tox test locally -

- Create a Dockerfile in your project directory with the following contents:

    ```Dockerfile
    FROM python:3.8

    # Install necessary packages
    RUN apt-get update && \
        apt-get install -y git && \
        pip install tox

    # Set working directory
    WORKDIR /app

    # Copy the project files into the container
    COPY . /app

    # Run tox
    CMD ["tox"]
    ```

- Build the Docker image by running the following command in your project directory:

```bash
docker build -t myproject .
```

- Run tox inside a container using the Docker image by running the following command:

```bash
docker run -it --rm myproject
```

> NOTE: The above two commands should be executed again if you update the code.

- If you want to persist data between container runs (such as test results or code coverage reports), you can use Docker volumes to mount directories inside the container to directories on your local machine. For example:

```bash
docker run -it --rm -v $(pwd)/results:/app/results myproject
```

> This will mount the results directory inside the container to a directory named results in your current working directory on the host machine, allowing you to save test results or other data outside the container.
