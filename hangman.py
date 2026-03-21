import random
with open("words.txt", "r") as f:
    words = f.read().split()

word = random.choice(words).upper()

total_chances = 7
guessed_word = "-" * len(word)

while total_chances != 0:
    
    print("\nWord:", guessed_word)
    letter = input("Guess a letter: ").upper()


    if len(letter) != 1 or not letter.isalpha():
        print("Enter only ONE letter!")
        continue

    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = (
                    guessed_word[:index] + letter + guessed_word[index+1:]
                )

        print("Correct Guess ")

        if guessed_word == word:
            print("\n Congratulations! You won!")
            break

    else:
        total_chances -= 1
        print("Incorrect Guess ")
        print("Remaining Chances:", total_chances)

else:
    print("\n Game Over!")
    print("Correct word was:", word)