import hashlib
import random
from zxcvbn import zxcvbn

def main():
    story = input("Tell us your story, worries, secrets... Or just your name. ")
    number = text_to_number(story)
    print(f"\nThis is your unique code... {number}. Your story has a 6 digit code that no story has. You can use this code in any way you want.")
    create_password(story, number)

def create_password(story, number):
    ch = input("\nIf you want me to generate a strong password with your code just for you, write Y: ")
    while ch.lower() == "y":
        passw = some_letters(story)
        password = new_password(passw, number)
        password_str = ''.join(password).capitalize()
        print(f"\n{password_str}")
        result = zxcvbn(password_str)
        print(f"\nEstimated time to crack password: {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}")
        while True:
            chh = input("\nWould you like a new password with your same unique code? Write Y or N: ")
            if chh.lower() == "y":
                break
            elif chh.lower() == "n":
                ch = ""
                break
            else:
                print("Invalid input. Please try again.")
    print("Goodbye!")


def text_to_number(story):
    hash_object = hashlib.sha256(story.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    number = int(hex_dig, 16) % 1000000
    return number

def some_letters(story):
    new_list = list(filter(lambda x: not x.isspace(), story))
    passw = ''
    for i in range(3):
        letter = random.choice(new_list)
        passw += letter
        new_list.remove(letter)
    return passw

def new_password(passw, number):
    password = []
    password.append(passw)
    password.append(str(number))
    characters = ["!", "*", "-", "_", "."]
    password.append(random.choice(characters))
    password.append(random.choice(characters))
    password.append(random.choice(characters))
    password.append(random.choice(characters))
    return password

if __name__ == "__main__":
    main()