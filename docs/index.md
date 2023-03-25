# winget: python cli template

- `windowsget` is a Python-based command-line interface (CLI) utility that can be used to download files from the internet on Windows operating system. 
- It is designed to be similar to the `wget` command in Linux. The syntax for using `windowsget` is as follows:

    ```bash
    windowsget <url> -o <output file path>
    ```

- Here, `<url>` is the URL of the file you want to download. 
- `<output file path>` is the path where you want to save the downloaded file. The `-o` option specifies the output file path.

- For example, to download a file from `https://example.com/file.zip` and save it to `newfile.zip`, you would use the following command:

    ```bash
    windowsget https://example.com/file.zip -o newfile.zip
    ```

- `windowsget` supports various other options such as `-h` (help). You can see the full list of options and their descriptions by running windowsget `-h` or windowsget `--help`.

> NOTE: `windowsget` requires Python 3.x to be installed on your system in order to run.
