from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host="127.0.0.1", user="root", db="addressbook", password="")

def test_add_contact_to_group(app, orm):
    if app.group.count() == 0:
        app.group.group_create(Group(name="test"))
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname="test"))
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    app.contact.add_contact_to_group(group.id, contact.id)
    assert Contact(id=contact.id) in db.get_contacts_in_group(Group(id=group.id))
