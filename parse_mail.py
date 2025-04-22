"""
from bs4 import BeautifulSoup

with open("./temp/mail.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

    links = soup.find_all("a", href=True)
    for link in links:
        print("Found link:", link["href"])

"""

linenum = 0

with open("./temp/mail.txt") as input_file:
    for line in input_file:
        linenum += 1
        if line.startswith("[DTVP]  ERGEBNISSE SUCHPROFIL:"):
            print(f"first line to check for: {linenum}")
        if line.startswith("Deutsche Bundesbank") and linenum > 1:
            print(f"first line for BuBa: {linenum}")
            break
