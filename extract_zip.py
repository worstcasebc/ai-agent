import zipfile
import os
from dotenv import load_dotenv

load_dotenv()

def extract_zip(zip_path, extract_to):
    """Extracts a zip file to the specified directory."""
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted {zip_path} to {extract_to}")


zip_filename = "C:\\Users\\baumanns\\Downloads\\Vergabeunterlagen_CXP4Y635F4H.zip"  # Replace with your zip file name
extract_to_path = ".\\temp\\bid"  # Replace with your extraction path

extract_zip(os.getenv("SOURCE_ZIP"), extract_to_path)

# Check if the extraction was successful
if os.path.exists(extract_to_path):
    print(f"Extraction successful. Files are located in {extract_to_path}")
else:
    print(f"Extraction failed. No files found in {extract_to_path}")

# List the files in the extraction directory
extracted_files = os.listdir(extract_to_path)
print("Extracted files:")
for file in extracted_files:
    print(file)
