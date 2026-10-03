import random


#stick figure drawing


stick_figure = [
    """
     _________
     |/      |
     |      
     |     
     |     
     |      
     |
    _|___
    """,
    """
     _________
     |/      |
     |      (_)
     |      
     |      
     |      
     |
    _|___
    """,
    """
     _________
     |/      |
     |      (_)
     |       |
     |      
     |      
     |
    _|___
    """,
    """
     _________
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
    _|___
    """,
    """
     _________
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
    _|___
    """,
    """
     _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___
    """,
    """
     _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___
    """,
    """
     _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___
    """
]


#helper function

def get_random_word():
  with open("hangmanWordList.txt", "r") as file:
    words = file.readlines()
  return random.choice(words).strip()


#define hangman

def hangman():
  word = get_random_word()
  word_letters = list(word)
  guessed_letters = []
  incorrect_guessed = 0

while incorrect_guesses < len(stick_figure):

  display_word = ""

  for letter in word_letters:
    if letter in guessed_letters:
      display_word += letter
    else:
      display_word += "-"

  print(display_word)

  if display_word == word:
    print("Congratulations! You guessed the right word.")
    break

  guess = input("Guess a letter: ").lower()

  if guess.isalpha() and len(guess) == 1:
    if guess in guessed_letters:
      print("You have already guessed that letter. Try another guess.")
    elif guess in word_letters:
      print("That guess was correct!")
      guessed_letters.append(guess)
    else:
      print("You guessed wrong!")
      incorrect_guesses += 1
      print("Tries remaining:", len(stick_figure) - incorrect_guesses)
      print(stick_figure[incorrect_guesses - 1])
      guessed_letters.append(guess)

    if incorrect_guesses == len(stick_figure):
      print("You ran out of tries. The word was: ", word)

  else:
    print("Invalid input. Please enter a single letter.")
hangman()