from random import randint

name = input('What is your name? >>> ')

hero = {
    name: {
        "health": 100,
        "damage1": 30,
        "damage2": 25,
        "damage3": 20,
        "damage4": 15,
        "damage5": 10,
    }
}

enemies = {
    "Varkos": {
        "health": 100,
        "damage": 20,
        "level": 1
    },
    "Grimclaw": {
        "health": 150,
        "damage": 30,
        "level": 2
    },
    "Zareth": {
        "health": 80,
        "damage": 15,
        "level": 3
    }
}

boss_level = randint(1, 3)

for enemy in enemies:
    if enemies[enemy]["level"] == boss_level:
        boss = enemy

print('Welcome to the game!')
print('_________________________________')
print(f'Your enemy is {boss}')
print('Parameters:')
print(f'Health: {enemies[boss]["health"]}')
print(f'Damage: {enemies[boss]["damage"]}')
print(f'Level: {enemies[boss]["level"]}')
print('_________________________________')

while True:
    hero_hit = input('Choose your number to hit (from 1 to 5) >>> ')

    try:
        hero_hit = int(hero_hit)
        if hero_hit < 1 or hero_hit > 5:
            print('Please choose a number from 1 to 5.')
            continue
    except ValueError:
        print('Please enter a valid number, not letters!')
        continue

    damage_key = f"damage{hero_hit}"
    damage = hero[name][damage_key]

    enemy_move = randint(0, 5)

    print(f'You chose: {hero_hit}')
    print(f'Enemy chose: {enemy_move}')


    if hero_hit == 5 and enemy_move == 5:

        enemy_damage = enemies[boss]["damage"]

        enemies[boss]["health"] -= damage
        hero[name]["health"] -= enemy_damage + damage

        print('Critical clash!')
        print(f'You hit the enemy for {damage} damage!')
        print(f'You received {enemy_damage + damage} damage!')

    elif hero_hit > enemy_move:

        enemies[boss]["health"] -= damage

        print(f'You hit the enemy for {damage} damage!')

    elif hero_hit < enemy_move:

        enemy_damage = enemies[boss]["damage"]

        hero[name]["health"] -= enemy_damage

        print(f'You were hit for {enemy_damage} damage!')

    else:
        print('You parried the attack!')

    print('_________________________________')
    print(f'Enemy health: {enemies[boss]["health"]}')
    print(f'{name} health: {hero[name]["health"]}')
    print('_________________________________')

    if hero[name]["health"] <= 0:
        print(f'{name} health: {hero[name]["health"]}')
        print('You lost!')
        break

    if enemies[boss]["health"] <= 0:
        print(f'{boss} health: {enemies[boss]["health"]}')
        print('You won!')
        break
