from model.contact import Contact

def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(firstname="new", middlename="new", lastname="new", nickname="new", title="new", company="new",
                    address="new", home="new", mobile="new", work="new",
                    fax="new", email="new", email2="new", email3="new", homepage="new", bday="1",
                    bmonth="October", byear="2020"))