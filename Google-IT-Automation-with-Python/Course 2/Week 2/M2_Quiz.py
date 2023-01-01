#Question 1
import os

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as python_file:
    filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))


# Question 2
import os

def new_directory(directory, filename):
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  os.chdir(directory)
  with open (filename, "w") as file:
    pass

  return os.listdir()

print(new_directory("PythonPrograms", "script.py"))

# Question 4
import os
import datetime

def file_date(filename):
  os.mknod(filename)
  timestamp = os.path.getmtime(filename)
  date =datetime.datetime.fromtimestamp(timestamp)
  return ("{:%Y-%m-%d}".format(date))
print(file_date("newfile.txt")) 

#Question 5
import os
def parent_directory():
  relative_parent = os.path.join(os.getcwd(), os.pardir)
  return os.path.abspath(relative_parent)

print(parent_directory())