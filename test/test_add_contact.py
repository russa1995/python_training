# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new_contact(Contact(firstname="2", middlename="3", lastname="4", nickname="345", title="xbbbf", company="xxbf",
                    address="4555", home="edrff", mobile="ffggr", work="afdgg",
                    fax="dgg", email="fgfggf", email2="gfggf", email3="gfggffg", homepage="555", bday="20",
                    bmonth="October", byear="1987"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                    mobile="", work="",
                    fax="", email="", email2="", email3="", homepage="", bday="", bmonth="October", byear="2000"))
    app.session.logout()
