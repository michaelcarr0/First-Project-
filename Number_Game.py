import random
def main():
    number_guess_game()
def number_guess_game():
    count = 0
    random_number = random.randint(1,100)
    guess_number = int(input("What is the number? "))
    while guess_number != random_number:
        if count > 10:
            print("Nice Try! Too many Attempts.")
            exit()
        else:
            print("Attempts Remaining: " + str(10 - count))
        count = count + 1
        if guess_number > random_number:
            print("Too High!")
        elif guess_number < random_number:
            print("Too Low!")
        guess_number = int(input("What is the number? "))
    print("You Win!")
    print("You had " + str(count) + " attempts")
main()