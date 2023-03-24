import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format= "[%(asctime)s: %(levelname)s]: %(message)s"
    )

# update the following values as per your project other wise it will take the given default - 
PROJECT_NAME = os.getenv("PROJECT_NAME")
REPO_NAME = os.getenv("REPO_NAME")
AUTHOR_USER_NAME = os.getenv("AUTHOR_USER_NAME")
AUTHOR_NAME = os.getenv("AUTHOR_NAME")
PACKAGE_NAME = os.getenv("PACKAGE_NAME")
AUTHOR_EMAIL = os.getenv("AUTHOR_EMAIL")
COMMAND_NAME = os.getenv("COMMAND_NAME")
SITE_AUTHOR = os.getenv("SITE_AUTHOR")
GITHUB_USER_NAME = os.getenv("GITHUB_USER_NAME")
PYTHON_VERSION = os.getenv("PYTHON_VERSION")
YEAR = os.getenv("YEAR")

if not all([PROJECT_NAME, REPO_NAME, AUTHOR_USER_NAME, PACKAGE_NAME, AUTHOR_EMAIL, COMMAND_NAME, SITE_AUTHOR]):
    raise Exception("One or more environment variables are not set")


logging.info(f"Creating project by name: {PROJECT_NAME}")

# list of files:
list_of_files = [
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/cli.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    f"research/trial_001.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file: {filename} at path: {filepath}")
    else:
        logging.info(f"file is already present at: {filepath}")

class UpdateContent:
    def __init__(self, path: str, **kwargs):
        self.path = path
        self.kwargs = kwargs

    def read_content(self):
        with open(self.path, "r") as f:
            self.content = f.read()
        if self.content!= "":
            logging.info(f"content read succesfully from: {self.path}")

    def update_content(self):
        if self.content!= "":
            for key, value in self.kwargs.items():
                self.content = self.content.replace(f"<{key}>", value)
            logging.info(f"content replaced succesfully!")

    def write_content(self):
        if self.content != "":
            with open(self.path, "w") as f:
                f.write(self.content)
            logging.info(f"content updated succesfully and written to: {self.path}")

path_and_kwargs = {
    "setup.py":{
    "REPO_NAME": REPO_NAME,
    "AUTHOR_USER_NAME": AUTHOR_USER_NAME,
    "PACKAGE_NAME": PACKAGE_NAME,
    "AUTHOR_EMAIL": AUTHOR_EMAIL,
    "COMMAND_NAME": COMMAND_NAME
    },
    
    "mkdocs.yml": {
    "PACKAGE_NAME": PACKAGE_NAME, 
    "SITE_AUTHOR": SITE_AUTHOR,
    "GITHUB_USER_NAME": GITHUB_USER_NAME,
    "YEAR": YEAR,
    "REPO_NAME": REPO_NAME,
    "AUTHOR_NAME": AUTHOR_NAME
    },
    
    "setup.cfg": {
    "PACKAGE_NAME": PACKAGE_NAME
    },

    "init_setup.sh": {
    "PYTHON_VERSION": PYTHON_VERSION
    } 
    }

for path, kwargs in path_and_kwargs.items():
    update_content = UpdateContent(path=Path(path), **kwargs)
    update_content.read_content()
    update_content.update_content()
    update_content.write_content()
