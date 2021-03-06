"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open('foo.txt') as foo:
    for bar in foo:
        print(bar, end='')

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# Create the new file
bar = open("bar.txt", "w")
# write to the file
bar.write("This is the first line\n")
bar.write("This is the second line\n")
bar.write("This is the third line\n")
# close the file
bar.close

#print the new files contents
with open('bar.txt') as bar:
    for line in bar:
        print(line, end='')
