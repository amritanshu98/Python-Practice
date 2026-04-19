# Accept a sequence of lines as input and print each line with all characters in uppercase. Stop reading when an empty line is entered

# input = "hello world, this is python program"

while True:
    line = input("Enter Srting: ")
    if line =="":
        break

    else: 
        print(line.upper())


