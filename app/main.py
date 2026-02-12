from modules.knights_configs import KNIGHTS
from modules.knights import Knight


def battle(knightsConfig: dict) -> dict:
    lancelot = Knight(knightsConfig["lancelot"])
    lancelot.prepare_for_battle()

    arthur = Knight(knightsConfig["arthur"])
    arthur.prepare_for_battle()

    mordred = Knight(knightsConfig["mordred"])
    mordred.prepare_for_battle()

    red_knight = Knight(knightsConfig["red_knight"])
    red_knight.prepare_for_battle()

    # 1 Lancelot vs Mordred:
    lancelot.attack(mordred)
    mordred.attack(lancelot)

    # 2 Arthur vs Red Knight:
    arthur.attack(red_knight)
    red_knight.attack(arthur)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }

knightsConfig = KNIGHTS
print(battle(knightsConfig))
