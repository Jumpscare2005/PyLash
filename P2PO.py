import time
import random
prompts1 = ['What defeats rock, paper AND scissors?','What the US president counts at night instead of sheep','Rename the capital of France','Name a candle scent designed specifically for Kim Kardashian']
prompts2 = ['Who the warlocks Patron really is','Why the DM is smiling','Your fish are bored! You should put a <BLANK> in their tank to amuse them.','What a statue on Easter Island might say when erected for the first time','Everyone knows that monkeys hate <BLANK>','Jesus REAL last words']
print ('PYLASH')
print(' ')
print ('How Many Players?')
print(' ')
pCount = input()
print(' ')

if pCount == '2':
    print ('5')
    print(' ')
    time.sleep(1)
    print ('4')
    print(' ')
    time.sleep(1)
    print ('3')
    print(' ')
    time.sleep(1)
    print ('2')
    print(' ')
    time.sleep(1)
    print ('1')
    print(' ')
    time.sleep(1)
    print ('Go!!!')
    print(' ')
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    time.sleep(0.3)
    prompt1 = random.choice(prompts1)
    prompt2 = random.choice(prompts2)
    scoreP1=0
    scoreP2=0
    print (prompt1)
    print(' ')
    p1c1 = input()
    print(' ')
    print (prompt2)
    print(' ')
    p1c2 = input()
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    print (prompt2)
    print(' ')
    p2c1 = input()
    print(' ')
    print (prompt1)
    print(' ')
    p2c2 = input()
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    #Prompt 1 Decisions
    print (prompt1)
    ordertt = [1,2]
    order1 = random.choice(ordertt)
    if order1 == 1:
        print(' ')
        print('||',p1c1,'||  ||',p2c2,'||')
        print(' ')
        print('P1')
        print(' ')
        choiceP1R1 = input()
        print(' ')
        print('P2')
        print(' ')
        choiceP2R1 = input()
        print(' ')
        if choiceP1R1 == '1':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
        elif choiceP1R1 == '2':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')
        if choiceP2R1 == '1':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
        elif choiceP2R1 == '2':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')
    if order1 == 2:
        print(' ')
        print('||',p2c2,'||  ||',p1c1,'||')
        print(' ')
        print('P1')
        print(' ')
        choiceP1R1 = input()
        print(' ')
        print('P2')
        print(' ')
        choiceP2R1 = input()
        print(' ')
        if choiceP1R1 == '2':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
        elif choiceP1R1 == '1':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')
        if choiceP2R1 == '2':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
        elif choiceP2R1 == '1':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')    
    time.sleep(5) 
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    print (prompt2)
    orderT = [1,2]
    order2 = random.choice(orderT)
    if order2 == 1:
        print(' ')
        print('||',p1c1,'||  ||',p2c2,'||')
        print(' ')
        print('P1')
        print(' ')
        choiceP1R1 = input()
        print(' ')
        print('P2')
        print(' ')
        choiceP2R1 = input()
        print(' ')
        if choiceP1R1 == '1':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
        elif choiceP1R1 == '2':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')
        if choiceP2R1 == '1':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
        elif choiceP2R1 == '2':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')
    if order2 == 2:
        print(' ')
        print('||',p2c2,'||  ||',p1c1,'||')
        print(' ')
        print('P1')
        print(' ')
        choiceP1R1 = input()
        print(' ')
        print('P2')
        print(' ')
        choiceP2R1 = input()
        print(' ')
        if choiceP1R1 == '2':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
        elif choiceP1R1 == '1':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')
        if choiceP2R1 == '2':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
        elif choiceP2R1 == '1':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')    
    time.sleep(5)
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    #Score Visualizer
    if scoreP1 > scoreP2:
        print ('Player One Wins With',scoreP1,'Points')
    elif scoreP1 < scoreP2:
        print ('Player Two Wins With',scoreP2,'Points')
    elif scoreP1 == scoreP2:
        print ('Tie')
    else:
        print ('error')