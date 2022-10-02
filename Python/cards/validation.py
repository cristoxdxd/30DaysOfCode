def validCard(card):
    card = [int(x) for x in str(card)]
    card = card[::-1]
    for i in range(1, len(card), 2):
        card[i] *= 2
        if card[i] > 9:
            card[i] -= 9
    return sum(card) % 10 == 0

def validModN(card, n):
    card = [int(x) for x in str(card)]
    card = card[::-1]
    for i in range(1, len(card), 2):
        card[i] *= 2
        if card[i] > 9:
            card[i] -= 9
    return sum(card) % n == 0 

def main():
    card = input('Enter a card number: ')
    if validCard(card):
        print('Valid card')
    else:
        print('Invalid card')

main()