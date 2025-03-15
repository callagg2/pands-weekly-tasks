# this file shows how you would open an existing text file
# and search for the occurence of the letter "e"
# and counts the number of "e"

#author: gerry  callaghan


# I want to import this module so i can check if the file exists


def is_valid_file_type(filename, valid_type):
    extension = os.path.splitext(filename)[1]

    if extension == valid_type:
        print("This is a valid file type")
    else:
        print("This is an invalid file type")


def letter_checker(input_file):
    """Count the number of characters in a file"""
    with open(input_file, "rt") as file_to_check:
        file_to_check.seek(0)
        file_contents = file_to_check.read()
        number_of_characters = len(file_contents)
        
    
    # #check = f.read()
        count = 0
        current_character = 0
    #  #   print(f"I'm in this section")    
        while current_character < number_of_characters:
            letter = file_contents[current_character]
            if letter == "e":
                count = count + 1
                current_character = current_character + 1
            else:
                current_character = current_character + 1
    
    return count 

import sys

# how to parse command line arguments https://stackoverflow.com/questions/1009860/how-can-i-read-and-process-parse-command-line-arguments?r=SearchResults&s=1%7C174.7322
# use argument 1 becasue argument 0 will be the python file that we are running, not the external file we want to read in
external_text_file = sys.argv[1]
print(f"The file name that you entered to search for the occurence of 'e' is {external_text_file}")

import os

if os.path.exists(external_text_file):
   # used this https://www.youtube.com/watch?v=FPSKYi5jUG8 to verify the file type
   is_valid_file_type(external_text_file,".txt")


   letter_checker(external_text_file)
   print(f"The letter 'e' occurs {letter_checker(external_text_file)} times")
else:
    print(f"The file {external_text_file} does not exist.")
