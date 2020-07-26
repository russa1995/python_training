from selenium.webdriver.support.select import Select
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def clic_add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def return_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home page").click()

    def create_new_contact(self, contact):
        wd = self.app.wd
        # click add new contact
        self.app.open_home_page()
        self.clic_add_new_contact()
        self.fill_contact_form(contact)
        self.submit()
        # return to home page
        self.return_home_page()
        self.contact_list = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname",  contact.firstname)
        self.change_field_value("middlename",  contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.select_field_value("bday", contact.bday)
        self.select_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)

    def select_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_name).click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_element_by_index(index)
        # press Delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.contact_list = None

    def click_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index,  contact):
        wd = self.app.wd
        # click add new contact
        self.app.open_home_page()
        self.select_element_by_index(index)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(contact)
        self.update_changes()
        # return to home page
        self.return_home_page()
        self.contact_list = None

    def select_element_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def update_changes(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def count(self):
        wd = self.app.wd
        self.click_home()
        return len(wd.find_elements_by_name("selected[]"))

    contact_list = None

    def get_contact_list(self):
        if self.contact_list is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_list = []
            for element in wd.find_elements_by_name("entry"):
                text = element.find_element_by_name("selected[]").get_attribute("title")
                lastname = wd.find_elements_by_tag_name("td")[1]
                firstname = wd.find_elements_by_tag_name("td")[2]
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_list.append(Contact(name=text, id=id, lastname=lastname, firstname=firstname))
        return list(self.contact_list)



