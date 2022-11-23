import csv

def main():
    student_id = 0
    student_name = 1
    studentsLog = {}
    userInpt = int(input('Enter Student ID: '))


    with open('programming-with-functions\students\students.csv','rt') as students:
        reader = csv.reader(students)
        next(reader)
        for student in reader:
            key = int(student[student_id])
            studentsLog[key] = student[student_name]

    # if userInpt in studentsLog.items():
    #     print(userInpt)

    for key, value in studentsLog.items():
        if userInpt == key:
            print(f'The student with the id {userInpt} is {value}')
            print(len(userInpt))
        else:
            print('User not found')



if __name__ == '__main__':
    main()