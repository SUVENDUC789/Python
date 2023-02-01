class Shambhu:
    family = "Chowdhury Industry "

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


class Debashis(Shambhu):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age


class Suvendu(Debashis):
    def __init__(self, fname, lname, age, lang):
        super().__init__(fname, lname, age)
        self.lang = lang

    def dettails(self):
        print("Family-Name : ", Suvendu.family)
        print("First-Name : ", self.fname)
        print("Last-Name : ", self.lname)
        print("Age : ", self.age)
        print("Lang : ", self.lang)


suv = Suvendu("Suvendu", "Chowdhury", 20, "English")
suv.dettails()
