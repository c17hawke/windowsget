"""
Downloader module
"""
import os
from pathlib import Path
import requests
from windowsget.logger import logger


def download(url: str, filepath: Path) -> int:
    """
    Download a file from the specified url and save it to the specified filepath.

    Args:
        url (str): The url of the file to download.
        filepath (Path): The file path where to save the downloaded file.

    Returns:
        int: The number of bytes downloaded.

    Raises:
        HTTPError: If the HTTP status code is not 200 (OK).
    """
    response = requests.get(url, timeout=2)

    # Check if the HTTP status code is OK (200)
    if response.status_code == 200:
        # Create the parent directory of the file if it does not exist
        filepath.parent.mkdir(exist_ok=True, parents=True)

        _, extension = os.path.splitext(filepath)
        if extension == "":
            logger.exception("ValuError: The file extension must be provided!")
            raise ValueError("The file extension must be provided!")

        # Write the contents of the response to the file
        with open(filepath, 'wb') as file_handler:
            bytes_downloaded = file_handler.write(response.content)

        # Return the number of bytes downloaded
        return bytes_downloaded
    logger.warning(f"status code: {response.status_code}, raising exception")
    # Raise an HTTPError if the status code is not OK
    response.raise_for_status()
    return 0
