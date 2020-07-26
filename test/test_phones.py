import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_contact_info_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.home == clear_2(contact_contact_info_from_edit_page.home)
    assert contact_from_home_page.mobile == clear_2(contact_contact_info_from_edit_page.mobile)
    assert contact_from_home_page.work == clear_2(contact_contact_info_from_edit_page.work)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work

def clear_2(s):
    return re.sub("[() -]", "", s)