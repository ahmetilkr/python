from koşullar_döngüler.enumerate import students

salaries=[1000,2000,3000,5000,7000]

[salary * 2 for salary in salaries if salary < 3000]

[salary * 2 if salary < 3000 else salary*0 for salary in salaries]



#students_no içindeyse eğer öğrenci adını küçült değilse büyült
students=["ahmet","mehmet","ali","davut"]
students_no=["mehmet","ali"]

[student.lower() if student in students_no else student.upper() for student in students ]