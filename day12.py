#_____________scope____________
# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside the function: {enemies}")

#local scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()

#global scope
# player_health = 10

# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# drink_potion()

#______Modifying global scope____________

# enemies = 1
# def increase_enemies():
#     # global enemies
#     # enemies += 1
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

#----------Global constant------
PI = 3.1415
URL = ""
