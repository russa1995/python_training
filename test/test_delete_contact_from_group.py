from model.group import Group
from model.contact import Contact
import random


def test_delete_contact_from_group(app, db):
    if app.group.count() == 0:
        app.group.group_create(Group(name="test"))
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.contact.delete_contact_from_group(group.id, contact.id)