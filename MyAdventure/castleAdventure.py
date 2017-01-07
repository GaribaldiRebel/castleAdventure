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
import textwrap
import shutil
import tempfile
import os


class Game(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)

        # Creating a temp file and copying the game database into it.
        self.handle, self.dbfile = tempfile.mkstemp()
        shutil.copyfile("castle.db", self.dbfile)

        # Calls get_room to load room then print it.
        self.loc = get_room(1, self.dbfile)
        self.print_room()

    # Function to handle movement commands.
    def move(self, dir):
        newroom = self.loc._neighbour(dir)
        if newroom is None:
            print("You seemed to have banged your head! Be more careful.")
        else:
            self.loc = get_room(newroom, self.dbfile)
            self.print_room()

    # Function to print out room.
    def print_room(self):
        os.system('clear')
        print(self.loc.name)
        print("")
        # Uses textwrap to tidy text on screen.
        for line in textwrap.wrap(self.loc.description, 72):
            print(line)

    # Ends game and tidies up files.
    def do_quit(self, args):
        """Quits the game."""
        print("Thank you for playing. See you again soon.")
        # Remove temporary db file (created in __init__) as mkstemp does not do
        # this.
        try:
            os.remove(self.dbfile)
        except OSError:
            pass
        return True

    # Functions that enable commands to be interpreted by cmd.Cmd.
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

    def do_save(self, args):
        """Save the game. Save <filename>"""
        shutil.copyfile(self.dbfile, args)
        print("The game was saved to {0}".format(args))

if __name__ == "__main__":
    g = Game()
    g.cmdloop()
