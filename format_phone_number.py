# Auth r: Mihir Phatak
# Date: April 07, 2018
# Purpose: Coding Challenge 
# Title : Format Phone Number Problem 2 at : https://gist.github.com/jamalc/0d4b9229ca62d4eb9d424a736c5f75ee
# Program Language : Python3
# Usage : Run as : python format_phone_number.py 

import sys

def format_phone_number(unformatted_string):                                #Function to return formatted string
 temp_string = ''
 formatted_number = ''         
  
 for single_char in unformatted_string:
  if (single_char is not ' ' and not (single_char == '-')):
   temp_string = temp_string + single_char

 new_temp_elements = [] 
 element = ''
 [new_temp_elements.append(temp_string[(i*3):(i*3)+3]) for i in range(len(temp_string)) if(temp_string[(i*3):(i*3)+3] is not '')] #List Comprehension for creating 3 character list


 for iter1, element1 in enumerate(new_temp_elements):                     #Joining the elements with '-'
   formatted_number = formatted_number + '-' +element1

 formatted_number = formatted_number[1:]                                  #Removing - from the beginning

 return(formatted_number)

if __name__ == "__main__":
 input_string  = ' - 0--1234 7 7---5544--00 67 8'                               #Accepting input string arguments
 formatted_string = format_phone_number(input_string)
 print("\nThe formatted output string is : ", formatted_string)              #Prints the Formatted Phone Number
 print("\n")

