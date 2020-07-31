# -*- coding: utf-8 -*-


from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + string.punctuation +" "*10
    return prefix +  "".join(random.choice(symbol) for i in range(random.randrange(maxlen)))

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                    address="", home="", mobile="", work="",
                    fax="", email="", email2="", email3="", homepage="", bday="20",
                    bmonth="October", byear="1987")] + [
    Contact(firstname=random_string("name", 10), middlename=random_string("header", 20), lastname=random_string("footer", 20),
            nickname=random_string("name", 10), title=random_string("header", 20), company=random_string("footer", 20),
            address=random_string("name", 10), home=random_string("header", 20), mobile=random_string("footer", 10),
            work=random_string("name", 10), fax=random_string("header", 20), email=random_string("footer", 20),
            email2=random_string("name", 10), homepage=random_string("header", 20))
    for i in range(3)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    pass
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    assert len(old_contacts) + 1  == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
