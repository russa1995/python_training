from model.contact import Contact
import random

def test_delete_contact(app, db, check_ui):
    contact = Contact(firstname="test")
    if app.contact.count() == 0:
        app.contact.create_new_contact(contact)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)