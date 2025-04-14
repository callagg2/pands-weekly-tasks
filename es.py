# this file shows how you would open an existing text file
# and search for the occurence of the letter "e"
# and counts the number of "e"

#author: gerry  callaghan


# I want to import this module so i can check if the file exists


# this function accepts in two variables, a name of a file, and a file extension type
def is_valid_file_type(filename, valid_type):
    extension = os.path.splitext(filename)[1] # so the os.path is used to be able to move between directories on a operating system,
    # more on this hee https://www.w3schools.com/python/module_os.asp
    # we covered it in class https://atlantictu-my.sharepoint.com/personal/andrew_beatty_atu_ie/_layouts/15/stream.aspx
    # we needed to split the name of the file from its extension, because we only want the extension (.txt, .mp4,.exe, etc) 
    # so we used 1 meaning the second part of the filename, ie after the fullstop

    if extension == valid_type: # if the extension is equal to the extension type that we passed in
        print("This is a valid file type")
    else:
        print("This is an invalid file type")


def letter_checker(input_file): #this accepts in a file name
    """Count the number of characters in a file"""
    with open(input_file, "rt") as file_to_check: #we open the file as read only and give it a name called file_to_check
        file_to_check.seek(0) #we now initialise our cursor at the start of the file
        file_contents = file_to_check.read() #we create and assign a variable equal to the contents of the file 
        number_of_characters = len(file_contents) # we now count the number of characters in our variable (file contents)
        

    # #check = f.read()
        count = 0 # initialise our count as zero
        current_character = 0 # initialise our cursor as zero
    #  #   print(f"I'm in this section")    
        while current_character < number_of_characters: # while we are not at the end of the list of characters in our file
            letter = file_contents[current_character] # assign the value of a new variable letter the value of the current character where the cursor is
            if letter == "e": # if the variable letter is equal to the letter e
                count = count + 1 # increment our count
                current_character = current_character + 1 # move the cursor ontot the next character
            else:
                current_character = current_character + 1 # move the cursor ontot the next character
    
    return count # return the final count of times the letter was found


# how to parse command line arguments https://stackoverflow.com/questions/1009860/how-can-i-read-and-process-parse-command-line-arguments
#sys.argv is a list that contains all the arguments passed to the script on the command line. 

import sys
external_text_file = sys.argv[1] # use argument 1 because argument 0 will be the python file that we are running, not the external file we want to read in
print(f"The file name that you entered to search for the occurence of 'e' is {external_text_file}")

import os

if os.path.exists(external_text_file):
   # used this https://www.youtube.com/watch?v=FPSKYi5jUG8 to verify the file type
   is_valid_file_type(external_text_file,".txt") # now we send the name of our file and the file extension type to our function to validate
    # if we got to here, we know its a text file, so let's proceed to checking for the letter e
   letter_checker(external_text_file) # so we pass the filename to our function that checks for letter and returns their frequency number
   print(f"The letter 'e' occurs {letter_checker(external_text_file)} times")
else:
    print(f"The file {external_text_file} does not exist.")


# More information realted to searching through files can be found here

# W3schools on files : https://www.w3schools.com/python/python_file_handling.asp
# realpython on file manipulation and the OS module: https://realpython.com/working-with-files-in-python/
# python documentation : https://docs.python.org/3/library/os.html#files-and-directories