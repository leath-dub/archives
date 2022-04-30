class Student(object):

    def set_attributes(self, sid, name, modlist):
        self.name = name
        self.sid = sid
        self.modlist = modlist

    def print_attributes(self):
        print("ID: {}".format(self.sid))
        print("Name: {}".format(self.name))
        print("Modules: {}".format(", ".join(self.modlist)))

    def add_module(self, mod):
        self.modlist.append(mod)

    def del_module(self, mod):
        self.modlist.remove(mod)
