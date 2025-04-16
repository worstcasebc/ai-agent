from bs4 import BeautifulSoup

with open("./temp/mail.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

    links = soup.find_all("a", href=True)
    for link in links:
        print("Found link:", link["href"])
