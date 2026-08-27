n = int(input("Enter number of students: "))

class_total = 0

for i in range(n):
    print("Student", i + 1)

    m1 = int(input("Enter marks: "))
    m2 = int(input("Enter marks: "))
    m3 = int(input("Enter marks: "))
    m4 = int(input("Enter marks: "))
    m5 = int(input("Enter marks: "))

    average = (m1 + m2 + m3 + m4 + m5) / 5

    print("Average =", average)

    passed = average >= 40

    if passed:
        print("Result = Pass")
    else:
        print("Result = Fail")

    class_total = class_total + average

print("Class Average =", class_total / n)