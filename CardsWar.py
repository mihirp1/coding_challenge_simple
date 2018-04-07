# Author: Mihir Phatak
# Date: April 07, 2018
# Purpose: Coding Challenge 
# Title : Cards War Problem 1 at : https://gist.github.com/jamalc/0d4b9229ca62d4eb9d424a736c5f75ee
# Program Language : Python3
# Usage : Run as : python CardsWar.py Alice_Cards Bob_Cards where Alice_Cards and Bob_Cards are strings 

import sys

def solution(CARDS_A, CARDS_B):

 hierarchy_deck = {'T':10,'J':11,'Q':12,'K':13,'A':14} #Creation of Hierarchy for values not between 2 and 9, both inclusive

 paired_l = list(zip(cardsA, cardsB))                  #Combining and pairing both strings 
 alice_count = 0
 for iter1, element in enumerate(paired_l):            #Looping over paired list while classifying each card as an integer or digit
  if(element[0].isdigit()):
   CA = int(element[0]) 
  else:
   CA = hierarchy_deck[element[0]]

  if(element[1].isdigit()):
   CB = int(element[1])
  else:
   CB = hierarchy_deck[element[1]]
  
  if(CA  > CB):                                       #Checking if wins by Alice are greater than winds by Bob and capturing in counter
   alice_count += 1                                              

 return (alice_count)
 
if __name__ == "__main__":
 cardsA = sys.argv[1]                                  #Accepting two CommandLine arguments in the form of two sets of strings as packs of cards
 cardsB = sys.argv[2]
 Alice_Count = solution(cardsA, cardsB)
 print("\nAlice will win %d times.\n" % Alice_Count)   #Prints the Result of Wins by Alice
