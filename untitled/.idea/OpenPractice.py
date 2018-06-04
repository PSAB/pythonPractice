# When using open, use the keyword 'with' before 'open', since it is good practice and automatically c
# closes the file after reading it

with open("/Users/johnyorangeseed/Documents/Raven.txt", "r") as File1: # File1 acts as the file object

    file_content = File1.read() #Stores the content of File1 in file_content variable

    print("first line?:", file_content, "\n") # file_content is a string

    print(type(file_content))



print(file_content)

print("File is closed:", File1.closed) # Return boolean value; Check if the file is closed?

print("\n\n\n") # Some Spacing

with open("/Users/johnyorangeseed/Documents/Raven.txt", "r") as File1Second:
    # The readlines method gets each line from the text file and stores it in a list
    # each element in the list is a line of the text file

    file_content = File1Second.readlines(1)
    print("Specified file content:", file_content)

    print("File status:",File1Second.closed)
print("File status", File1Second.closed) # When 'with us used, the file closes when the loop closes

with open("/Users/johnyorangeseed/Documents/Raven.txt", "r") as File1Third:
    first_line = File1Third.readline() # read the file line by line using readline() function
    print("backsass", first_line)
    second_line = File1Third.readline()
    print("lacksass", second_line)






































