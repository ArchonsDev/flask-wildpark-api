class AccountModel:
    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname

    def to_dict(self):
        return {"id": self.id, "firstname": self.firstname, "lastname": self.lastname}
