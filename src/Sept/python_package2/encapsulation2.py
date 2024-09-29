class Encapsulation_part2:
    public_variable1 = "Private Variable"
    _protected_variable1 = "Protected Variable"
    __private_variable1 = "Private Variable"

    def fetch_private(self):
        print(self.__private_variable1)

    def fetch_protected(self):
        print(self._protected_variable1)

    def fetch_public(self):
        print(self.public_variable1)

