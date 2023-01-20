import re
import csv
from pandas import *

valid_email = []
invalid_email = []

def isvalidEmail(email):
    
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # objs = re.search(regex, email)
    if (re.fullmatch(regex,email)):

        valid_email.append(email)
    else:

        invalid_email.append(email)

def check_mail(save_file):
    emails = read_csv(save_file)

    mails = emails['Email Address'].to_list()

    # print(mails)

    for mail in mails:

        VorNotV = isvalidEmail(mail)
