import StudentClass as s 

#I assume there is already a student exist 

dob = '10/06/1999'
classi = 'Freshman'


student = s.Student(dob,classi)
student.age()

student.reg_time() 

print("Your age is ",student.get_age())
print("Your registration time is ",student.get_reg_time() )



