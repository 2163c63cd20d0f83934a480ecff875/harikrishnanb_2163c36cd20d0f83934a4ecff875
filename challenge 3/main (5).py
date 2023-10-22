class student:

  def __init__(self,name,roll_number,cgpo):
    self.name=name
    self.roll_number=roll_number



def sort_students(student_list):
  sorted_student= sorted(student_list,key=lambda student: student.cgpa, reverse=true)
  return sorted_students

#example usage:
student = [ 
  student("hari","a123",7.8),
  student("ajay","a124",8.9),
  student("bharath","a125",9.1),
  student("mohan","a126",9.9),
]

sorted_student = sort_student(students)

for student in sorted_student:
  print("name: {}, roll number: {}, cgpa:{}".fromat(student.name, student.cgpa))
student.roll_number,