from model.group import Group
import random
import string
import os.path
import json
import getopt
import sys

try:
        opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)

def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + string.punctuation +" "*10
    return prefix +  "".join(random.choice(symbol) for i in range(random.randrange(maxlen)))

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")

with open(file, "w") as f:
    f.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))