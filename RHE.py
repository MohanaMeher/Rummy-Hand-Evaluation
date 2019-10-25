def get_cards(make_cards):
    card_number = 0
    import random
    #Assuming 1 as 'A', 11 as 'J', 12 as 'Q', 13 as 'K'
    ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    suits = ['C', 'D', 'H', 'S']
    cards = [[rank, suit] for rank in ranks for suit in suits]
    #Shuffling the cards
    random.shuffle(cards)
    while card_number < 13:
        make_cards.append(random.choice(cards))
        #cards depict the deck of cards remained after distribution
        cards.remove(make_cards[card_number])
        card_number += 1

def Remove_elements(Cards, Set_or_sequence):
    card_number = 0
    while card_number < len(Set_or_sequence):
        if Set_or_sequence[card_number] in Cards:
            Cards.remove(Set_or_sequence[card_number])
        card_number += 1
    return()


def is_seq(order, cards, Sequence):
    i = 0
    while i < len(cards) + 1 - order:
        j, k, m, count = i, i, 0, 0
        while m < order - 1:
            if cards[j+1][0] - cards[j][0] == 1 and cards[j+1][1] == cards[j][1]:
                count += 1
            j += 1
            m += 1
        if count == order - 1:
            while k < i + order:
                Sequence.append(cards[k]) 
                k += 1
            Remove_elements(cards, Sequence)
            break
        i += 1
    return()


def order4_incomplete_seq(cards, sequence):
    card_number = 0
    while card_number < len(cards) - 2 and len(sequence) == 0:
        if cards[card_number][0] == cards[card_number+1][0]-1 == cards[card_number+2][0]-3 or cards[card_number][0] == cards[card_number+1][0]-2 == cards[card_number+2][0]-3 and cards[card_number][1] == cards[card_number+1][1] == cards[card_number+2][1]:
            sequence.extend([cards[card_number], cards[card_number+1], cards[card_number+2]])
        card_number += 1
    Remove_elements(cards, sequence)
    return()


def order3_incomplete_seq(Cards, sequence):
    j = 0
    if len(sequence) == 0:
        is_seq(2, Cards, sequence)
    while j < len(Cards) - 1 and len(sequence) == 0:
        if Cards[j+1][0] - Cards[j][0] == 2 and Cards[j+1][1] == Cards[j][1]:
            sequence.extend([Cards[j], Cards[j+1]])
        j += 1        
    Remove_elements(Cards, sequence)
    return()


def check_seq_4(cards, sequence):
    if len(sequence) == 0:
        is_seq(4, cards, sequence)
    if len(sequence) == 0:
        order4_incomplete_seq(cards, sequence)
    return()


def check_seq_3(cards, sequence):
    if len(sequence) == 0:
        is_seq(3, cards, sequence)
    if len(sequence) == 0:
        order3_incomplete_seq(cards, sequence)
    return()


def is_set(Cards, Set):
    order = 4
    while len(Set) == 0 and order > 1:
        i = 0
        while i < len(Cards) + 1 - order:
            j, k, m, count = i, i, 0, 0
            while m < order - 1:
                if Cards[j + 1][0] == Cards[j][0]:
                    count += 1
                j += 1
                m += 1
            if count == order - 1:
                while k < i + order:
                    Set.append(Cards[k])
                    k += 1
                Remove_elements(Cards, Set)
                break
            i += 1
        order -= 1
    return()


def single_card(cards, Set):
    if len(Set) == 0:
        Set.append(cards[0])
        Remove_elements(cards, Set)
    return()


playing_cards, Seq_1, Seq_2, Set_1, Set_2 = [], [], [], [], []
get_cards(playing_cards), print("\n", "Randomly Selected Cards:", "\n\n",  playing_cards, "\n")
from operator import itemgetter
playing_cards = (sorted(playing_cards, key = itemgetter(1)))
playing_cards = (sorted(playing_cards, key = itemgetter(0))) 
playing_cards = (sorted(playing_cards, key = itemgetter(1)))
check_seq_4(playing_cards, Seq_1), check_seq_3(playing_cards, Seq_1), check_seq_3(playing_cards, Seq_2), is_seq(3, playing_cards, Set_1)
playing_cards = (sorted(playing_cards, key = itemgetter(0)))
is_set(playing_cards, Set_1)
playing_cards = (sorted(playing_cards, key = itemgetter(1)))
order3_incomplete_seq(playing_cards, Set_1)
is_seq(3, playing_cards, Set_2)
playing_cards = (sorted(playing_cards, key = itemgetter(0)))
is_set(playing_cards, Set_2)
playing_cards = (sorted(playing_cards, key = itemgetter(1)))
order3_incomplete_seq(playing_cards, Set_2)
single_card(playing_cards, Set_1), single_card(playing_cards, Set_2)
print("\n", "Sorted Cards:", "\n\n",  Seq_1 + Seq_2 + Set_1 + Set_2 + playing_cards, "\n\n", "You need", len(playing_cards), "cards to win the game.", "\n")
