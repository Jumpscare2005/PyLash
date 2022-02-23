import time
import random
prompts1 = ['What defeats rock, paper AND scissors?','What the US president counts at night instead of sheep','Rename the capital of France','Name a candle scent designed specifically for Kim Kardashian']
prompts2 = ['Who the warlocks Patron really is','Why the DM is smiling','Your fish are bored! You should put a <BLANK> in their tank to amuse them.','What a statue on Easter Island might say when erected for the first time','Everyone knows that monkeys hate <BLANK>','Jesus REAL last words']
prompts3 = ['The worst thing for an evil witch to turn you into','The Skittles flavor that just missed the cut','Whats actually causing global warming?']
prompts4 = ['My Christian girlfriend broke up with me because she caught me <BLANK>','Damn it! I failed NNN because of <BLANK> again!']
oneOrder = [1,2]
twoOrder = [1,2]
threeOrder = [1,2]
fourOrder = [1,2]
print ('PYLASH')
print(' ')
print('The Rules Of The Game Are Simple!')
time.sleep(0.5)
print(' ')
print('When It Is Your Turn (Indicated By My Beautiful Countdown) Answer Your Prompts With The Funniest Thing You Can Think Of')
print(' ')
print('When It Comes Time To Vote, Use 1 or 2 To Make Your Selection')
print(' ')
print ('Now How Many Players Will Be Joining Us?')
print(' ')
pCount = input()
print(' ')

if pCount == '2':
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    print ("It Is Now Player 1's Turn")
    print(' ')
    time.sleep(1)
    print('5')
    print(' ')
    time.sleep(1)
    print('4')
    print(' ')
    time.sleep(1)
    print('3')
    print(' ')
    time.sleep(1)
    print('2')
    print(' ')
    time.sleep(1)
    print('1')
    print(' ')
    time.sleep(1)
    print('Go!!!')
    print(' ')
    time.sleep(1)
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
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
    print ("It Is Now Player 2's Turn")
    print(' ')
    time.sleep(1)
    print('5')
    print(' ')
    time.sleep(1)
    print('4')
    print(' ')
    time.sleep(1)
    print('3')
    print(' ')
    time.sleep(1)
    print('2')
    print(' ')
    time.sleep(1)
    print('1')
    print(' ')
    time.sleep(1)
    print('Go!!!')
    print(' ')
    time.sleep(1)
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
#Prompt2 Decisions
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
elif pCount == '3':
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    print ("It Is Now Player 1's Turn")
    print(' ')
    time.sleep(1)
    print('5')
    print(' ')
    time.sleep(1)
    print('4')
    print(' ')
    time.sleep(1)
    print('3')
    print(' ')
    time.sleep(1)
    print('2')
    print(' ')
    time.sleep(1)
    print('1')
    print(' ')
    time.sleep(1)
    print('Go!!!')
    print(' ')
    time.sleep(1)
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    prompt1 = random.choice(prompts1)
    prompt2 = random.choice(prompts2)
    prompt3 = random.choice(prompts3)
    scoreP1=0
    scoreP2=0
    scoreP3=0
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
    print ("It Is Now Player 2's Turn")
    print(' ')
    time.sleep(1)
    print('5')
    print(' ')
    time.sleep(1)
    print('4')
    print(' ')
    time.sleep(1)
    print('3')
    print(' ')
    time.sleep(1)
    print('2')
    print(' ')
    time.sleep(1)
    print('1')
    print(' ')
    time.sleep(1)
    print('Go!!!')
    print(' ')
    time.sleep(1)
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    print (prompt2)
    print(' ')
    p2c1 = input()
    print(' ')
    print (prompt3)
    print(' ')
    p2c2 = input()
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    print ("It Is Now Player 3's Turn")
    print(' ')
    time.sleep(1)
    print('5')
    print(' ')
    time.sleep(1)
    print('4')
    print(' ')
    time.sleep(1)
    print('3')
    print(' ')
    time.sleep(1)
    print('2')
    print(' ')
    time.sleep(1)
    print('1')
    print(' ')
    time.sleep(1)
    print('Go!!!')
    print(' ')
    time.sleep(1)
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    print (prompt1)
    print(' ')
    p3c1 = input()
    print(' ')
    print (prompt3)
    print(' ')
    p3c2 = input()
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    #Prompt 1 Decisions
    # Go From Here
    print (prompt1)
    order1 = random.choice(oneOrder)
    if order1 == 1:
        print(' ')
        print('||',p1c1,'||  ||',p3c1,'||')
        print(' ')
        print('P2')
        print(' ')
        choiceP2R1 = input()
        print(' ')
        if choiceP2R1 == '1':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
        elif choiceP2R1 == '2':
            scoreP3 += 100
            print('+100 Points To P3')
            print(' ')
    if order1 == 2:
        print(' ')
        print('||',p3c1,'||  ||',p1c1,'||')
        print(' ')
        print('P2')
        print(' ')
        choiceP2R1 = input()
        print(' ')
        if choiceP2R1 == '1':
            scoreP3 += 100
            print('+100 Points To P3')
            print(' ')
        elif choiceP2R1 == '2':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
    time.sleep(5)
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    #Prompt 2 Decisions
    print(prompt2)
    order2 = random.choice(twoOrder)
    if order2 == 1:
        print(' ')
        print('||',p1c2,'||  ||',p2c1,'||')
        print(' ')
        print('P3')
        print(' ')
        choiceP3R1 = input()
        print(' ')
        if choiceP3R1 == '1':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
        elif choiceP3R1 == '2':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')
    if order2 == 2:
        print(' ')
        print('||',p2c1,'||  ||',p1c2,'||')
        print(' ')
        print('P3')
        print(' ')
        choiceP2R1 = input()
        print(' ')
        if choiceP2R1 == '1':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')
        elif choiceP2R1 == '2':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
    time.sleep(5)
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
#Prompt 3 Decisions
    print(prompt3)
    order3 = random.choice(threeOrder)
    if order3 == 1:
        print(' ')
        print('||',p3c2,'||  ||',p2c2,'||')
        print(' ')
        print('P1')
        print(' ')
        choiceP1R1 = input()
        print(' ')
        if choiceP1R1 == '1':
            scoreP3 += 100
            print('+100 Points To P3')
            print(' ')
        elif choiceP3R1 == '2':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')
    if order3 == 2:
        print(' ')
        print('||',p2c2,'||  ||',p3c2,'||')
        print(' ')
        print('P1')
        print(' ')
        choiceP1R1 = input()
        print(' ')
        if choiceP1R1 == '1':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')
        elif choiceP1R1 == '2':
            scoreP3 += 100
            print('+100 Points To P3')
            print(' ')
    time.sleep(5)
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    #Score Visualizer
    if scoreP1 > scoreP2 and scoreP1 > scoreP3:
        print ('Player One Wins With',scoreP1,'Points')
    elif scoreP1 < scoreP2 and scoreP3 < scoreP2:
        print ('Player Two Wins With',scoreP2,'Points')
    elif scoreP1 < scoreP3 and scoreP2 < scoreP3:
        print ('Player Three Wins With',scoreP3,'Points')
    elif scoreP1 == scoreP2 and scoreP1 == scoreP3 and scoreP2 == scoreP3:
        print ('Tie')
    else:
        print ('error')
elif pCount == '4':
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    print ("It Is Now Player 1's Turn")
    print(' ')
    time.sleep(1)
    print('5')
    print(' ')
    time.sleep(1)
    print('4')
    print(' ')
    time.sleep(1)
    print('3')
    print(' ')
    time.sleep(1)
    print('2')
    print(' ')
    time.sleep(1)
    print('1')
    print(' ')
    time.sleep(1)
    print('Go!!!')
    print(' ')
    time.sleep(1)
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    time.sleep(0.3)
    prompt1 = random.choice(prompts1)
    prompt2 = random.choice(prompts2)
    prompt3 = random.choice(prompts3)
    prompt4 = random.choice(prompts4)
    scoreP1=0
    scoreP2=0
    scoreP3=0
    scoreP4=0
    print (prompt1)
    print(' ')
    p1c1 = input()
    print(' ')
    print (prompt4)
    print(' ')
    p1c2 = input()
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    print ("It Is Now Player 2's Turn")
    print(' ')
    time.sleep(1)
    print('5')
    print(' ')
    time.sleep(1)
    print('4')
    print(' ')
    time.sleep(1)
    print('3')
    print(' ')
    time.sleep(1)
    print('2')
    print(' ')
    time.sleep(1)
    print('1')
    print(' ')
    time.sleep(1)
    print('Go!!!')
    print(' ')
    time.sleep(1)
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    print (prompt2)
    print(' ')
    p2c1 = input()
    print(' ')
    print (prompt3)
    print(' ')
    p2c2 = input()
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    print ("It Is Now Player 3's Turn")
    print(' ')
    time.sleep(1)
    print('5')
    print(' ')
    time.sleep(1)
    print('4')
    print(' ')
    time.sleep(1)
    print('3')
    print(' ')
    time.sleep(1)
    print('2')
    print(' ')
    time.sleep(1)
    print('1')
    print(' ')
    time.sleep(1)
    print('Go!!!')
    print(' ')
    time.sleep(1)
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    print (prompt1)
    print(' ')
    p3c1 = input()
    print(' ')
    print (prompt3)
    print(' ')
    p3c2 = input()
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    print ("It Is Now Player 4's Turn")
    print(' ')
    time.sleep(1)
    print('5')
    print(' ')
    time.sleep(1)
    print('4')
    print(' ')
    time.sleep(1)
    print('3')
    print(' ')
    time.sleep(1)
    print('2')
    print(' ')
    time.sleep(1)
    print('1')
    print(' ')
    time.sleep(1)
    print('Go!!!')
    print(' ')
    time.sleep(1)
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    print (prompt2)
    print(' ')
    p4c1 = input()
    print(' ')
    print (prompt4)
    print(' ')
    p4c2 = input()
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    #Prompt 1 Decisions
    print (prompt1)
    order1 = random.choice(oneOrder)
    if order1 == 1:
        print(' ')
        print('||',p1c1,'||  ||',p3c1,'||')
        print(' ')
        print('P2')
        print(' ')
        choiceP2R1 = input()
        print(' ')
        print('P4')
        print(' ')
        choiceP4R1 = input()
        print(' ')
        if choiceP2R1 == '1':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
        elif choiceP2R1 == '2':
            scoreP3 += 100
            print('+100 Points To P3')
            print(' ')
        print(' ')
        if choiceP4R1 == '1':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
        elif choiceP4R1 == '2':
            scoreP3 += 100
            print('+100 Points To P3')
            print(' ')
    if order1 == 2:
        print(' ')
        print('||',p3c1,'||  ||',p1c1,'||')
        print(' ')
        print('P2')
        print(' ')
        choiceP2R1 = input()
        print(' ')
        print('P4')
        print(' ')
        choiceP4R1 = input()
        print(' ')
        if choiceP2R1 == '1':
            scoreP3 += 100
            print('+100 Points To P3')
            print(' ')
        elif choiceP2R1 == '2':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
        print(' ')
        if choiceP4R1 == '1':
            scoreP3 += 100
            print('+100 Points To P3')
            print(' ')
        elif choiceP4R1 == '2':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
    time.sleep(5)
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    #Prompt 2 Decisions
    print(prompt2)
    order2 = random.choice(twoOrder)
    if order2 == 1:
        print(' ')
        print('||',p4c1,'||  ||',p2c1,'||')
        print(' ')
        print('P1')
        print(' ')
        choiceP1R1 = input()
        print(' ')
        print('P3')
        print(' ')
        choiceP3R1 = input()
        print(' ')
        if choiceP1R1 == '2':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')
        elif choiceP1R1 == '1':
            scoreP4 += 100
            print('+100 Points To P4')
            print(' ')
        print(' ')
        if choiceP3R1 == '2':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')
        elif choiceP3R1 == '1':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
    if order2 == 2:
        print(' ')
        print('||',p2c1,'||  ||',p4c1,'||')
        print(' ')
        print('P1')
        print(' ')
        choiceP1R1 = input()
        print(' ')
        print('P3')
        print(' ')
        choiceP3R1 = input()
        print(' ')
        if choiceP1R1 == '1':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')
        elif choiceP1R1 == '2':
            scoreP4 += 100
            print('+100 Points To P4')
            print(' ')
        if choiceP3R1 == '1':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')
        elif choiceP3R1 == '2':
            scoreP4 += 100
            print('+100 Points To P4')
            print(' ')
    time.sleep(5)
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
#Prompt 3 Decisions
    print(prompt3)
    order3 = random.choice(threeOrder)
    if order3 == 1:
        print(' ')
        print('||',p3c2,'||  ||',p2c2,'||')
        print(' ')
        print('P1')
        print(' ')
        choiceP1R1 = input()
        print(' ')
        print('P4')
        print(' ')
        choiceP4R1 = input()
        print(' ')
        if choiceP1R1 == '1':
            scoreP3 += 100
            print('+100 Points To P3')
            print(' ')
        elif choiceP1R1 == '2':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')
        if choiceP4R1 == '1':
            scoreP3 += 100
            print('+100 Points To P3')
            print(' ')
        elif choiceP4R1 == '2':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')
    if order3 == 2:
        print(' ')
        print('||',p2c2,'||  ||',p3c2,'||')
        print(' ')
        print('P1')
        print(' ')
        choiceP1R1 = input()
        print(' ')
        print('P4')
        print(' ')
        choiceP4R1 = input()
        print(' ')
        if choiceP1R1 == '1':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')
        elif choiceP1R1 == '2':
            scoreP3 += 100
            print('+100 Points To P3')
            print(' ')
        if choiceP4R1 == '1':
            scoreP2 += 100
            print('+100 Points To P2')
            print(' ')
        elif choiceP4R1 == '2':
            scoreP3 += 100
            print('+100 Points To P3')
            print(' ')
    time.sleep(5)
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
#Prompt 4 Decisions
    print(prompt4)
    order4 = random.choice(fourOrder)
    if order4 == 1:
        print(' ')
        print('||',p1c2,'||  ||',p4c2,'||')
        print(' ')
        print('P2')
        print(' ')
        choiceP2R1 = input()
        print(' ')
        print('P3')
        print(' ')
        choiceP3R1 = input()
        print(' ')
        if choiceP2R1 == '1':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
        elif choiceP2R1 == '2':
            scoreP4 += 100
            print('+100 Points To P4')
            print(' ')
        if choiceP3R1 == '1':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
        elif choiceP3R1 == '2':
            scoreP4 += 100
            print('+100 Points To P4')
            print(' ')
    if order4 == 2:
        print(' ')
        print('||',p4c2,'||  ||',p1c2,'||')
        print(' ')
        print('P2')
        print(' ')
        choiceP2R1 = input()
        print(' ')
        print('P3')
        print(' ')
        choiceP3R1 = input()
        print(' ')
        if choiceP2R1 == '2':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
        elif choiceP2R1 == '1':
            scoreP4 += 100
            print('+100 Points To P4')
            print(' ')
        if choiceP3R1 == '2':
            scoreP1 += 100
            print('+100 Points To P1')
            print(' ')
        elif choiceP3R1 == '1':
            scoreP4 += 100
            print('+100 Points To P4')
            print(' ')
    time.sleep(5)
    spacer = 0
    while spacer <= 1:
        print(' ')
        spacer += 0.01
    #Score Visualizer
    if scoreP1 > scoreP2 and scoreP1 > scoreP3 and scoreP1 > scoreP4:
        print ('Player One Wins With',scoreP1,'Points')
    elif scoreP1 < scoreP2 and scoreP3 < scoreP2 and scoreP4 < scoreP2:
        print ('Player Two Wins With',scoreP2,'Points')
    elif scoreP1 < scoreP3 and scoreP2 < scoreP3 and scoreP4 < scoreP3:
        print ('Player Three Wins With',scoreP3,'Points')
    elif scoreP1 < scoreP4 and scoreP2 < scoreP4 and scoreP3 < scoreP4:
        print ('Player Three Wins With',scoreP3,'Points')
    elif scoreP1 == scoreP2 and scoreP1 == scoreP3 and scoreP2 == scoreP3 and scoreP2 == scoreP4:
        print ('Tie')
    else:
        print ('error')
else:
    print ('Either You Have Input An Invalid Game Type Or The Feature Has Not Been Added Yet')
time.sleep(20)
