# File Extension Recovery

This script is designed to recover the file name extension from a given path and rename the files accordingly. It is particularly useful for files that are photos or videos without any extension.

## Usage

1. **Clone the Repository:** Clone this repository to your local machine.

2. **Install Requirements:** Make sure you have Python installed on your machine. Additionally, install the required packages by running:
    ```
    pip install tqdm
    ```

3. **Run the Script:** Navigate to the directory where the script is located and run it by executing the following command:
    ```
    python file_extension_recovery.py
    ```

4. **Input Path:** Provide the path to the directory containing the files you want to recover extensions for. Modify the `path` variable in the script accordingly.

5. **Review Output:** Once the script is executed, it will recover extensions for files without extensions and rename them accordingly.

## Example

Suppose you have a directory containing files named `MGYM6489`, `IMG001`, `VIDEO123`, etc. After running the script, these files will be renamed to `MGYM6489.heic`, `IMG001.jpg`, `VIDEO123.mp4`, etc., based on their detected extensions.

## Notes

- This script relies on file signatures (magic numbers) to identify the file type and recover the extension. Therefore, it may not work correctly for all file types.
- Make sure to provide the correct path to the directory containing the files you want to process.
- Use caution when running the script, as it will rename files in the specified directory.

