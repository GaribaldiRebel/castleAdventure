#!/usr/bin/env python3

###############################################
# Script imports room text files of (n).json
# format to be imported into the game db.
# Will replace room details in db if they
# already exist.
#

import sys
import sqlite3
import os


def main(dbname):
    con = sqlite3.connect(dbname)

    # Created the tables if it does not exist.
    con.execute(
        "CREATE TABLE IF NOT EXISTS rooms(id INTEGER PRIMARY KEY, json TEXT NOT NULL)")
    con.commit()

    # For each filename with a .json extension it reads
    # contents and writes them to the rooms table in the db.
    for filename in os.listdir('./'):
        base, extension = os.path.splitext(filename)
        if extension == '.json':
            with open(filename, 'r') as f:
                json = f.read()

                print("Inserting room {0}".format(int(base)))

                con.execute(
                    "INSERT OR REPLACE INTO rooms(id, json) VALUES(?, ?);", (int(base), json))
                con.commit()

    con.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: {0} <database name>'.format(sys.argv[0]))
    else:
        main(sys.argv[1])
