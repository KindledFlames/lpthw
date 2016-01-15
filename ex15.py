#imports argv module from sys
from sys import argv

#argv variables
script, filename = argv

#opens the file
txt = open(filename)

#prints the file name
print "Here's your file %r:" % filename
#prints the file's contents
print txt.read()
#closes the file
txt.close()

#prints text
print "I'll also ask you to type it again:"
#raw_input
file_again = raw_input("> ")

#opens file
txt_again = open(file_again)

#prints file contents
print txt_again.read()
#closes file
txt_again.close()
