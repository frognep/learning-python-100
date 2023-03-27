## GLOBAL VARIABLES = CAPS = DO NOT MODIFY

# EX
PI = 3.14159

def potion_strength():
    global strength

    strength += 1

    return strength

strength = 1

potion_strength()

print(strength)