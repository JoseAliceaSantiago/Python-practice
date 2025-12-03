def get_max_health(modifier, level):
    return modifier * level


my_modifier = 5
my_level = 10

## don't touch above this line

max_health = get_max_health(my_modifier, my_level) #solved, solution: replaced parameter with my_modifier and my_level instead of modifier and level

# don't touch below this line

print(f"max_health is: {max_health}")
