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
