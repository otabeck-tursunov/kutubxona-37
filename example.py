class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def about(self):
        return self.first_name + ' ' + self.last_name


qilichbek = Student(first_name='Qilichbek', last_name='Bek')
qilichbek.last_name = "Mansurov"
print(qilichbek.about())