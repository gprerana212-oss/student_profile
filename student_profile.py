import sys
if len(sys.argv) != 5:
    print("Usage: python student_profile.py <Name> <USN> <Department> <Semester>")
    sys.exit()


name = sys.argv[1]
usn = sys.argv[2]
department = sys.argv[3]
semester = sys.argv[4]

if name and usn and department and semester:
    print("\n========== STUDENT PROFILE CARD ==========")
    print(f"Name       : {name}")
    print(f"USN        : {usn}")
    print(f"Department : {department}")
    print(f"Semester   : {semester}")
    print("===========================================\n")
else:
    print("Error: All four fields must be provided!")
