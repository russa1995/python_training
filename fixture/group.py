class GroupHelper:

    def __init__(self, app):
        self.app = app

    def group_create(self, group):
        wd = self.app.wd
        # return to group page
        self.app.open_home_page()
        wd.find_element_by_link_text("groups").click()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.open_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        # select first group
        wd.find_element_by_name("selected[]").click()
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.open_groups_page()

    def open_groups_page(self):
        wd = self.app.wd
        # open groups page
        wd.find_element_by_link_text("groups").click()
