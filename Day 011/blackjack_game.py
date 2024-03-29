# Blackjack Game


from art import logo
import random


def show_results():
    global my_cards, computers_cards
    a = sum(my_cards)
    b = sum(computers_cards)
    if a > 21 and b > 21:
        print("both went over")
    elif a > 21:
        print("you went over. opponent win")
    elif b > 21:
        print("opponent went over. You win")
    elif a > b:
        print("You won")
    elif b > a:
        print("You lost")
    elif a == b:
        print("draw game")


def show_output2(a, b):
    print(f"Your final hand score {a}, final score: {sum(a)}")
    print(f"Computer's final hand: {b}, final score {sum(b)}")


def check_11():
    global my_cards, computers_cards

    num = 0
    for i in my_cards:
        if i == 11:
            if sum(my_cards) > 21:
                my_cards[num] = 1
        num += 1

    num = 0
    for i in computers_cards:
        if i == 11:
            if sum(computers_cards) > 21:
                computers_cards[num] = 1
        num += 1
    show_output2(my_cards, computers_cards)


def add_comp_cards():
    global computers_cards, cards
    while sum(computers_cards) <= 17:
        computers_cards.append(random.choice(cards))
    check_11()


def ask_user():
    global my_cards
    run = True
    user = ""
    while run:
        global my_cards, computers_cards
        if sum(my_cards) > 21:
            show_results()
            run = False
        else:
            user = input(f"Type 'y' to get another cars, Type 'n' to pass: ")
        if user == "y":
            add_user_cards(1, my_cards)
            show_output(my_cards, computers_cards)
        elif user == "n":
            run = False
            add_comp_cards()
            show_results()
            break


def show_output(a, b):
    user_sum = sum(a)

    print(f"Your cards: {a}, current score: {user_sum}")
    print(f"Computer's first card: {b[0]}")
    ask_user()


def add_user_cards(n, list_add):
    for i in range(n):
        list_add.append(random.choice(cards))


def calculate():
    global my_cards, computers_cards
    print(logo)
    add_user_cards(2, my_cards)
    add_user_cards(1, computers_cards)
    show_output(my_cards, computers_cards)


r = True
while r:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    my_cards = []
    computers_cards = []
    ask_playgame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if ask_playgame == "y":
        calculate()
    else:
        r = False
