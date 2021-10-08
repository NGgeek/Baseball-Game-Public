import pandas as pd
import sys
import random


def dice(inFront, inBack, result):
    inFront = int(inFront)
    inBack = int(inBack)
    diceTotal = 0
    diceResults = []

    for x in range(int(inFront)):
        dice_roll = random.randint(1, inBack)
        diceTotal += dice_roll
        diceResults.append(dice_roll)
    if result == "DT":
        return diceTotal
    if result == "DR":
        return diceResults
    else:
        return diceTotal, diceResults


team_2_data = pd.read_csv('team2.csv')
team_1_data = pd.read_csv('team1.csv')

print("Team 1 looks like this: ")
print(team_1_data)
print()
a = input("Does this look good? answer with Y/n : ")
if a != 'Y':
    print("Go to file 'team1.csv' and fix it")
    print("Quiting now...")
    sys.exit()


print("Team 2 looks like this: ")
print(team_2_data)
print()
a = input("Does this look good? answer with Y/n : ")
if a != 'Y':
    print("Go to file 'team2.csv' and fix it")
    print("Quiting now...")
    sys.exit()


g = input("Ready to go? Enter Y or n : ")
if g != 'Y':
    print("Quiting now...")
    sys.exit()


print(r"""
                     _
                    / )
                   / /
            .-""-.//'
           /_____B\___
           /// 6 6~\~~`
           (    7  )
            \  '='/
          _//'---'\                   
         ( \       `\                 
         (\/`-.__/  /
          "`-._  _.' 
          
          """)
print("PLAY BALL")



def batter_at_bat(batter,batter_target):
    global swing_score
    global t1_at_bat_number
    global t2_at_bat_number

    print("Now at bat ", batter, "!")
    swing_score = dice(1, 100, 'DT')
    print(batter,"'s Swing Score is ", swing_score, " Their swing target is", batter_target)










def pitcher_at_bat(pitcher, pitch_die, batter, batter_target):
    global pitch_swing_score
    global outcome
    global out
    global t1_at_bat_number
    global t2_at_bat_number
    global base
    global runner

    pitch_swing_score = dice(1, pitch_die, 'DT')
    swing_target = pitch_swing_score + swing_score
    print(pitcher, "'s  pitch die rolled ", pitch_swing_score, " Bringing ", batter, " 's swing score up to",swing_target)

    if swing_target <= batter_target:
        print("HIT!")
        outcome = "hit"

    elif swing_target < batter_target + 5:
        print("WALK!")
        outcome = "walk"
        base = 1
        runner = 1
    elif batter_target + 5 < swing_target:
        print("OUT!")
        outcome = "out"
        out = out +1
        base = 0
        runner = 0




t1_at_bat_number = 0
t2_at_bat_number = 0




def out_result():
    global outcome
    global out
    out_die = dice(0, 9, 'DT')
    if out_die == 0 or 1 or 2:
        print("STRIKEOUT!")
        outcome = 'strikeout'
    elif out_die == 3:
        print("Groundout to first!")
        outcome = 'G-3'
    elif out_die == 4:
        print("Groundout to second!")
        outcome = '4-3'
    elif out_die == 5:
        print('Groundout to third!')
        outcome = '5-3'
    elif out_die == 6:
        print("Groundout to shortstop!")
        outcome = '6-3'
    elif out_die == 7:
        print("Fly out to left field!")
        outcome = 'F-7'
    elif out_die == 8:
        print("Fly out to center!")
        outcome = 'F-8'
    elif out_die == 9:
        print("Fly out to right field!")
        outcome = 'F-9'
    out = out + 1


def defense():
    # consult defense table on page 17
    print("running defense function")
    global outcome
    global base
    global runner
    global defense_outcome
    def_die = dice(1,12,'DT')
    print("defense dice rolled ", def_die)
    if def_die == range(1,3,1):
        print('ERROR!, RUNNERS TAKE AN EXTRA BASE')
        base = base + 1
        defense_outcome = 'error'
    elif def_die == range(10,12,1):
        if base == 2:
            base = 1
            runner = 2
        elif base == 3:
            base = 2
            runner = 3
        defense_outcome = 'level'
    elif def_die == 12:
        out_result()
    else:
        defense_outcome = 'hit'

# def score_keeping():

    

def team_at_bat(at_bat_team_data, pitching_team_data):
    global out
    global t1_at_bat_number
    global t2_at_bat_number
    global base
    global runner
    global outcome
    global defense_outcome
    out = 0

    pitcher = pitching_team_data['Name'][8]
    pitch_die = pitching_team_data['d'][8]

    while out < 3:

        batter = at_bat_team_data['Name'][t1_at_bat_number]
        batter_target = at_bat_team_data['BT'][t1_at_bat_number]

        batter_at_bat(batter, batter_target,)
        pitcher_at_bat(pitcher,pitch_die, batter, batter_target)

        if at_bat_team_data is team_1_data:
            t1_at_bat_number = t1_at_bat_number + 1
            if t1_at_bat_number == 8:
                t1_at_bat_number = 0
        if at_bat_team_data is team_2_data:
            t2_at_bat_number = t2_at_bat_number + 1
            if t1_at_bat_number == 8:
                t1_at_bat_number = 0
        if outcome == 'hit':
            hit_die = dice(1,20,'DT')
            print("hit dice rolled", hit_die)
            if hit_die in range(1,3,1):
                print('Single!')
                base = 1
                runner = 1
                outcome = 'single'
            elif hit_die in range(3, 8, 1):
                print("hit die rolled a number from 3-7")
                base = 1
                defense()
                if defense_outcome == 'hit':
                    print('Single!')
                    base = 1
                    runner = 1
                    outcome = 'single'
            elif hit_die in range(8,13,1):
                print("single! Runners advance 2!")
                base = 1
                runner = 2
                outcome = 'single+'
            elif hit_die in range(13, 16, 1):
                base = 2
                defense()
                if defense_outcome == 'hit':
                    print('Double!')
                    base = 2
                    runner = 2
                    outcome = 'double'
            elif hit_die in range(16, 18, 1):
                print('DOUBLE!! RUNNERS ADVANCE THREE')
                base = 2
                runner = 3
                outcome = 'double+'
            elif hit_die == 18:
                defense()
                if defense_outcome == 'hit':
                    print("Its a Triple!")
                    base = 3
                    runner = 3
                    outcome = 'triple'
            elif hit_die in range(19,21,1):
                print('HOLY GUACAMOLE ITS GONE!!')
                base = 4
                runner = 4
                outcome = 'home run'
            print("runners advance ", runner, " bases")
            print('At bat runner advance', base, " bases")


        print(out, "out's")
        input('press enter to proceed...')




team_at_bat(team_2_data, team_1_data,)


