import os

# Task 1
a =  "AAA BBB CCC DDD FFFF GGG"
b = a.split()
print(b)

final_list = b.reverse()
print(b)
# We have string type  - "AAA BBB CCC DDD FFFF GGG".
# - break it by words
# - sort words in reverse order
# - translate this task in english

#Task 2
def strange_task(x):
  x = str(x)
  if len(x) == 6:
      print(x)
  elif len(x) > 6:
      print("number muast be not bigger then 6 digits")
  elif len(x) == 5:
      print("00000" + str(x))
  elif  len(x) == 4:
      print("0000" + str(x))
  elif len(x) == 3:
      print("000" + str(x))
  elif len(x) == 2:
      print("0000" + str(x))
  elif len(x) == 1:
      print("00000" + str(x))# я знаю , решение длинное :)

strange_task(66)
strange_task(999)
strange_task(99999999)
"""
We have an digits 1 or 999 - it doesn't really matter - in short - it's just a function variable
- you need to show it in string like "000001" and  "000999"  with given length  and leading zeros at the beginning
- write function
- translate task in english 
"""
#Task 3
#my_file = path("/Phy/22,09,2019test1")
list_a =["Marun-0001-0002.txt", "Merin-0002-0002.txt"]


def check_files(file_name = list_a, folder="/Phy/22,09,2019test1", name_prefix=None):
    for element in os.scandir(folder):
        if element.is_file():
            for i in file_name:
             if element.name == i:
                print("file exist")
        else:
            print("file not exist")
check_files()