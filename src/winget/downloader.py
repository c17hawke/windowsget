import requests
from pathlib import Path
from winget.logger import logger
import os

def download(URL: str, filepath: Path) -> int:
    """
    Download a file from the specified URL and save it to the specified filepath.

    Args:
        URL (str): The URL of the file to download.
        filepath (Path): The file path where to save the downloaded file. 
        
    Returns:
        int: The number of bytes downloaded.

    Raises:
        HTTPError: If the HTTP status code is not 200 (OK).
    """
    response = requests.get(URL)

    # Check if the HTTP status code is OK (200)
    if response.status_code == 200:
        # Create the parent directory of the file if it does not exist
        filepath.parent.mkdir(exist_ok=True, parents=True)

        filename, extension = os.path.splitext(filepath)
        if extension == "":
            logger.exception(f"ValuError: The file extension must be provided!")
            raise ValueError("The file extension must be provided!")
        
        # Write the contents of the response to the file
        with open(filepath, 'wb') as f:
            bytes_downloaded = f.write(response.content)

        # Return the number of bytes downloaded
        return bytes_downloaded
    else:
        logger.warning(f"status code: {response.status_code}, raising exception")
        # Raise an HTTPError if the status code is not OK
        response.raise_for_status()
        return 0
