import pygame, time, random
pygame.init()
screen = pygame.display.set_mode((1100, 800))
pygame.display.set_caption('Rummy Hand Evaluation')  
WHITE, BLACK, RED, GREEN, BLUE, DARK_GREEN, DARK_RED, MAGENTA, S, SB = (255,255,255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 100, 0), (139, 0, 0), (255, 0, 255), (139, 69, 90), (244, 164, 96)
clock = pygame.time.Clock()

def image_converter(cards, x, y):
    i = 0
    while i < len(cards):
        if cards[i] == [1, 'C']: screen.blit(pygame.image.load('images/clubs-a-75.png'), (x, y))
        elif cards[i] == [2, 'C']: screen.blit(pygame.image.load('images/clubs-2-75.png'), (x, y))
        elif cards[i] == [3, 'C']: screen.blit(pygame.image.load('images/clubs-3-75.png'), (x, y))
        elif cards[i] == [4, 'C']: screen.blit(pygame.image.load('images/clubs-4-75.png'), (x, y))
        elif cards[i] == [5, 'C']: screen.blit(pygame.image.load('images/clubs-5-75.png'), (x, y))
        elif cards[i] == [6, 'C']: screen.blit(pygame.image.load('images/clubs-6-75.png'), (x, y))
        elif cards[i] == [7, 'C']: screen.blit(pygame.image.load('images/clubs-7-75.png'), (x, y))
        elif cards[i] == [8, 'C']: screen.blit(pygame.image.load('images/clubs-8-75.png'), (x, y))
        elif cards[i] == [9, 'C']: screen.blit(pygame.image.load('images/clubs-9-75.png'), (x, y))
        elif cards[i] == [10, 'C']: screen.blit(pygame.image.load('images/clubs-10-75.png'), (x, y))
        elif cards[i] == [11, 'C']: screen.blit(pygame.image.load('images/clubs-j-75.png'), (x, y))
        elif cards[i] == [12, 'C']: screen.blit(pygame.image.load('images/clubs-q-75.png'), (x, y))
        elif cards[i] == [13, 'C']: screen.blit(pygame.image.load('images/clubs-k-75.png'), (x, y))
        elif cards[i] == [1, 'D']: screen.blit(pygame.image.load('images/diamonds-a-75.png'), (x, y))
        elif cards[i] == [2, 'D']: screen.blit(pygame.image.load('images/diamonds-2-75.png'), (x, y))
        elif cards[i] == [3, 'D']: screen.blit(pygame.image.load('images/diamonds-3-75.png'), (x, y))
        elif cards[i] == [4, 'D']: screen.blit(pygame.image.load('images/diamonds-4-75.png'), (x, y))
        elif cards[i] == [5, 'D']: screen.blit(pygame.image.load('images/diamonds-5-75.png'), (x, y))
        elif cards[i] == [6, 'D']: screen.blit(pygame.image.load('images/diamonds-6-75.png'), (x, y))
        elif cards[i] == [7, 'D']: screen.blit(pygame.image.load('images/diamonds-7-75.png'), (x, y))
        elif cards[i] == [8, 'D']: screen.blit(pygame.image.load('images/diamonds-8-75.png'), (x, y))
        elif cards[i] == [9, 'D']: screen.blit(pygame.image.load('images/diamonds-9-75.png'), (x, y))
        elif cards[i] == [10, 'D']: screen.blit(pygame.image.load('images/diamonds-10-75.png'), (x, y))
        elif cards[i] == [11, 'D']: screen.blit(pygame.image.load('images/diamonds-j-75.png'), (x, y))
        elif cards[i] == [12, 'D']: screen.blit(pygame.image.load('images/diamonds-q-75.png'), (x, y))
        elif cards[i] == [13, 'D']: screen.blit(pygame.image.load('images/diamonds-k-75.png'), (x, y))
        elif cards[i] == [1, 'H']: screen.blit(pygame.image.load('images/hearts-a-75.png'), (x, y))
        elif cards[i] == [2, 'H']: screen.blit(pygame.image.load('images/hearts-2-75.png'), (x, y))
        elif cards[i] == [3, 'H']: screen.blit(pygame.image.load('images/hearts-3-75.png'), (x, y))
        elif cards[i] == [4, 'H']: screen.blit(pygame.image.load('images/hearts-4-75.png'), (x, y))
        elif cards[i] == [5, 'H']: screen.blit(pygame.image.load('images/hearts-5-75.png'), (x, y))
        elif cards[i] == [6, 'H']: screen.blit(pygame.image.load('images/hearts-6-75.png'), (x, y))
        elif cards[i] == [7, 'H']: screen.blit(pygame.image.load('images/hearts-7-75.png'), (x, y))
        elif cards[i] == [8, 'H']: screen.blit(pygame.image.load('images/hearts-8-75.png'), (x, y))
        elif cards[i] == [9, 'H']: screen.blit(pygame.image.load('images/hearts-9-75.png'), (x, y))
        elif cards[i] == [10, 'H']: screen.blit(pygame.image.load('images/hearts-10-75.png'), (x, y))
        elif cards[i] == [11, 'H']: screen.blit(pygame.image.load('images/hearts-j-75.png'), (x, y))
        elif cards[i] == [12, 'H']: screen.blit(pygame.image.load('images/hearts-q-75.png'), (x, y))
        elif cards[i] == [13, 'H']: screen.blit(pygame.image.load('images/hearts-k-75.png'), (x, y))
        elif cards[i] == [1, 'S']: screen.blit(pygame.image.load('images/spades-a-75.png'), (x, y))
        elif cards[i] == [2, 'S']: screen.blit(pygame.image.load('images/spades-2-75.png'), (x, y))
        elif cards[i] == [3, 'S']: screen.blit(pygame.image.load('images/spades-3-75.png'), (x, y))
        elif cards[i] == [4, 'S']: screen.blit(pygame.image.load('images/spades-4-75.png'), (x, y))
        elif cards[i] == [5, 'S']: screen.blit(pygame.image.load('images/spades-5-75.png'), (x, y))
        elif cards[i] == [6, 'S']: screen.blit(pygame.image.load('images/spades-6-75.png'), (x, y))
        elif cards[i] == [7, 'S']: screen.blit(pygame.image.load('images/spades-7-75.png'), (x, y))
        elif cards[i] == [8, 'S']: screen.blit(pygame.image.load('images/spades-8-75.png'), (x, y))
        elif cards[i] == [9, 'S']: screen.blit(pygame.image.load('images/spades-9-75.png'), (x, y))
        elif cards[i] == [10, 'S']: screen.blit(pygame.image.load('images/spades-10-75.png'), (x, y))
        elif cards[i] == [11, 'S']: screen.blit(pygame.image.load('images/spades-j-75.png'), (x, y))
        elif cards[i] == [12, 'S']: screen.blit(pygame.image.load('images/spades-q-75.png'), (x, y))
        elif cards[i] == [13, 'S']: screen.blit(pygame.image.load('images/spades-k-75.png'), (x, y))
        i += 1
        x += 50
    pygame.display.flip()
    return()

def deal_cards(cards):
    card_number, x = 0, 200
    while card_number < len(cards):
        screen.blit(pygame.image.load('images/back-red-75-1.png'), (x, 90)) 
        card_number += 1
        x += 50
    pygame.display.flip()
    return()               

def get_cards(make_cards):
    card_number = 0
    import random
    ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    suits = ['C', 'D', 'H', 'S']
    cards = [[rank, suit] for rank in ranks for suit in suits]
    random.shuffle(cards)
    while card_number < 13:
        make_cards.append(random.choice(cards))
        cards.remove(make_cards[card_number])
        card_number += 1

def declare_cards(index):
     if index == 1: screen.blit(pygame.image.load('images/one.png'), (370, 475))
     elif index == 2: screen.blit(pygame.image.load('images/two.png'), (370, 475))
     elif index == 3: screen.blit(pygame.image.load('images/three.png'), (370, 475))
     elif index == 4: screen.blit(pygame.image.load('images/four.png'), (370, 475))
     elif index == 5: screen.blit(pygame.image.load('images/five.png'), (370, 475))
     elif index == 6: screen.blit(pygame.image.load('images/six.png'), (370, 475))
     elif index == 7: screen.blit(pygame.image.load('images/seven.png'), (370, 475))
     elif index == 8: screen.blit(pygame.image.load('images/eight.png'), (370, 475))
     return()
     
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

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def Options_Display(x, y, width, height, colour, courser_colour, comment, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, courser_colour, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "play":
                game_play()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(screen, colour, (x, y, width, height))
    smallText = pygame.font.SysFont("comicsansms", 40)
    textSurf, textRect = text_objects(comment, smallText)
    textRect.center = ( (x + (width / 2)), (y + (height / 2)))
    screen.blit(textSurf, textRect)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(pygame.image.load('images/Screen.png'), [-110, -10])
        Options_Display(150, 350, 200, 100, GREEN, BLUE, "Start", "play")
        Options_Display(150, 500, 200, 100, RED, DARK_RED, "Quit", "quit")
        pygame.display.update()
        clock.tick(15)

def game_play():
    quit_button = pygame.Rect(950, 650, 100, 50)
    home_button = pygame.Rect(50, 650, 100, 50)
    seeCards_button = pygame.Rect(30, 110, 140, 70)
    evaluate_button = pygame.Rect(30, 320, 140, 70)
    playing_cards, Seq_1, Seq_2, Set_1, Set_2 = [], [], [], [], []
    get_cards(playing_cards)
    copy_cards = playing_cards
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
    screen.fill(GREEN)
    screen.blit(pygame.image.load('images/Joker.png'), [0, 0])
    screen.blit(pygame.image.load('images/ppp.png'), [380, 30])
    deal_cards(copy_cards)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()  
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()
                if home_button.collidepoint(mouse_pos):
                    game_intro()
                if seeCards_button.collidepoint(mouse_pos):
                    image_converter(copy_cards, 200, 90)
                if evaluate_button.collidepoint(mouse_pos):
                    image_converter(Seq_1 + Seq_2 + Set_1 + Set_2 + playing_cards, 200, 300)
                    declare_cards(len(playing_cards))
        pygame.draw.rect(screen, RED, quit_button)  
        pygame.draw.rect(screen, RED, home_button) 
        pygame.draw.rect(screen, WHITE, seeCards_button)
        pygame.draw.rect(screen, BLUE, evaluate_button)
        smallText = pygame.font.SysFont("comicsansms", 35)
        textSurf, textRect = text_objects("Quit", smallText)
        textRect.center = (1000, 675)
        screen.blit(textSurf, textRect)
        textSurf, textRect = text_objects("Home", smallText)
        textRect.center = (100, 675)
        screen.blit(textSurf, textRect)
        textSurf, textRect = text_objects("See Cards", smallText)
        textRect.center = (100, 145)
        screen.blit(textSurf, textRect)
        textSurf, textRect = text_objects("Evaluate", smallText)
        textRect.center = (100, 355)
        screen.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    sys.exit

game_intro()
game_play()
pygame.quit()
