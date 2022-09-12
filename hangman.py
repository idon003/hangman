from details import words, pict, letters
import random

def random_word(words):
    return words[random.randint(0, len(words)-1)]

print('1. Cars\n2. Games \n3. Footballers\n4.Animals')
ind = int(input('Choose 1/2/3/4\n > '))


choosen_word = random_word(words[ind])
print(choosen_word)


def print_hang(chances):
    print (pict[8-int(chances)])



def letters_show(ch):
    if ch in letters:
        letters.remove(ch)
    print(*letters)

def hidden(encrypted, ch):
    res = False
    for i in range(len(choosen_word)):
        if choosen_word[i] == ch.upper() or choosen_word[i] == ch.lower():
            encrypted[i] = choosen_word[i]
            res = True
    print(*encrypted)
    return encrypted, res

def main(secreted,count):
    print('Enter any letter that is shown above: ')
    ch = input("> ")
    if ch == 'break':
        exit(0)
    
    if ch.upper() not in letters:
        main(secreted,count)
    secreted, check = hidden(secreted, ch)
    
    if '*' not in secreted:
        input("You win!")
        exit(0)
    
    if not check:
        count -= 1
        print_hang(count)
        if count == 0:
            input("You lose!")
            print(f'The word was {choosen_word}')
            exit(0)
    letters_show(ch.upper())
    
    main(secreted,count)


secreted = ['*' for i in range(len(choosen_word))]
print(*letters)
print(*secreted)
main(secreted,9)