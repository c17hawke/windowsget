from winget import download
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


@pytest.mark.parametrize("URL, filepath", correct_filepaths)
def test_correct_URL_and_filepath(URL, filepath):
    TEST_DIR = "test_dir"
    test_filepath = f"{TEST_DIR}/{filepath}"
    response = download(URL=URL, filepath=Path(test_filepath))
    assert isinstance(response, int)
    assert Path(test_filepath).exists()
    shutil.rmtree(TEST_DIR)


@pytest.mark.parametrize("URL, filepath", bad_filepaths)
def test_bad_URL_and_filepath(URL, filepath):
    with pytest.raises(ValueError):
        response = download(URL=URL, filepath=Path(filepath))

