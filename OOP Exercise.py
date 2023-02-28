class IOString:
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())


xyz = IOString()
xyz.get_string()
xyz.print_string()
