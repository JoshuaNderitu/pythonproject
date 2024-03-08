from statistics import mean  # Import the mean function

admins = {'Joshua': 'pass123@'}

StudentDict = {'Kelly': [78, 88, 93], 'Alex': [92, 76, 88], 'Sam': [89, 92, 93]}

def entergrades():
    nametoEnter = input('Student Name: ')
    gradetoEnter = float(input('Grade: '))  # Convert input grade to float

    if nametoEnter in StudentDict:
        print('Adding Grade....')
        StudentDict[nametoEnter].append(gradetoEnter)
    else:
        print('Student does not Exist')

    print(StudentDict)

def removeStudent():
    nametoRemove = input('Student Name: ')

    if nametoRemove in StudentDict:
        print('Removing Student...')
        del StudentDict[nametoRemove]
    else:
        print('Student does not Exist')

    print(StudentDict)

def studentAVGs():
    for eachstudent in StudentDict:
        gradeList = StudentDict[eachstudent]
        avgGrade = mean(gradeList)  # Correctly use the mean function

        print(eachstudent, 'has an average Grade of', avgGrade)
    
    print(StudentDict)

def main():
    print("""
    Welcome to Grade Central!
    
    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average grade
    [4] - Exit
    """)

    action = input("What would you like to do today? (Enter a number): ")

    if action == '1':
        entergrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAVGs()  # Call the function, don't print it
    elif action == '4':
        exit()
    else:
        print("No valid Choice!")

login = input('Username: ')
PassW = input('Password: ')

if login in admins:
    if admins[login] == PassW:
        print('Welcome,', login)
        while True:
            main()
    else:
        print('Invalid Password')
else:
    print('Invalid Username!')
