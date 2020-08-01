from model.contact import Contact
import random

def test_edit_contact(app,  db, check_ui):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.edit_contact_by_id(contact.id, Contact(firstname="test"))
    assert len(old_contacts)  == app.contact.count()
    if check_ui:
        old_contacts = db.get_contact_list()
        new_contacts = app.contact.get_contact_list()
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)