from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
        opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)

n=5
f="data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + string.punctuation +" "*10
    return prefix +  "".join(random.choice(symbol) for i in range(random.randrange(maxlen)))

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                    address="", home="", mobile="", work="",
                    fax="", email="", email2="", email3="", homepage="", bday="20",
                    bmonth="October", byear="1987")] + [
    Contact(firstname=random_string("name", 10), middlename=random_string("header", 20),
            lastname=random_string("footer", 20),
            nickname=random_string("name", 10), title=random_string("header", 20), company=random_string("footer", 20),
            address=random_string("name", 10), home=random_string("header", 20), mobile=random_string("footer", 10),
            work=random_string("name", 10), fax=random_string("header", 20), email=random_string("footer", 20),
            email2=random_string("name", 10), homepage=random_string("header", 20)
            )
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))