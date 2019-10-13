class Truck():
    def __init__(self, engine, gearbox, chassis, color):
        self.m_engine = engine
        self.m_gearbox = gearbox
        self.m_chassis = chassis
        self.m_color = color

    def print_specs(self):
        print("Engine:", self.m_engine)
        print("Gearbox:", self.m_gearbox)
        print("Chassis:", self.m_chassis)
        print("Color:", self.m_color)

class Scania(Truck):
    def __init__(self, engine, gearbox, chassis, color, model, year):
        super().__init__(engine, gearbox, chassis, color)
        self.m_model = model
        self.m_year = year

    def print_specs(self):
        print("Scania", self.m_model)
        print("Year:", self.m_year)
        print("Engine:", self.m_engine)
        print("Gearbox:", self.m_gearbox)
        print("Chassis:", self.m_chassis)
        print("Color:", self.m_color)

class Volvo(Truck):
    def __init__(self, engine, gearbox, chassis, color, model, year):
        super().__init__(engine, gearbox, chassis, color)
        self.__model = model
        self.__year = year

    def print_specs(self):
        print("Volvo", self.__model)
        print("Year:", self.__year)
        print("Engine:", self.m_engine)
        print("Gearbox:", self.m_gearbox)
        print("Chassis:", self.m_chassis)
        print("Color:", self.m_color)

ScaniaS730 = Scania("730hp 16.4L V8 EURO6", "GRSO925R", "6x4", "Red", "S", 2019)
VolvoFH13_540 = Volvo("540hp 13L L6 EURO6", "ATO2612D", "4x2", "White", "FH13", 2017)

ScaniaS730.print_specs()
print()
VolvoFH13_540.print_specs()