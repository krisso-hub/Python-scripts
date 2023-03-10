
class Dock:
    sound = "Quack quack."
    movement = "walk like a duck."

    def quack(self):
        print(self.sound)
    def move(self):
        print(self.movement)

def main():
    donald = Dock()
    donald.quack()
    donald.move()
if __name__ == "__main__" : main()