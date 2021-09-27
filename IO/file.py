#Write to a new file

with open('temp_file', 'w') as file:
    file.write("Hello world")

#Read from a file
with open('temp_file', 'r') as file:
    for line in file:
        print(line)

