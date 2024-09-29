class Encapsulation_part1:

    public_variable = "Private Variable"
    _protected_variable = "Protected Variable"
    __private_variable = "Private Variable"

    def fetch_private(self):
        print(self.__private_variable)

    def fetch_protected(self):
        print(self._protected_variable)

    def fetch_public(self):
        print(self.public_variable)