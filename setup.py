import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.7"

REPO_NAME = "windowsget"
AUTHOR_USER_NAME = "c17hawke"
PACKAGE_NAME = "windowsget"
AUTHOR_EMAIL = "sunny.c17hawke@gmail.com"
COMMAND_NAME = "windowsget"

setuptools.setup(
    name=PACKAGE_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="windowsget is a Python-based command-line interface (CLI) utility that can be used to download files from the internet on Windows operating system.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        "Documentation": f"https://{AUTHOR_USER_NAME}.github.io/{REPO_NAME}/",
        "Homepage": f"https://{AUTHOR_USER_NAME}.github.io/{REPO_NAME}/",
        "Source": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    entry_points={
        "console_scripts": [
            f"{COMMAND_NAME} = {PACKAGE_NAME}.cli:main",
        ]
    }
)
