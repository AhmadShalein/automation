import shutil
import  re
from faker import Faker

fake = Faker('en_US')

with open('potential-contacts.txt', 'r') as f:
    text = f.read().replace('\n', '')

phone_regex = re.compile(r'''((\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))?)''', re.VERBOSE)

email_regex = re.compile(r'''([a-zA-Z0-9._%+-]+ @[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))''', re.VERBOSE)

phones = []
emails = []

for i in phone_regex.findall(text):
    phone_num = '-'.join([i[1], i[3], i[5]])
    phone_num = re.sub(r'[(|)]','', phone_num)
    if phone_num not in phones:
        phones.append(phone_num)
for i in email_regex.findall(text):
    if i[0] not in emails:
        emails.append(i[0])

phones.sort()
emails.sort()

with open("./assets/phone_numbers.txt","w+") as f:
    for element in phones:
     f.write(element + "\n")

with open("./assets/emails.txt","w+") as f:
    for element in emails:
     f.write(element + "\n")

print(len(phones))
print(str(phones))
print("-" * 50)
print(len(emails))
print(str(emails))