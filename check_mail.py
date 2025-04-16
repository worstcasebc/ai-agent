import os
from imap_tools import MailBox

from dotenv import load_dotenv

load_dotenv()

with MailBox("imap.gmail.com").login(
    os.getenv("EMAIL_ACCOUNT"), os.getenv("EMAIL_PASSWORD"), os.getenv("EMAIL_FOLDER")
) as mailbox:
    for msg in mailbox.fetch(limit=1, reverse=True, mark_seen=False):
        print(msg.subject)
        # print(msg.text)
        # print(msg.from_)
        # print(msg.date)
        # print(msg.to)
        # print(msg.html)
        # print(msg.attachments)

        # write msg.text into file for analysis with llm-agent
        with open(os.getenv("EMAIL_PATH_HTML"), "a") as myfile:
            print("✨ write mail")
            myfile.write(msg.html)

        with open(os.getenv("EMAIL_PATH"), "a") as myfile:
            print("✨ write mail")
            myfile.write(msg.text)
