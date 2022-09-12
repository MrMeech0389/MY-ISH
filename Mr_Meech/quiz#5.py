NameOfStudent = input("What is your name student?")
History = int(input("What is your History grade?"))
Math = int(input("what is your Math score?"))
Science = int(input("what is your Science School?"))
print(f"{NameOfStudent}\'s average is {(History+Math+Science)/3}")


f = open("calculated_average.txt", "w")
f.write(f"{NameOfStudent}\'s average is {(History+Math+Science)/3}")
f.close()
