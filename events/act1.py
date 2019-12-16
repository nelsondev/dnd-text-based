import time

def event_play(game):
    game.stopSound()
    game.print("A man sleeps in a dark dim room, only bright from the moons shine; awake, listening to the thunder and lightning passing. Sleepless nights aren’t called upon but brought upon by the human mind for reasons unknown.")
    game.print("BANG BANG!")
    game.print("The door to the room shutters as if a large gust of wind had blown it off the hinges. Throwing yourself out of bed in defence; your eyes adjust to the dim light only able to make out vague forming blurs of dark static.")
    game.setState("start")
    return 0

def event_start(game):
    game.print("CLICK!")
    game.print("The lamp illuminates the room only not reaching to the deep corners. Dark shadows start taking shape: a dresser, a record player, and your lockbox on top of your shelf. It looks safe.")
    game.setState("dream-0-choice-0")
    return 0

def event_wardrobe_choice_0(game):
    game.playSound("./audio/titlescreenboosted.wav")
    time.sleep(0.25)
    game.print("OH god that was loud")
    game.stopSound()
    return 0

def event_wardrobe_choice_1(game):
    game.print("The lockbox is cold, covered in dust and looks unopened. There's a key hole on the front.")
    return 0

def event_wardrobe_choice_2(game):
    game.print("I wonder what I should wear today...")
    game.print("Shirts:")
    game.print("1)  Blouse")
    game.print("2)  Denim Vest")
    game.print("3)  Hawaiian")
    game.print("4)  Tuxedo T-Shirt")

    game.setState("wardrobe-shirts")

    return 0

def event_wardrobe_choice_3(game):
    game.print("Pants:")
    game.print("  Zipoff pants")
    game.print("  Jorts")
    game.print("  Leggings")
    game.print("  Swim Trunks\n")
    
    game.setState("wardrobe-pants")

    return 0

__all__ = [
    'event_play', 
    'event_start', 
    'event_wardrobe_choice_0',
    'event_wardrobe_choice_1',
    'event_wardrobe_choice_2',
    'event_wardrobe_choice_3'
]