import zipfile
import os
from dotenv import load_dotenv

load_dotenv()


def extract_zip(zip_path, extract_to):
    """Extracts a zip file to the specified directory."""
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted {zip_path} to {extract_to}")


extract_zip(os.getenv("SOURCE_ZIP"), os.getenv("DATA_PATH"))

# Check if the extraction was successful
if os.path.exists(os.getenv("DATA_PATH")):
    print(f"Extraction successful. Files are located in {os.getenv('DATA_PATH')}")
else:
    print(f"Extraction failed. No files found in {os.getenv('DATA_PATH')}")

# List the files in the extraction directory
extracted_files = os.listdir(os.getenv("DATA_PATH"))
print("Extracted files:")
for file in extracted_files:
    print(file)
