# -*- coding: utf-8 -*-


from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="2", middlename="3", lastname="4", nickname="345", title="xbbbf", company="xxbf",
                    address="4555", home="edrff", mobile="ffggr", work="afdgg",
                    fax="dgg", email="fgfggf", email2="gfggf", email3="gfggffg", homepage="555", bday="20",
                    bmonth="October", byear="1987")
    app.contact.create_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1  == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_add_empty_contact(app):
#    app.contact.create_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
#                    mobile="", work="",
#                    fax="", email="", email2="", email3="", homepage="", bday="", bmonth="October", byear="2000"))
