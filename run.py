import random

# Clubs
driver_distance = list(range(220, 260, 5))
three_wood_distance = list(range(185, 220, 5))
five_distance = list(range(155, 185, 5))
seven_distance = list(range(140, 160, 5))
nine_distance = list(range(115, 135, 5))
pitching_wedge_distance = list(range(60, 110, 5))
lob_wedge_distance = list(range(15, 55, 5))
putter = [1, 2, 3]


# Define functions for hitting clubs
def hit_driver():
    club_distance = random.choice(driver_distance)
    return club_distance


def hit_three_wood():
    club_distance = random.choice(three_wood_distance)
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
    putt = random.choice(putter)
    return putt


# Course Setup
full_range = list(range(130, 520, 5))
par3 = list(range(130, 250, 5))
par4 = list(range(250, 440, 5))
par5 = list(range(440, 500, 5))
par3_4 = par3 + par4
par3_5 = par3 + par5
par4_5 = par4 + par5

par3_count = 0
par4_count = 0
par5_count = 0

# Scorecard
total_strokes = 0
total_to_par = 0

# Introduction
print("Welcome to Type Golf! Would you like to see the rules?")
print()
print("Type y/n")
print()



while True:
    answer = input("")
    if answer == "y":
        print()
        print("*When the game begins you will be presented with your clubs.")
        print()
        print("*The information for the hole will then show.")
        print()
        print("*Type which club you would like to use.")
        print()
        print("*If you dont make it onto the green you will then be shown the")
        print()
        print("distances remaining and prompted to hit your next shot.")
        print()
        print("*Make it onto the green the game will automatically putt for you.")
        print()
        print("*You will move onto the next hole and the loop will repeat.")
        print()
        break

    elif answer == "n" or answer == "N":
        print()
        print("Good Luck!")
        print()
        break

    elif answer:
        print()
        print("Invalid input please type y/n")
        print()

club_choices = ("Here is your bag: Driver, 3 Wood, "
                "5 Iron, 7 Iron, 9 Iron, Pitching Wedge, Lob Wedge.")

print()

# Main Game

# Loop for holes 1-9
for x in range(1, 10):

    # Create hole count restrictions on par
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

    # Par for the hole
    if hole_length <= 250:
        par = 3
        par3_count += 1
    elif hole_length > 250 and hole_length <= 440:
        par = 4
        par4_count += 1
    elif hole_length > 440:
        par = 5
        par5_count += 1

    # Set parameters for starting each hole
    distance_remaining = hole_length
    hole_shots = 0
    print(club_choices)
    print()

    # Show player the hole information
    print("Hole #" + str(x) + " is a " + str(hole_length)
          + "-yard Par " + str(par) + ".")
    print()

    # Start loop to be able to choose clubs while at least 20 yards away
    while distance_remaining >= 20:
        club = input("What club would you like to use? ")
        if club == "Driver" or club == "driver":
            shot_distance = hit_driver()
            print()
            print("You hit your Driver " + str(shot_distance) + " yards.")
            distance_remaining = abs(distance_remaining - shot_distance)
            print("You have " + str(distance_remaining) + " yards left.")
            print()
            hole_shots += 1
        elif (club == "3Wood"
                or club == "3 Wood"
                or club == "3 wood"
                or club == "3wood"
                or club == "3Wood"
                or club == "3w"
                or club == "3"
                or club == "3W"):
            shot_distance = hit_three_wood()
            print()
            print("You hit your 3 Wood " + str(shot_distance) + " yards.")
            distance_remaining = abs(distance_remaining - shot_distance)
            print("You have " + str(distance_remaining) + " yards left.")
            print()
            hole_shots += 1
        elif (club == "5Iron"
                or club == "5 iron"
                or club == "5 Iron"
                or club == "5"
                or club == "5i"
                or club == "5I"
                or club == "5iron"):
            shot_distance = hit_five_iron()
            print()
            print("You hit your 5 Iron " + str(shot_distance) + " yards.")
            distance_remaining = abs(distance_remaining - shot_distance)
            print("You have " + str(distance_remaining) + " yards left.")
            print()
            hole_shots += 1
        elif (club == "7 Iron"
                or club == "7 iron"
                or club == "7iron"
                or club == "7Iron"
                or club == "7"
                or club == "7i"):
            shot_distance = hit_seven_iron()
            print()
            print("You hit your 7 Iron " + str(shot_distance) + " yards.")
            distance_remaining = abs(distance_remaining - shot_distance)
            print("You have " + str(distance_remaining) + " yards left.")
            print()
            hole_shots += 1
        elif (club == "9 Iron"
                or club == "9 iron"
                or club == "9iron"
                or club == "9Iron"
                or club == "9"
                or club == "9i"
                or club == "9I"):
            shot_distance = hit_nine_iron()
            print()
            print("You hit your 9 Iron " + str(shot_distance) + " yards.")
            distance_remaining = abs(distance_remaining - shot_distance)
            print("You have " + str(distance_remaining) + " yards left.")
            print()
            hole_shots += 1
        elif (club == "Pitching Wedge"
                or club == "pitching wedge"
                or club == "Pitching wedge"
                or club == "pitching Wedge"
                or club == "pitching"
                or club == "Pitching"):
            shot_distance = hit_pitching_wedge()
            print()
            print("You hit your Pitching Wedge " +
                  str(shot_distance) + " yards.")
            distance_remaining = abs(distance_remaining - shot_distance)
            print("You have " + str(distance_remaining) + " yards left.")
            print()
            hole_shots += 1
        elif (club == "Lob Wedge"
                or club == "lob wedge"
                or club == "Lob wedge"
                or club == "lob Wedge"
                or club == "lob"
                or club == "Lob"):
            shot_distance = hit_lob_wedge()
            print()
            print("You hit your Lob Wedge " + str(shot_distance) + " yards.")
            distance_remaining = abs(distance_remaining - shot_distance)
            print("You have " + str(distance_remaining) + " yards left.")
            print()
            hole_shots += 1
        elif club:
            print()
            print("You do not have this club in your")
            print("bag or club name invalid.")
            print()

    # Finish the hole by putting
    if distance_remaining < 20:
        if distance_remaining == 0:
            putts = 0
            hole_strokes = hole_shots + putts
            hole_to_par = hole_strokes - par
            total_strokes += hole_strokes
            total_to_par += hole_to_par
        else:
            putts = putt()
            hole_strokes = hole_shots + putts
            hole_to_par = hole_strokes - par
            total_strokes += hole_strokes
            total_to_par += hole_to_par

        # Show player hole/round scoring info
        if putts == 0:
            print("You're in the hole! You're in for "
                  + str(hole_strokes) + " strokes.")
        else:
            print("You're on the green! After " + str(putts) +
                  " putt(s), you're in for " + str(hole_strokes) + " strokes.")
        if hole_to_par > 0:
            print("Your score for the hole is +"
                  + str(hole_to_par) + " to par.")
        elif hole_to_par == 0:
            print("Your score for the hole is even to par.")
        else:
            print("Your score for the hole is "
                  + str(hole_to_par) + " to par.")
        print()
        print("You've hit a total of "
              + str(total_strokes) + " strokes so far.")
        if total_to_par > 0:
            print("Your score for the round is +"
                  + str(total_to_par) + " to par.")
        elif total_to_par == 0:
            print("Your score for the round is even to par.")
        else:
            print("Your score for the round is "
                  + str(total_to_par) + " to par.")
        print()
        print()
        print()

# Final score messages & exit prompt
print("Congratulations on finishing your 9-hole round!")
print()
print("Your stroke total is " + str(total_strokes) + ".")
print()
if total_to_par > 0:
    print("Your score for the day is +" + str(total_to_par) + " to par.")
elif total_to_par == 0:
    print("Your score for the day is even to par.")
    print()
else:
    print("Your score for the day is " + str(total_to_par) + " to par.")
print()
print()
print("Type Exit To Exit")
print()
print()

while True:
    end = input("")
    if end == "Exit" or end == "exit":
        exit()
    elif end:
        print()
        print("Type Exit To Exit")
        print()

