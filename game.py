import os
import winsound

SAVE_FILE = "save.txt"

class Event:
    def __init__(self, name, state, call, strict=""):
        self._name = name
        self._state = state
        self._call = call
        self._strict = strict

    def __checkInput(self, game):
        
        result = False
        
        if (self._strict == "strict"):
            
            for name in self._name.split(","):
                if (game.getInput().lower() != name): continue
                result = True
                break

        elif self._strict == "contains":

            for name in self._name.split(","):
                if (not name in game.getInput().lower()): continue
                result = True
                break

        else:

            for name in self._name.split(","):
                if (game.getArgs()[0].lower() != name): continue
                result = True
                break

        return result

    def call(self, game):
        if (self._state != "global" and game.getState() != self._state): return 0
        if (not self.__checkInput(game)): return 0
        return self._call(game)

class Handler:
    def __init__(self, game):
        self.__events = []
        self.__game = game

    def register(self, event):
        self.__events.append(event)

    def start(self):
        state = 0
        while state != 1:
            # grab next text input from player
            self.__game.setInput(input("> "))
            print(" ")
            # loop through events in stack and execute their calls
            # on condition of the input string matches.
            for event in self.__events:
                if (state == 1): break
                state = event.call(self.__game)

class Game:

    def __init__(self):
        self.__handler = Handler(self)
        self.__state = "title"
        self.__input = ""
        self.__name = ""
        self.__sounds = []

    # getters
    def getState(self):
        return self.__state
    def getFullState(self):
        return self.__state.split("-")
    def getInput(self):
        return self.__input
    def getArgs(self):
        return self.__input.split(" ")
    def getCleanArgs(self):
        return " ".join(self.getArgs()[1:])
    def getName(self):
        return self.__name

    # setters
    def setState(self, state):
        self.__state = state
    def setInput(self, string):
        self.__input = string
    def setName(self, string):
        self.__name = string

    # methods
    def print(self, str):
        self.__print(str)

    def __print(self, str):

        if (len(str) <= 80):
            return print(str + "\n")

        # grab the first 80 chars in the string
        result = str[0:79]

        # if last character or next line last char is space, just print
        if (str[80] == " " or str[78] == " "):
            print(result)
        # else, assume a word has been broken.
        else:
            print(result + "-")
        
        # recursively call self for remaining string.
        self.__print(str[79:])

    def playSound(self, name):
        self.__sound = winsound.PlaySound(name, winsound.SND_ASYNC | winsound.SND_ALIAS)

    def stopSound(self):
        self.__sound = winsound.PlaySound(None, winsound.SND_ASYNC)

    def handle(self, event):
        return self.__handler.register(event)
    
    def start(self):
        self.__handler.start()

    def __read(self):
        data = []
        try:
            with open(SAVE_FILE, "r") as file:
                data = file.readlines()
                file.close()
        except IOError:
            with open(SAVE_FILE, "w") as file:
                file.close()
        finally:
            return data

    def __deserialize(self, str):
        str = str.replace("Game=", "")
        # remove the brackets and new line characters
        str = str[1:len(str)-2]
        # split the properties by the comma
        str = str.split(",")
        # load the sep properties into an array
        str = [ str[0].split("="), str[1].split("=") ]
        return str

    def __existsAt(self, name):
        data = self.__read()
        line = -1

        for i in range(len(data)):
            deserialized = self.__deserialize(data[i])
            if (deserialized[0][1] == name):
                line = i

        return line

    def save(self, name):

        self.__name = name

        try:
            # open save.txt in read mode to grab lines
            with open(SAVE_FILE, "r") as file:
                data = file.readlines()
                file.close()

            # grab data line that contains named save
            line = self.__existsAt(name)

            # if data doesn't exist, just append a new line
            if (line == -1):
                with open(SAVE_FILE, "a+") as file:
                    file.write(self.__str__() + "\n")
            # data exists, change the line, then write all lines
            else:
                data[line] = self.__str__() + "\n"
                with open(SAVE_FILE, "w") as file:
                    file.writelines(data)
                    file.close()

        except IOError:
            print("Save file unable to be created..")
        finally:
            print("Wrote save '" + name + "'.")

    def load(self, name):
        # read file, grab data
        line = self.__existsAt(name)

        if (line == -1):
            print("No save game with name '" + name + ".'")
            return 0

        data = self.__read()[line]
        data = self.__deserialize(data)

        self.__name = data[0][1]
        self.__state = data[1][1]

        print("Loaded game '" + self.__name + ".'")
        return 0

    def delete(self, name):

        line = self.__existsAt(name)

        if (line == -1):
            print("No save game with name '" + name + ".'")
            return 0

        # open file and grab line data
        data = self.__read()

        # delete from array
        del data[line]

        # write lines back
        with open(SAVE_FILE, "w") as file:
            file.writelines(data)
            file.close()

        print("Removed game '" + name + ".'")

    # override
    def __str__(self):
        str = "Game={"
        str += "name=" + self.__name
        str += ",state=" + self.__state
        str += "}"
        return str