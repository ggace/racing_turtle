class Boost:
    percentage:int
    repeat:int
    forward:tuple

    def __init__(self, percentage, repeat, forward):
        self.percentage = percentage
        self.repeat = repeat
        self.forward = forward