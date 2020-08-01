from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", user="root", db="addressbook", password="")

try:
    l = db.get_contacts_in_group(Group(id="76"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy