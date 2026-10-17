NO-ARGUMENT CONSTRUCTOR

    # ❌ Cannot choose starting values when creating the object
    # ✅ Values can still be changed later because they are public
    def __init__(self):
        self.health = 100
        self.score = 0

def main():
player1 = Player()

    # Player(200, 50) ❌ NOT allowed by this constructor

    player1.health = 200  # ✅ Can change afterward because it is public

    print(player1.health)
    print(player1.score)

main()

---

# CONSTRUCTOR WITH REQUIRED ARGUMENTS

    # ✅ You MUST provide name and health when creating the object
    # ❌ Player() by itself will NOT work
    # ✅ Variables can be changed afterward because they are public
    def __init__(self, name, health):
        self.name = name
        self.health = health

def main():
player1 = Player("Tony", 100)

    # player2 = Player() ❌ NOT allowed because arguments are required

    player1.health = 200  # ✅ Can change afterward

    print(player1.name)
    print(player1.health)

main()

---

    # CONSTRUCTOR WITH DEFAULT ARGUMENTS
    # ✅ Player() works because default values are provided
    # ✅ Player("Tony", 200) also works and overrides the defaults
    # ✅ Variables can be changed afterward because they are public
    def __init__(self, name="Unknown", health=100):
        self.name = name
        self.health = health

def main():
player1 = Player() # ✅ Uses defaults
player2 = Player("Tony", 200) # ✅ Overrides defaults

    player1.health = 150            # ✅ Can change afterward

    print(player1.name, player1.health)
    print(player2.name, player2.health)

main()

---

    # CONSTRUCTOR WITH DEFAULT ARGUMENTS + PRIVATE MEMBER VARIABLES
    # ✅ Can use defaults OR provide your own starting values
    # ❌ Private variables should NOT be changed directly from outside the class
    # ✅ Getter = reads/returns a private variable
    # ✅ Setter = changes a private variable
    def __init__(self, name="Unknown", health=100):
        self.__name = name
        self.__health = health

    # GETTERS
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # SETTERS
    def setName(self, name):
        self.__name = name

    def setHealth(self, health):
        self.__health = health

def main():
player1 = Player("Tony", 100)

    # Read private variables using getters
    print(player1.getName())
    print(player1.getHealth())

    # Change private variables using setters
    player1.setName("Gu")
    player1.setHealth(200)

    # player1.__health = 500  ❌ Don't directly change private member variables

    print(player1.getName())
    print(player1.getHealth())

main()
