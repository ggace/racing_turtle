class Boost:
    percentage:int
    repeat:int
    forward:tuple

    def __init__(self, percentage:int, forward: tuple):
        self.percentage = percentage
        self.forward    = forward