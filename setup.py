import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "<REPO_NAME>"
AUTHOR_USER_NAME = "<AUTHOR_USER_NAME>"
PACKAGE_NAME = "<PACKAGE_NAME>"
AUTHOR_EMAIL = "<AUTHOR_EMAIL>"
COMMAND_NAME = "<COMMAND_NAME>"

setuptools.setup(
    name=PACKAGE_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    entry_points={
        "console_scripts": [
            f"{COMMAND_NAME} = {PACKAGE_NAME}.cli:main",
        ]
    }
)
