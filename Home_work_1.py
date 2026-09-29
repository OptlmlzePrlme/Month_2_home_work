class A_Team:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce_1(self):
        ED_retun_value = lambda x: "this man does have higher education" if self.higher_education else "this man doesn't have higher education"
        return 'Name: {}, date of birth {}, skills: {}, {}.'.format(self.name, self.birth_date, self.occupation, ED_retun_value(self.higher_education))

person_1 = A_Team('John "Hannibal" Smith', '01.10.1928', "Team leader, master tactician, and master of disguise", True)
person_2 = A_Team('Templeton Arthur "Faceman" Peck', '01.03.1945', "Con artist, smooth talker, and procurement expert", True)
person_3 = A_Team('H.M. (Howling Mad) Murdock', "24.11.1947", "Pilot extraordinaire; capable of flying almost any aircraft", True)
person_4 = A_Team('Bosco Albert "B.A." (Bad Attitude) Baracus', '21.05.1952', " Mechanic genius, heavy muscle and a driver ", False)

print(person_1.introduce_1())
print(person_2.introduce_1())
print(person_3.introduce_1())
print(person_4.introduce_1())



