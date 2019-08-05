import random


A = "Real_Madrid"
B = "Manchester_United"
C = "Tottenham"
D = "Barcelona"

Real_Madrid = ["S.Ramos(90)", "ISCO(90)", "Asensio(88)", "Benzema(86)", "Modrić(92)"]
Manchester_United = ["de Gea(95)", "Pogba(85)", "Lingard(87)", "Rashford(86)", "Rooney(95)"]
Tottenham = ["Lorris(90)", "Eriksen(92)", "Kane(87)", "Alderweireld(86)", "Lucas(89)"]
Barcelona = ["Messi(93)", "Pique(88)", "Grizmann(88)", "Alba(86)", "Rakitić(85)"]


def pickup(Team1, Team2):

    A = "Real_Madrid"
    B = "Manchester_United"
    C = "Tottenham"
    D = "Barcelona"

    random.randrange(A or B or C or D)
    if Team1 is A:
        print(Team1) and random.randrange(B or C or D)
        if Team2 is B:
            print(Team2)
        if Team2 is C:
            print(Team2)
        if Team2 is D:
            print(Team2)
            return
    elif Team1 is B:
        print(Team1) and random.randrange(A or C or D)
        if Team2 is A:
            print(Team2)
        if Team2 is C:
            print(Team2)
        if Team2 is D:
            print(Team2)
            return
    elif Team1 is C:
        print(Team1) and random.randrange(A or B or D)
        if Team2 is A:
            print(Team2)
        if Team2 is B:
            print(Team2)
        if Team2 is D:
            print(Team2)
            return
    elif Team1 is D:
        print(Team1) and random.randrange(A or B or C)
        if Team2 is A:
            print(Team2)
        if Team2 is B:
            print(Team2)
        if Team2 is C:
            print(Team2)
            return


