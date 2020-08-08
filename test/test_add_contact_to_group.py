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
    group = random.choice(orm.get_group_list())
    contacts = db.get_contact_list()
    contacts_without_groups = []
    for contact in contacts:
        if Contact(id=contact.id) in db.get_contacts_not_in_group(Group(id=group.id)):
            contacts_without_groups.append(contact)
    if len(contacts_without_groups) == 0:
        app.contact.contact(Contact(firstname="test"))
        contacts = db.get_contact_list()
        for contact in contacts:
            if Contact(id=contact.id) in db.get_contacts_not_in_group(Group(id=group.id)):
                contacts_without_groups.append(contact)
    app.contact.add_contact_to_group(group.id, contacts_without_groups[0].id)
    assert Contact(id=contacts_without_groups[0].id) in db.get_contacts_in_group(Group(id=group.id))
