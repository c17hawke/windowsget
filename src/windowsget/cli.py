import argparse
from pathlib import Path
from windowsget import download
from windowsget.logger import logger

def main():
    """
    Download a file from a given URL and save it to the specified output file or to the current
    working directory.

    The script takes a URL as input and downloads the file located at that URL to the specified
    output file or to the current working directory if no output file is specified. It uses the
    `windowsget` package to perform the download.

    Example usage:
        python downloader.py https://example.com/file.zip -o /path/to/output.zip
    """
    parser = argparse.ArgumentParser(
        description="Download a file from a given URL and save it to the specified output file or to the current working directory."
    )

    # Add a positional argument for the URL
    parser.add_argument(
        "url", type=str,
        help="The URL of the file to download."
    )

    # Add an optional argument for the output file
    parser.add_argument(
        "--output", "-o",
        help=("The path to save the downloaded file. If not set, the file will be saved to the "
              "current working directory with the same name as in the URL.")
    )

    # Parse the arguments
    args = parser.parse_args()

    # Set the filepath to the output file or to the current working directory
    filepath = args.output
    if filepath is None:
        filepath = Path(args.url).name
    try:
        # Download the file and get the size of the downloaded file
        file_size = download(URL=args.url, filepath=Path(filepath))
        # Print the success message with the filepath and size of the downloaded file
        logger.info(f"Download successfully completed at {filepath} of size: {file_size} bytes")
    except Exception as e:
        logger.exception(e)
        raise e

if __name__ == "__main__":
    main()
