class Event(object):
    def __init__(self, description):
        self._description = description

    def get_description(self):
        return self._description
