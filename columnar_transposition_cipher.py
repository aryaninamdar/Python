# -*- coding: utf-8 -*-
"""Columnar Transposition Cipher

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zUsl4zkDKOkoV1OnuoriZtJcIGGCmg20
"""

import sys

# Columnar Transposition Cipher: Takes in a key word input and then the inputted word's letters are arranged in collumns, each collumn represention one of the key word's letters. 
# Then the keyword's letters are put in alphabetical order, and the new encrypted message is read from collumn to collumn.
def Columnar_Transposition_Cipher():
  print("\n\nCOLUMNAR TRANSPOSITION CIPHER")
  # get key word from user
  key_word = input("Enter the key word for the Columnar Transposition Cipher: ")
  # put all of its letters into a list
  key_word_list = []
  for letter in key_word:
    key_word_list.append(letter)

  # detect no key word input
  if (key_word_list == []):
    sys.exit("No valid encryption can be formed")

  # get word from user
  word = input("Enter a word/phrase to be encrypted with the Columnar Transposition Cipher: ")
  # put all of its letters in a list
  word_list = []
  for letter in word:
    word_list.append(letter)
    # remove all spaces from the word list
    if (letter == " "):
        word_list.remove(letter)
  
  # detect no word input
  if (word_list == []):
    print("No valid encryption can be formed")

  # split word list into separate rows, each row being the length of the key word
  rows = []
  x = 0
  y = len(word_list)
  for i in range(x,y,len(key_word_list)):
    # append each row to the encrypted word list
    x = i
    row = word_list[x:x+len(key_word_list)]
    # sort each row by using the optimal alphabetically organized key word list as a reference
    sorted_row = [x for _,x in sorted(zip(key_word_list,row))]
    # fill each unfilled row with leading spaces
    if(len(sorted_row) < 5):
      for i in range(5 - len(sorted_row)):
        sorted_row.append('')
    rows.append(sorted_row)
    
  # zip the rows (each row nested within) to form a collumn
  collumns = []
  collumn = list(zip(*rows)) # work on this
  collumns.append(collumn)
  
  # encrypted word list is the final list containing the encryption
  encrypted_word_list = []
  encrypted_word_list = ''.join([str(elem) for elem in collumns])
  # convert the encrypted word list into one string
  encrypted_word = ''.join((filter(lambda x: x not in ['[', ']', '(', ')', ',', "'", "'", " "], encrypted_word_list)))
  # detect is encrypted word is blank
  if (encrypted_word == ""):
    print("No valid encryption can be formed")
  else:
    print("The encrypted word/phrase is: ")
    print(encrypted_word)