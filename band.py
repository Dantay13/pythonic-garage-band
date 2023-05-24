class Musician:
    def __str__(self):
        return f"{self.__class__.__name__}: {self.get_instrument()}"

    def __repr__(self):
        return self.__str__()

    def get_instrument(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def play_solo(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Guitarist(Musician):
    def get_instrument(self):
        return "Guitar"

    def play_solo(self):
        return "Guitar solo"


class Bassist(Musician):
    def get_instrument(self):
        return "Bass"

    def play_solo(self):
        return "Bass solo"


class Drummer(Musician):
    def get_instrument(self):
        return "Drums"

    def play_solo(self):
        return "Drum solo"


class Band:
    all_bands = []

    def __init__(self, name):
        self.name = name
        self.members = []
        Band.all_bands.append(self)

    def play_solos(self):
        solos = [member.play_solo() for member in self.members]
        return solos

    def __str__(self):
        return f"Band: {self.name}"

    def __repr__(self):
        return self.__str__()

    @classmethod
    def to_list(cls):
        return cls.all_bands



if __name__ == "__main__":
    guitarist = Musician()
    bassist = Musician()
    drummer = Musician()

