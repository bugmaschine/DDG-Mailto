from importlib import import_module
import sys
from requests.structures import CaseInsensitiveDict

import pyperclip
import requests

url = "https://quack.duckduckgo.com/api/email/addresses"
ddgEmail = ""
targetEmail = ""
key = ""

def returnEmail(target, fromMail):
    target = target.replace("@", "_at_")
    return target + "_" + fromMail

def generateEmail(key):
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer " + key
    headers["Host"] = "quack.duckduckgo.com"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0"
    r = requests.post(url, headers=headers)
    if r.status_code == 201:
        email = r.json()["address"] + "@duck.com"
        return email
    else:
        print("Error: " + str(r.status_code))
        print(r.text)
        sys.exit(1)

if (len(sys.argv) != 2):
    print("Please provide a target email address")
    targetEmail = input("What is the email you are sending to?: ")
else:
    targetEmail = sys.argv[1]

ddgEmail = generateEmail(key)

outputEmail = returnEmail(targetEmail, ddgEmail)

print("Your email is: " + ddgEmail)
print("Your target email is: " + targetEmail)
print("Send email to: " + outputEmail)

print("Copied to clipboard")
pyperclip.copy(outputEmail)

# Layout:
# name_at_domain_ddgmail

# TODO :
# make the code look beter


