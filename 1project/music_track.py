class MusicTrack:
    def __init__(self, path):
        """ """
        self.path = path

    def __eq__(self, other):
        if other:
            return self.path == other.path
        return False
