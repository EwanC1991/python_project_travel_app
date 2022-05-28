class City:
    def __init__(self, name, country, visited= False, id=None):
        self.name = name
        self.visited = visited
        self.country = country
        self.id=id

    def mark_visited(self):
        self.visited = True