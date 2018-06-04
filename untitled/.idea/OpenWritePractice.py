# A file is being created with open. If file is already present, it will be overwritten
with open("/Users/johnyorangeseed/Documents/PythonWrite.txt", "w") as File1:
    # Writing some data into the file
    File1.write("this is line #1\n")

    # During the second run, this line is written:
    File1.write("This is line #2\n")

print(File1.closed)

List1 = ["This is line A\n", "This is line B\n", "This is line C\n"]

# in 'a' APPEND MODE, new text is added to existing file and does not overwrite

with open("/Users/johnyorangeseed/Documents/PythonWrite.txt", "a") as File2:
    for line in List1:
        File2.write(line)











