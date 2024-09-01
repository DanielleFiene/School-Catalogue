class School:
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_numberOfStudents(self):
        return self.numberOfStudents

    def set_numberOfStudents(self, newNumberOfStudents):
        if isinstance(newNumberOfStudents, int):
            self.numberOfStudents = newNumberOfStudents

    def __repr__(self):
        return f'A {self.level} school named {self.name} which currently has {self.numberOfStudents} students.'


class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, 'primary', numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def get_pickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + f' The pickup policy is {self.pickupPolicy}.'


class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, 'high', numberOfStudents)
        self.sportsTeams = sportsTeams

    def get_sportsTeams(self):
        return self.sportsTeams

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + f' The sports teams are: {", ".join(self.sportsTeams)}.'


# Testing
b = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(b.get_pickupPolicy())  # Outputs: Pickup Allowed
print(b)  # Outputs: A primary school named Codecademy which currently has 300 students. The pickup policy is Pickup Allowed.

c = HighSchool('Oscar Romero', 4850, ['Golden Eagles', 'Horse Girls'])
print(c.get_sportsTeams())  # Outputs the list of sports teams.
print(c)  # Outputs: A high school named Oscar Romero which currently has 4850 students. The sports teams are: Golden Eagles, Horse Girls.
