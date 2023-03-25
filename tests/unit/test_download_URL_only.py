from windowsget import download
import pytest
from pathlib import Path
from requests.exceptions import HTTPError
import os

correct_URLs = [
    "https://raw.githubusercontent.com/c17hawke/raw_data/main/interactions.csv"
] 

bad_URLs = [
    "https://raw.githubusercontent.com/c17hawke/raw_data/main/interactions",
    "https://raw.githubusercontent.com/c17hawke/raw_data/main/xyz"
]

@pytest.mark.parametrize("URL", correct_URLs)
def test_correct_URLs_only(URL):
    filepath = Path(URL).name
    response = download(URL=URL, filepath=Path(filepath))
    assert isinstance(response, int)
    os.remove(Path(filepath))

@pytest.mark.parametrize("URL", bad_URLs)
def test_bad_URLs_only(URL):
    filepath = Path(URL).name
    with pytest.raises(HTTPError):
        response = download(URL=URL, filepath=Path(filepath))
