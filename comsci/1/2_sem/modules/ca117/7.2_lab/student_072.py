class Student(object):

    def __init__(self, sid, name, modlist=0):
        self.sid = sid
        self.name = name
        self.modlist = [] if not(modlist) else modlist

    def add_module(self, mod_name):
        self.modlist.append(
            mod_name) if mod_name not in self.modlist else False

    def del_module(self, mod_name):
        self.modlist.remove(
            mod_name) if mod_name not in self.modlist else False

    def __str__(self):
        return "ID: {}\nName: {}\nModules: {}".format(
            self.sid, self.name, ", ".join(self.modlist))
