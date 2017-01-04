#!/usr/bin/env python3

######################################
# This text adventure program has been  
# coded by Phil Gibbons as a learning
# tool.
#
# Insperation and most of code 
# provided by Jeffrey Armstrong
# from his excellent PyOhio 2013
# video https://youtu.be/8CDePunJlck
#

import cmd
from room import get_room


class Game(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)

        self.loc = get_room(1)
        self.look()

    def move(self, dir):
        newroom = self.loc._neighbour(dir)
        if newroom is None:
            print("You seemed to have banged your head! Be more careful.")
        else:
            self.loc = get_room(newroom)
            self.look()

    def look(self):
        print(self.loc.name)
        print("")
        print(self.loc.description)

    def do_quit(self, args):
        """Quits the game."""
        print("Thank you for playing. See you again soon.")
        return True

    def do_n(self, args):
        """Wander in a northerly direction."""
        self.move('n')

    def do_e(self, args):
        """Wander in an easterly direction."""
        self.move('e')

    def do_s(self, args):
        """Wander in a southerly direction."""
        self.move('s')

    def do_w(self, args):
        """Wander in a westerly direction."""
        self.move('w')

if __name__ == "__main__":
    g = Game()
    g.cmdloop()
