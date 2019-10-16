class Fraction():
    def __init__(self, numerator, denominator):
        self.m_numerator = numerator
        self.m_denominator = denominator

    def print_fraction(self):
        print(self.m_numerator, "/", self.m_denominator)

    def __add__(self, other):
        if self.m_denominator == other.m_denominator:
            temp_num = self.m_numerator + other.m_numerator
            temp_denom = self.m_denominator
        elif self.m_denominator % other.m_denominator == 0:
            other.m_numerator *= self.m_denominator // other.m_denominator
            temp_num = self.m_numerator + other.m_numerator
            temp_denom = self.m_denominator
        elif other.m_denominator % self.m_numerator == 0:
            self.m_numerator *= other.m_denominator // self.m_denominator
            temp_num = self.m_numerator + other.m_numerator
            temp_denom = self.m_numerator
        else:
            temp_num = self.m_numerator * other.m_denominator + other.m_numerator * self.m_denominator
            temp_denom = self.m_denominator * other.m_denominator
        temp_num, temp_denom = Fraction.cut_fraction(temp_num, temp_denom)
        return Fraction(temp_num, temp_denom)

    def __sub__(self, other):
        if self.m_denominator == other.m_denominator:
            temp_num = self.m_numerator - other.m_numerator
            temp_denom = self.m_denominator
        elif self.m_denominator % other.m_denominator == 0:
            other.m_numerator *= self.m_denominator // other.m_denominator
            temp_num = self.m_numerator - other.m_numerator
            temp_denom = self.m_denominator
        elif other.m_denominator % self.m_numerator == 0:
            self.m_numerator *= other.m_denominator // self.m_denominator
            temp_num = self.m_numerator - other.m_numerator
            temp_denom = self.m_numerator
        else:
            temp_num = self.m_numerator * other.m_denominator - other.m_numerator * self.m_denominator
            temp_denom = self.m_denominator * other.m_denominator
        temp_num, temp_denom = Fraction.cut_fraction(temp_num, temp_denom)
        return Fraction(temp_num, temp_denom)

    def __mul__(self, other):
        temp_num = self.m_numerator * other.m_numerator
        temp_denom = self.m_denominator * other.m_denominator
        temp_num, temp_denom = Fraction.cut_fraction(temp_num, temp_denom)
        return Fraction(temp_num, temp_denom)

    def __floordiv__(self, other):
        temp_num = self.m_numerator * other.m_denominator
        temp_denom = self.m_denominator * other.m_numerator
        temp_num, temp_denom = Fraction.cut_fraction(temp_num, temp_denom)
        return Fraction(temp_num, temp_denom)

    def __eq__(self, other):
        return self.m_numerator / self.m_denominator == other.m_numerator / other.m_denominator
    def __ne__(self, other):
        return self.m_numerator / self.m_denominator != other.m_numerator / other.m_denominator
    def __gt__(self, other):
        return self.m_numerator / self.m_denominator > other.m_numerator / other.m_denominator
    def __lt__(self, other):
        return self.m_numerator / self.m_denominator < other.m_numerator / other.m_denominator
    def __ge__(self, other):
        return self.m_numerator / self.m_denominator >= other.m_numerator / other.m_denominator
    def __le__(self, other):
        return self.m_numerator / self.m_denominator <= other.m_numerator / other.m_denominator

    @staticmethod
    def cut_fraction(a, b):
        if a == b:
            return 1, 1
        elif a > b:
            for i in range(b, 1, -1):
                if a % i == 0 and b % i == 0:
                    a //= i
                    b //= i
                    return a, b
        else:
            for i in range(a, 1, -1):
                if a % i == 0 and b % i == 0:
                    a //= i
                    b //= i
                    return a,b
        return a,b

kot1 = Fraction(2, 6)
kot2 = Fraction(1, 5)
kot3 = kot1 // kot2
kot3.print_fraction()
print(kot1 == kot2)
print(kot1 != kot2)
print(kot1 > kot2)
print(kot1 >= kot2)
print(kot1 < kot2)
print(kot1 <= kot2)