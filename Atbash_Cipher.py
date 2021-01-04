{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Atbash Cipher",
      "provenance": [],
      "authorship_tag": "ABX9TyNogwt/6S8+JW3LTkzHg7yL",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/aryaninamdar/Cryptography/blob/main/Atbash_Cipher.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jc3vhrmE8LAL"
      },
      "source": [
        "# Atbash Cipher: Takes each letter from original word and replaces it with the letter in a flipped list of the alphabet that corresponds to the original letter's position in the original alphabet list\n",
        "def Atbash_Cipher():\n",
        "  print(\"ATBASH CIPHER\")\n",
        "  # original alphabet list\n",
        "  alphabet_list = [\"a\", \"b\", \"c\", \"d\", \"e\", \"f\", \"g\", \"h\", \"i\", \"j\", \"k\", \"l\", \"m\", \"n\", \"o\", \"p\", \"q\", \"r\", \"s\", \"t\", \"u\", \"v\", \"w\", \"x\", \"y\", \"z\"]\n",
        "  # reversed alphabet list\n",
        "  reversed_alphabet_list = []\n",
        "  for x in reversed(alphabet_list):\n",
        "    # append letters in reverse order to new reversed list\n",
        "    reversed_alphabet_list.append(x)\n",
        "\n",
        "  # take input from the user\n",
        "  word = input(\"Enter a word/phrase to be encrypted with the Atbash Cipher: \")\n",
        "  # iterate through every letter in the word\n",
        "  encrypted_word_list = []\n",
        "  for letter in word:\n",
        "    # if there is a space\n",
        "    if (letter == \" \"):\n",
        "      # append space to new word list\n",
        "      encrypted_word_list.append(\" \")\n",
        "    # if lowercase version of letter is present in the alphabet_list\n",
        "    if (letter.lower() in alphabet_list):\n",
        "      # assign the index of the lowercase version of the letter in the list to a variable called letter_index\n",
        "      letter_index = alphabet_list.index(letter.lower())\n",
        "      # create variable corresponding_letter which equals the letter in the reversed_alphabet_list which has the same index as the original letter in the original list\n",
        "      corresponding_letter = reversed_alphabet_list[letter_index]\n",
        "      # if letter is uppercase\n",
        "      if (letter.isupper() == True):\n",
        "        # append the uppercase leter to list by using .upper()\n",
        "        encrypted_word_list.append(corresponding_letter.upper())\n",
        "      else:\n",
        "        # append lowercase letter\n",
        "        encrypted_word_list.append(corresponding_letter)\n",
        "\n",
        "  # convert the new word list into a string\n",
        "  encrypted_word = ''.join([str(elem) for elem in encrypted_word_list])\n",
        "  # handle exception of no inoput or integer input\n",
        "  if (encrypted_word == \"\"):\n",
        "    print(\"No valid encryption can be formed\")\n",
        "  else:\n",
        "    print(\"The encrypted word/phrase is: \")\n",
        "    print(encrypted_word)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}