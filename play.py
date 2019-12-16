from game import Game, Event
from events.system import *
from events.act1 import *

# instantiate game inst
game = Game()

# register events
game.handle(Event("exit,quit", "global", event_exit, "strict"))
game.handle(Event("help", "global", event_help, "strict"))
game.handle(Event("save", "global", event_save))
game.handle(Event("load", "global", event_load))
game.handle(Event("delete", "global", event_delete))
game.handle(Event("stat", "global", event_stats, "strict"))
game.handle(Event("play", "title", event_play, "strict"))
game.handle(Event("lamp,light,switch", "start", event_start, "contains"))
game.handle(Event("record", "dream-0-choice-0", event_wardrobe_choice_0, "contains"))
game.handle(Event("lock", "dream-0-choice-0", event_wardrobe_choice_1, "contains"))
game.handle(Event("dresser", "dream-0-choice-0", event_wardrobe_choice_2, "contains"))
game.handle(Event("1,2,3,4", "wardrobe-shirts", event_wardrobe_choice_3, "strict"))

printTitleScreen(game) # print starting title

game.start()
