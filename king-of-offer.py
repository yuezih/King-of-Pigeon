'''
Coding with the assistance of Github Copilot:
- Copilot automatically completed some unfinished comments.
- Copilot generated almost all of the Python code.
'''

file_list = ['PKUxk','THUsz_ai','THUsz_cs','THUsz_data','USTC_cs']

# file_list是一个夏令营，对应的txt文件在当前目录下的data文件夹中
# 文件中的每一行都是一个学生的名字

# 定义一个学生类，包括学生的名字和参加的camper
class Student(object):
    def __init__(self, name):
        self.name = name
        self.camper = []

    def add_camper(self, camper):
        self.camper.append(camper)

    def __str__(self):
        return self.name + ': ' + str(self.camper)

student_list = []

for file in file_list:
    with open('data/' + file + '.txt', 'r') as f:
        for line in f:
            # 如果学生列表中没有这个学生，就添加进去
            if not any(student.name == line.strip() for student in student_list):
                std = Student(line.strip())
                std.add_camper(file)
                student_list.append(std)
            else:
                # 如果学生列表中有这个学生，且file不在camper列表中，就把file加到这个学生的camper列表中
                for student in student_list:
                    if student.name == line.strip() and file not in student.camper:
                        student.add_camper(file)

# 打印学生和他们参加的夏令营，按照参加的夏令营数量排序
for student in sorted(student_list, key=lambda x: len(x.camper), reverse=True):
    print(student)