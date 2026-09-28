# # # #write a program to read a text file and displays the number of lines in a file
#
file = open("sample.txt.py", "r")

lines = file.readlines()

print("Number of lines:", len(lines))

file.close()
#
# # # #write a program to display the number of words in a file
#
f= open("sample.txt.py", "r")
data=f.read()
words = data.split()
print("Number of words:", len(words))
f.close()

# # #write a program to update the second line in a file
f= open("sample.txt.py", "r")
s=f.readlines()
s[1]="new line\n"

f.close()

f= open("sample.txt.py", "w")
f.writelines(s)
f.close()


# # #write a program to display the last 5 lines in a file
f = open("sample.txt.py", "r")
s = f.readlines()
f.close()

print(s[-5:])

#
# # #program to search a particular word in a file
f= open("sample.txt.py", "r")
s = f.read()
f.close()
word=input("enter a word:")
if word in s:
    print("word found")
else:
    print("word not found")
# #find the number of letters,digits,and spaces in a file

f= open("sample.txt.py", "r")
s=f.read()
f.close()
letters=0
digits=0
spaces=0

for ch  in s:
    if ch.isalpha():
        letters+=1
    elif ch.isdigit():
        digits+=1
    elif ch.isspace():
        spaces+=1
print("letters:",letters)
print("digits:",digits)
print("spaces:",spaces)

#reverse the lines in a file

# f=open("sample.txt.py","r")
# s=f.readlines()
# f.close()
# s.reverse()
# for i in s:
#     print(i)


f=open("sample.txt.py","r")
s=f.readlines()
print(s[::-1])
f.close()
f=open("sample.txt.py","r")
f.writelines(s)
f.close()

# A file totalstudents.txt contains the names of all students in a class,
# and a file passedstudents.txt contains the names of students who passed.txt the exam.
# Write a Python program to:
# Read the names from both files.
# # Find the students who did not pass.
# # Write their names to a new file named failed_students.txt, one name per line.
# #
f = open("totalstudents.txt.py", "r")
total = f.readlines()
f.close()

f = open("passedstudents.txt.py", "r")
passed = f.readlines()
f.close()

f = open("failed_students.txt.py", "w")

for student in total:
    if student not in passed:
        print(student, end="")
        f.write(student)

f.close()