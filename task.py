import random

# rand_int = random.randint(1, 10)
# print(rand_int)

# rand_0_1 = random.random()
# print(rand_0_1)

# random_float = random.uniform(1, 10)
# print(random_float)

# text_rand = random.choice(["Heads", "Tails"])
# print(text_rand)

# rand_num = random.randint(1, 2)
# if rand_num == 1:
#     print("Heads")
# else:
#     print("Tails")


# list_a = ['h', 1]
# list_a.extend(['b', 3])
# print(list_a)

# list_pop = list_a.pop(2)
# print(list_pop)
# print(list_a)

# friends = ["ali", "helen", "tim", "kat", "david"]
# #random_pay = friends[random.randint(0, len(friends) -1)]
# random_pay = random.choice(friends)
# print(random_pay)

# your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

# computer_choice = random.randint(0, 2)
# if your_choice == computer_choice:
#     print(f"computer choice: {computer_choice}")
#     print("you Win")
# else:
#     print(f"computer choice: {computer_choice}")
#     print("you lose")


# list_num = [1, 4, 2, 1]
# total_list = sum([1, 2])
# print(total_list)

#print(max(list_num))

# max_score = 0
# for score in list_num:
#     if max_score < score:
#         max_score = score
# print(max_score)

# total = 0
# for score in range(1, 101):
#     total += score
# print(total)


# word_list = ["aardvark", "baboon", "camel"]

# chosen_word = random.choice(word_list)
# print(chosen_word)

# placeholder = ""
# for i in range(len(chosen_word)):
#     placeholder += "_"

# correct_letters = []

# game_over = False
# while not game_over:
#     guess = input("Guess a letter: ").lower()
#     display = ""

#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(letter)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"

#     print(display)

#     if "_" not in display:
#         game_over = True
#         print("You win")

# alphabet = []

# def encrypt(original_text: str, shift_amount: int):
#     shift_text = ""
#     for letter in original_text:
#         position = alphabet.index(letter)
#         next_position = position + shift_amount
#         next_position = next_position % len(alphabet)
#         shift_text += alphabet[next_position]


# flag = True
# bidders = {}
# while flag:
#     name = input("What is your name: ")
#     bid = int(input("What's your bid?: $"))
#     more_bid = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
#     bidders[name] = bid
#     if more_bid != 'yes':
#         max_name = ""
#         max_bid = 0
#         for key, value in bidders.items():
#             if value >= max_bid:
#                 max_bid = value
#                 max_name = key
#         print(f"The winner is {max_name} with a bid of {max_bid}")
#         flag = False
    



# def game():
#     print("I'm thinking of a number between 1 and 100.")
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

#     choose_number = random.randint(1, 101)

#     if level == "hard":
#         lives = 5
#     else:
#         lives = 10
#     result = 0
#     while lives > 0:
#         print(f"You have {lives} attempts remaining to guess the number.")
#         guess_number = int(input("Make a guess: "))
#         lives -= 1
#         if guess_number == choose_number:
#             result = 1
#             break
#         elif guess_number < choose_number:
#             print("Two low!")
#         else:
#             print("Two high.")
#     if result == 0:
#         print("You loss")
#     else:
#         print("You win")
    

# game()



# with open("requirements.txt") as file:
#     contents = file.read()
#     print(contents)




# from enum import Enum

# class TrafficLight(Enum):
#   RED = 'Stop'
#   YELLOW = 'Caution'
#   GREEN = 'Go'

# def traffic_action(light):
#   if light == TrafficLight.RED:
#     return "Stop your car."
#   elif light == TrafficLight.YELLOW:
#     return "Prepare to stop."
#   elif light == TrafficLight.GREEN:
#     return "You can go."

# # Example usage
# current_light = TrafficLight.RED
# print(traffic_action(current_light))


import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        print("bye")
    return wrapper_function

@delay_decorator
def say_hi():
    print("Hi you!")

say_hi()