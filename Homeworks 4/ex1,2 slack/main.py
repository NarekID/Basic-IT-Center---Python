class Student():

    def __init__(self, name, surname, age, scores):
        self.m_name = name
        self.m_surname = surname
        self.m_age = age
        self.m_scores = scores

    def avg_score(self):
        n = len(self.m_scores)
        s = 0
        for i in self.m_scores:
            s += i
        return s / n

class Building():

    def __init__(self, floor, entrance, apartments):
        self.m_floor = floor
        self.m_entrance = entrance
        self.m_apartments = apartments

    def apartments_count(self):
        return self.m_floor * self.m_entrance * self.m_apartments


stud1 = Student("Karen", "Avetisyan", 17, [4, 4, 5, 5, 5])
stud2 = Student("Arman", "Sargsyan", 16, [3, 3, 4, 4, 3])
print(stud1.m_name, stud1.m_surname, "average score =", stud1.avg_score())
print(stud2.m_name, stud2.m_surname, "average score =", stud2.avg_score())

build1 = Building(5, 5, 4)
build2 = Building(10, 3, 4)
print(build1.apartments_count())
print(build2.apartments_count())