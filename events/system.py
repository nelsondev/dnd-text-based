import winsound

def printTitleScreen(game):
    print("  . .. .. . .")
    print("  . ####### .")
    print("  . # ## ## .")
    print("  . ####### .")
    print("  .  #####  .")
    print("  .  #####  .")
    print("  .  #####  .")
    print("  .  #####  .")
    print("  .  #####  .")
    print("  .  ## ##  .")
    print("  .#### ####.")
    print("  @.@@@@.@@.@")
    print("- Mannys Week -")
    print("> play - help")
    game.playSound("./audio/titlescreen.wav")

def event_exit(game):
    print("Bye!")
    return 1

def event_help(game):
    str = "\nMannys Week Help:\n"
    str += "* quit - quit game\n"
    str += "* help - display this message\n"
    str += "* save <name> - save game\n"
    str += "* load <name> - load game file\n"
    str += "* delete <name> - delete game file\n"
    str += "* stat - display game statistics\n"
    print(str)
    return 0

def event_save(game):

    if (len(game.getArgs()) < 2):
        print("Please enter a name for the save. Ex: > save nelsons game")
        return 0
    
    # grab the save game name from the command args
    name = game.getCleanArgs()
    game.save(name)
    return 0

def event_load(game):

    if (len(game.getArgs()) < 2):
        print("Please enter the name of the save. Ex: > load nelsons game")
        return 0

    name = game.getCleanArgs()
    return game.load(name)

def event_delete(game):

    if (len(game.getArgs()) < 2):
        print("Please enter the name of the save. Ex: > load nelsons game")
        return 0

    name = game.getCleanArgs()
    game.delete(name)
    return 0

def event_stats(game):
    # TODO: print game state.
    print("")
    return 0

__all__ = [ 
    'printTitleScreen', 
    'event_exit', 
    'event_help', 
    'event_save', 
    'event_load', 
    'event_delete', 
    'event_stats' 
]