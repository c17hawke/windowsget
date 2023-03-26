from windowsget import download
import pytest
from pathlib import Path
import shutil




correct_filepaths = [
    ("https://raw.githubusercontent.com/c17hawke/raw_data/main/interactions.csv", "x/y/test.csv"),
    ("https://raw.githubusercontent.com/c17hawke/raw_data/main/interactions.csv", "example.csv"),
] 

bad_filepaths = [
    ("https://raw.githubusercontent.com/c17hawke/raw_data/main/interactions.csv", "x/y/test"),
    ("https://raw.githubusercontent.com/c17hawke/raw_data/main/interactions.csv", "example"),
]


@pytest.mark.parametrize("url, filepath", correct_filepaths)
def test_correct_url_and_filepath(url, filepath):
    TEST_DIR = "test_dir"
    test_filepath = f"{TEST_DIR}/{filepath}"
    response = download(url=url, filepath=Path(test_filepath))
    assert isinstance(response, int)
    assert Path(test_filepath).exists()
    shutil.rmtree(TEST_DIR)


@pytest.mark.parametrize("url, filepath", bad_filepaths)
def test_bad_url_and_filepath(url, filepath):
    TEST_DIR = "test_dir"
    test_filepath = f"{TEST_DIR}/{filepath}"
    with pytest.raises(ValueError):
        response = download(url=url, filepath=Path(test_filepath))
    shutil.rmtree(TEST_DIR)

