class Employee:
    def __init__(self,name,hourly_rate,hours):
        self.__name = name
        self.__hours=hours
        if hourly_rate<0:
            raise ValueError("Некорректный возраст")
        else:
            self.__hourly_rate=hourly_rate
    @property
    def name(self):
        return self.__name
    def display_info(self):
        print(f"Name: {self.__name}")
    @property
    def hours(self):
        return self.__hours
    @hours.setter
    def add_hours(self,h):
        if 0<h<=12:
            self.__hours+=h
        else:
            raise ValueError
    @property
    def calculate_salary(self):
        return self.__hourly_rate*self.__hours
    @property
    def total_salary(self):
        r=self.__hourly_rate*self.__hours
        self.__hours=0
        return r
