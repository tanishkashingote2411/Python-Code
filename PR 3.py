assignments = ["DBMS", "SE", "MCA", "EE", "DSA"]

print("My assignments:", assignments)

assignments.append("Python")
print("Added:", assignments)

completed = input("Enter completed assignments: ")
if completed in assignments:
    assignments.remove(completed)
    print("removed:", assignments)

else:
    print("Assignments not found")