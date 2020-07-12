from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, home=None, mobile=None,
                           work=None, fax=None, email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, id=None, name=None):
        self.firstname = firstname
        self.middlename =middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id
        self.name = name

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.name is None or other.name is None or self.name == other.name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize