import json
import sqlite3


# Main function that loads room.
def get_room(id, dbfile):
    ret = None

    con = sqlite3.connect(dbfile)

    for row in con.execute("SELECT json FROM rooms WHERE id=?", (id,)):

        jsontext = row[0]
        d = json.loads(jsontext)
        d['id'] = id
        ret = Room(**d)
        break

    con.close()
    return ret

# Room class.


class Room():

    def __init__(self, id=0, name="A Room", description="An empty room", neighbours={}):
        self.id = id
        self.name = name
        self.description = description
        self.neighbours = neighbours

    def _neighbour(self, direction):
        if direction in self.neighbours:
            return self.neighbours[direction]
        else:
            return None

    def north(self):
        return self._neighbour('n')

    def east(self):
        return self._neighbour('e')

    def south(self):
        return self._neighbour('s')

    def west(self):
        return self._neighbour('w')
