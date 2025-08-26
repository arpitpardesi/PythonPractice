from monkey1 import Monkey

def new_speak(self):
    return "Hello! I'm a patched monkey!"

Monkey.speak = new_speak
