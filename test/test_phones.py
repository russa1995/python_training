import re
from model.contact import Contact

def test_phones_on_home_page(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contact_from_home_page)):
        assert clear(contact_from_home_page[i].address) == clear(contact_from_db[i].address)
        assert clear(contact_from_home_page[i].firstname) == clear(contact_from_db[i].firstname)
        assert clear(contact_from_home_page[i].lastname) == clear(contact_from_db[i].lastname)
        assert clear(contact_from_home_page[i].all_phones_from_home_page) == clear(merge_phones_like_on_home_page(contact_from_db[i]))
        assert clear(contact_from_home_page[i].email) == clear(merge_emails_like_on_home_page(contact_from_db[i]))


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))