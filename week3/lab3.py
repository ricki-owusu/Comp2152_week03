import random

# Dice Options using list() and range()
diceOptions = list(range(1, 7))

# Weapons array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

print("Available Weapons:", ', '.join(weapons))


# Inputs combat strength hero
combatStrength = int(input("Enter your combat strength (1-6): "))
if combatStrength < 1 or combatStrength > 6:
    print("Invalid input! Combat strength should be between 1 and 6.")
    combatStrength = 1 #Default value for invalid input


# Input combat strength for the monster
mCombatStrength = int(input("Enter your combat strength (1-6): "))
if mCombatStrength < 1 or mCombatStrength > 6:
    print("Invalid input! Combat strength should be between 1 and 6.")
    mCombatStrength = 1 #Default value for invalid input

#Simulate Battle Rounds 
for j in range(1, 21, 2): #Simulation of 20 rounds, stepping by 2
    #Dice rolls for hero and monster
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    #Calculate the weapons
    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    #Calculate total strength
    heroTotal = combatStrength + heroRoll
    monsterTotal = mCombatStrength + monsterRoll 

    #Print round details
    print(f"\nRound {j} Hero rolled {heroRoll}, Monster rolled {monsterRoll}")
    print(f"Hero selected: {heroWeapon}, Monster selected: {monsterWeapon}")
    print(f"Hero total strength: {heroRoll}, Monster total strength: {monsterTotal}")

    # Determine Winner
    if heroTotal > monsterTotal:
        print("Hero wins the round!")
    elif heroTotal < monsterTotal:
        print("Monster wins the round!")
    else:
        print("Its a tie!")
    
    if j == 11:
        print("\n Battle Truce declared in Round 11. Game Over!")
        break
    if j != 11:
        print("\n Battle conluded after 20 rounds!")

