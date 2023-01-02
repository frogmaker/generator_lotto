import random


def choose_random_numbers(amount, total_amount):
    lotto = []
    while len(lotto) < amount:
        luck = random.choice([num for num in range(1, total_amount + 1)])
        lotto.append(luck)
        if len(lotto) > 1:
            for i in range((len(lotto)-1)):
                if lotto[i] == luck:
                    lotto.pop()
    lotto.sort()
    print("Wyniki Lotto: ", lotto)


print("Generator lotto")
print()

on: bool = True
while on:
    print(">>>Wprowadź parametry gry<<<")
    print()
    amount = int(input("Liczba losowanych cyfr: "))
    total_amount = int(input("Pula dostępnych liczb: "))
    print()
    if amount > total_amount:
        print("Wprowadzono błędne dane")
        print()
    else:
        choose_random_numbers(amount, total_amount)
        print()
        again = input("Czy powtórzyć?: (y/N)")
        if again == 'y' or again == 'Y':
            continue
        else:
            on: bool = False
