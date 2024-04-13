#Clubs
driver_distance = [range(220,260, 5)]
five_distance = [range(155, 185, 5)]
seven_distance = [range(140, 160, 5)]
nine_distance = [range(115, 135,5)]
pitching_wedge_distance = [range(60, 110, 5)]
lob_wedge_distance = [range(20, 55, 5)]
putts = [1,2,3] 

#Define functions for hitting clubs
def hit_driver():
    club_distance = random.choice(driver_distance)
    return club_distance

def hit_five_iron():
    club_distance = random.choice(five_distance)
    return club_distance

def hit_seven_iron():
    club_distance = random.choice(seven_distance)
    return club_distance

def hit_nine_iron():
    club_distance = random.choice(nine_distance)
    return club_distance

def hit_pitching_wedge():
    club_distance = random.choice(pitching_wedge_distance)
    return club_distance

def hit_lob_wedge():
    club_distance = random.choice(lob_wedge_distance)
    return club_distance

def putt():
    putt = random.choice(putts)
    return putt

#Course Setup
full_range = [range(130,520,5)]
par3 = [range(130,250,5)]
par4 = [range(250,440,5)]
par5 = [range(440,500,5)]
par3_4 = par3 + par4
par3_5 = par3 + par5
par4_5 = par4 + par5

par3_count = 0
par4_count = 0
par5_count = 0

#Scorecard
total_strokes = 0
total_to_par = 0

#Introduction
print("Welcome to Type Golf! Ready to play?")
print()

answer = input(" ")

if answer == "no":
    print()
    print("Come back when you are ready to play.")
    print()
    exit()

else:
    print()
    print("Good Luck!")
    print()

club_choices = "Here is your bag: Driver, 5 Iron, 7 Iron, 9 Iron, Pitching Wedge, Lob Wedge, Putter."

print(club_choices)
print()

#Main Game

#Loop for holes 1-9
for x in range(1,10):

    #Create hole count restrictions on par
    if par3_count < 2 and par4_count < 5 and par5_count < 2:
        hole_length = random.choice(full_range)
    if par3_count >= 2 and par4_count < 5 and par5_count < 2:
        hole_length = random.choice(par4_5)
    if par3_count >= 2 and par4_count < 5 and par5_count >= 2:
        hole_length = random.choice(par4)
    if par3_count < 2 and par4_count < 5 and par5_count >= 2:
        hole_length = random.choice(par3_4)
    if par3_count < 2 and par4_count >= 5 and par5_count >= 2:
        hole_length = random.choice(par3)
    if par3_count >= 2 and par4_count >= 5 and par5_count < 2:
        hole_length = random.choice(par5)
    if par3_count < 2 and par4_count >= 5 and par5_count < 2:
        hole_length = random.choice(par3_5)  

    #Par for the hole
    if hole_length <= 250:
        par = 3
        par3_count += 1
    elif hole_length > 250 and hole_length <= 440:
        par = 4
        par4_count += 1
    elif hole_length > 440:
        par = 5
        par5_count += 1
    
    #Set perameters for starting each hole
    distance_remaining = hole_length
    hole_shots = 0