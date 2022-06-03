from random import randint
students = ["Andy Pandy", "Benny Menny", "Kim Simms", "Rolly Polly", "Cindy Mindy", "Geeta Peeta"]
courses = ["CS101", "CS105", "CS110", "CS115", "CS120"]

#Length for the list of students and courses
numC = len(courses)
numS = len(students)
def main():
    marks = initializeMarks(numC, numS)
    computeAllRanges(courses, marks)
    computeAllAverages(students, marks)

#Generating a multi-dimesional marks list for stuednts
def initializeMarks(numC, numS):
    marks = []
    for i in range(numC):
        row = [0] * numS
        marks.append(row)
    for i in range(numC):
        for j in range(numS):
            marks[i][j] = randint(0, 100)
    return marks

#Finding the Minimum and returning minimum
def findMinForRow(marks, row):
    min = 100
    for column in range(numS):
        if marks[row][column] < min:
            min = marks[row][column]
    return min

#Finding the Maximum and returning maximum
def findMaxForRow(marks, row):
    max = 0
    for column in range(numS):
        if marks[row][column] > max:
            max = marks[row][column]
    return max

#Funtion to calcualte the range
def printRangeForCourse(courses, position, maximum, minimum):
    Range = maximum - minimum
    print('{0:>15}{1:^25}'.format(courses[position], Range))

#Funtion to create the table and display the values for student name and average marks
def computeAllAverages(students, marks):
    print('{0:>15}{1:^25}'.format("Student Name", "Average Marks"))    #Output for the tables
    for i in range(len(marks[0])):
        total = 0
        for j in range(len(marks)):
            total += marks[j][i]
        average = total / len(marks)
        print('{0:>15}{1:^25}'.format(students[i], average))

#Funtion to create the table and display the blaues for courses and range of marks
def computeAllRanges(courses, marks):
    print('{0:>15}{1:^25}'.format("Courses", "Range of Marks"))
    for i in range(len(marks)):
        printRangeForCourse(courses, i, findMaxForRow(marks, i), findMinForRow(marks, i))
    print()


main()