# Author: Mihir Phatak
# Date: April 07, 2018
# Purpose: Simple Coding Challenge Problem 3 at https://gist.github.com/jamalc/0d4b9229ca62d4eb9d424a736c5f75ee
# Title : Minimum Coin Flips Calculation
# Program Language : Python3
# Usage : Run program as python reversing_coins.py 

def solution(coins):
 count0 = coins.count(0)
 count1 = coins.count(1)
 
 if(count0 < count1):
  return count0

 else:
  return count1

if __name__ == "__main__":
 COINS = [1,1,1,1,1,1]
 reversal = solution(COINS) 
 print(reversal)
