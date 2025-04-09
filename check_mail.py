#!/usr/bin/env python
#
# Basic example of using Python3 and IMAP to read emails in a gmail folder/label.
# Remove legacy email.header api use.
import os
import sys
import imaplib
import email
import datetime
import base64
from dotenv import load_dotenv

load_dotenv()


def process_mailbox(M):
    """
    Do something with emails messages in the folder.
    For the sake of this example, print some headers.
    """

    rv, data = M.search(None, "ALL")
    if rv != "OK":
        print("No messages found!")
        return

    for num in data[0].split():
        rv, data = M.fetch(num, "(RFC822)")
        if rv != "OK":
            print("ERROR getting message", num)
            return

        msg = email.message_from_bytes(data[0][1])
        subject = msg["Subject"]
        subject = subject[10 : subject.find("?=")]
        # print(f"Subject: {subject}")
        print(
            f"Message {num.decode('utf-8')}: {base64.b64decode(subject).decode('utf-8')}"
        )
        print("Raw Date:", msg["Date"])
        # Now convert to local date-time
        date_tuple = email.utils.parsedate_tz(msg["Date"])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(
                email.utils.mktime_tz(date_tuple)
            )
            print("Local Date:", local_date.strftime("%a, %d %b %Y %H:%M:%S"))


M = imaplib.IMAP4_SSL("imap.gmail.com")

try:
    rv, data = M.login(os.getenv("EMAIL_ACCOUNT"), os.getenv("EMAIL_PASSWORD"))
except imaplib.IMAP4.error:
    print("LOGIN FAILED!!! ")
    sys.exit(1)

# print(rv, data)


# rv, mailboxes = M.list()
# if rv == "OK":
#     print("Mailboxes:")
#     print(mailboxes)

rv, data = M.select(os.getenv("EMAIL_FOLDER"))
if rv == "OK":
    # print("Processing mailbox...\n")
    process_mailbox(M)
    M.close()
else:
    print("ERROR: Unable to open mailbox ", rv)

M.logout()
