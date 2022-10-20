import hangman_art
import hangman_words
import random

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
game_ended = False

print(hangman_art.logo)
print("Please guess one letter at a time.")
'''
Hint to check if the code is working: 

print(f'The solution is {chosen_word}... You cheater.')
''' 

display = []
for _ in range(word_length):
    display += "_"
  
def guess_a_letter():
  global lives
  global game_ended
  
  while not game_ended:
    guess = input("Guess a letter: ").lower()
      
    if guess in display:
      print(f"You have already guessed {guess}")
      
    for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter
      
    if guess not in chosen_word:
      lives -= 1
      if lives == 0:
        game_ended = True
        print(f"Oof... Looks like you died.\nThe word was {chosen_word}")
    
    print(display)
    print(hangman_art.stages[lives])

    if "_" not in display:
      game_ended = True
      print("Wow! You've managed to not get hung... Yay (?)")


'''
Check guessed letter:

print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
'''

while "_" in display:
  guess_a_letter()