class GeeksPeople: 
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Имя - {self.name} \nЭл.почта - {self.email} \nНомер телефона - {self.phone}"

kudbuhan = GeeksPeople("Кудбухан", "geekskutbuhan@gmail.com", "+996 554 20 22 20")
print(kudbuhan)

class Student(GeeksPeople):
    def __init__(self, name, email, phone, student_id, group_where_study):
        GeeksPeople.__init__(self, name, email, phone)
        self.student_id = student_id
        self.group_where_study = group_where_study

    def study(self):
        print(f"Имя - {self.name} \n Эл.почта - {self.email} \n Номер телефона - {self.phone} \nГруппа - {self.group_where_study} \nid студента - {self.student_id} \n")

oydinoy = Student("Ойдиной", "olyausmanova@gmail.com", "+996 554 03 30 30", 15243791, "17-1B")
oydinoy.study()

class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, group_where_teacher):
        GeeksPeople.__init__(self, name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teacher = group_where_teacher

    def teach(self):
        print(f"Имя - {self.name} \n Эл.почта - {self.email} \n Номер телефона - {self.phone} \nГруппа - {self.group_where_teacher} \nid учителя - {self.teacher_id} \n")

syimyk = Teacher("Сыймык", "syimyk@gmail.com", "+996 555 01 10 10", 51545856, "17-1B")
syimyk.teach()

class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        GeeksPeople.__init__(self, name, email, phone)
        self.admin_id = admin_id

    def creat_group(self):
        print(f"Имя - {self.name} \n Эл.почта - {self.email} \n Номер телефона - {self.phone}  \nid администратора - {self.admin_id} \n")

admin = Admin('Улан', 'ulan@gmail.com', '+996 553 41 14 14',  23568914)
admin.creat_group()

class Mentor(Student, Teacher):
    def __init__(self, name, email, phone, student_id, group_where_study, teacher_id, group_where_teacher):
        Student.__init__(self, name, email, phone, student_id, group_where_study)
        Teacher.__init__(self, name, email, phone, teacher_id, group_where_teacher)

mentor = Mentor("Элиза", "eliza.@gmail.com", "+996 554 60 06 06", 15243791, "17-1B", 51545856, "17-1B")
mentor.teach()
mentor.study()

