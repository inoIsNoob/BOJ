student = []
for _ in range(int(input())):
  student.append(input())

if student == sorted(student):
  print('INCREASING')
elif student == sorted(student, reverse = True):
  print('DECREASING')
else:
  print('NEITHER')
