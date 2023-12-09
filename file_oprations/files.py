import os


# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open("names.txt", "r")
#print(f.read())
#print(f.readline())


for x in f:
    print(x)

f.close()

try:
    f = open("name_list.txt", "r")
    print(f.read())

except:
    print("The file doesn't exists")

finally:
    f.close()


# append - create the file of it doesn't exist
f = open("name_list.txt", "a")
f.write("\nNdubueze")
f.close()

f = open("name_list.txt")
print(f.read())
f.close()

# Write (overwrite)
f = open("contxt.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("contxt.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing, creates the file if it doesn't exist
f = open("names_list.txt", "w")
f.close()

# Create the specified file, but returns an error if the file already exist
if not os.path.exists("king.txt"):
    f = open("king.txt", "x")
    f.close()


# Delete a file

# avoid an error if it doesn't exist
if os.path.exists("context.txt"):
    os.remove("context.txt")
    print("file deleted")
else:
    print("The file does not exist")


with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)