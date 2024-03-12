import re
mbno = input("Enter Mobile Number: ")
mob_valpat = "[0|91]?[-\s]?[6-9]\d{9}"
if re.search(mob_valpat,mbno):
    print("Valid Mobile No.")
else:
    print("Invalid Mobile No.")
