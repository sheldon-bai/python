class Ninja():
    def __init__(self, name):
        self.name = name

    def callName(self):
        print(self.name)

def main():
    aaa = Ninja('aaa')
    aaa.callName()

main()
