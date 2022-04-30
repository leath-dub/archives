class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return "{} {} {}".format(
            self.name, self.phone, self.email)

class ContactList(object):

    def __init__(self):
        self.d = {}

    def add(self, instance):
        self.d[instance.name] = instance

    def remove(self, name):
        if name in self.d:
            del self.d[name]

    def get(self, name):
        if name in self.d:
            return self.d[name]

    def __str__(self):
        rlist = []
        rlist.append("Contact list\n------------")
        for k, v in sorted(self.d.items()):
            rlist.append("{}".format(v))
        return "\n".join(rlist)
