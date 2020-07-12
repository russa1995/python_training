from model.contact import Contact

def test_edit_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="new", middlename="new", lastname="new", nickname="new", title="new", company="new",
                    address="new", home="new", mobile="new", work="new",
                    fax="new", email="new", email2="new", email3="new", homepage="new", bday="1",
                    bmonth="October", byear="2020")
    contact.id = old_contacts[0].id
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname="test"))
    app.contact.edit_first_contact(contact)
    assert len(old_contacts)  == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)