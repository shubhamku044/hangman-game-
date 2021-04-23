import random
word_list = ['ardvark', 'baboon', 'camel', 'apple', 'boy', 'box', 'ball', 'notes', 'keyboard', 'mouse', 'book', 'room', 'python']
life = -1
print("\n")
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
                   
print(logo)
print("\n")
print("\n")
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
def split(word):
    return [char for char in word]
chosen_word = split(random.choice(word_list))
# print(chosen_word)

empty_list = []
for i in range(0, len(chosen_word)):
    empty_list.append("_")

print(empty_list)
print(f"You have {len(empty_list)} chances.")
while True:
    letter = input("Guess the letter: ").lower()

    for i in range(0, len(empty_list)):
        if letter == chosen_word[i]:
            empty_list[i] = letter
        else:
            continue
    print(empty_list)
    if letter in chosen_word:
        print(stages[life])
    else:
        life -= 1
        print(stages[life])
        if life <= -7:
            print("you loose")
            break
    if empty_list == chosen_word:
        print("you win")
        break
    else:
        continue
# if empty_list != chosen_word:
#     print("you loose")



