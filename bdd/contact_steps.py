from pytest_bdd import given, when, then
from model.contact import Contact
import random

@given('a contact list')
def contact_list(db):
    return db.get_contact_list()

@given('a contact with <firstname>, <lastname> and <address>')
def new_contact(firstname, lastname, address):
    return Contact(firstname=firstname, lastname=lastname, address=address)

@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create_new_contact(new_contact)

@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, app, contact_list, new_contact, check_ui):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        new_contacts = app.contact.get_contact_list()
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

@given('a non-empty contact list')
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname='some test'))
    return db.get_contact_list()

@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)

@then('the new list is equal to the old list without the deleted contact')
def verify_contact_deleted(app, db, non_empty_contact_list, random_contact, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

@when('I edit the contact from the list')
def edit_contact(app, random_contact):
    app.contact.edit_contact_by_id(random_contact.id, Contact(firstname="test"))

@then('the new list is equal to the old list with the edited contact')
def verify_contact_edited(app, db, non_empty_contact_list, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        old_contacts = app.contact.get_contact_list()
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)