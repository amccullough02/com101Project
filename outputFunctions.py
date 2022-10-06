from matplotlib import pyplot as plt
from fileManager import FileManager
from inputFunctions import InputFunctions


class OutputFunctions:
    def __init__(self):
        self.fm = FileManager()
        self.fileData = self.fm.readFile("data/DATA.txt")
        self.ipt = InputFunctions()

    def Refresh(self):
        self.fileData = self.fm.readFile("data/DATA.txt")

    def SummaryReport(self):

        print("=== Summary Report ===\n")
        for i in self.fileData[1:]:  # A useful to start at a non-zero index when iterating over a list.
            print(i)

    def newData(self):
        newData = []
        for i in self.fileData[2:]:
            newData.append(i.split(", "))
        return newData

    def TotalTitles(self):
        total = 0
        newData = []
        for i in self.fileData[2:]:
            newData.append(i.split(", "))
        for i in range(len(newData)):
            total += int(newData[i][5])
        print("\nThe total number of records available: {}".format(total))

    def TotalValue(self):
        cost = 0
        newData = []
        for i in self.fileData[2:]:
            newData.append(i.split(", "))
        for i in range(len(newData)):
            cost += float(newData[i][6])
        cost = round(cost, 2)
        print("\nThe total value of records available: {}".format(cost))

    def PriceThreshold(self):
        price = float(input("\nEnter minimum price threshold: "))
        price = round(price, 2)
        validData = []
        newData = []
        for i in self.fileData[2:]:
            newData.append(i.split(", "))
        for i in range(len(newData)):
            if float(newData[i][6]) > price:
                validData.append(newData[i])
        print("\nARTIST, TITLE, GENRE, PLAY LENGTH, CONDITION, STOCK, COST\n")
        for i in validData:
            print(', '.join(i))

    def GenreType(self):
        newData = []
        validData = []
        print("Select genre:\n1. Rock\n2. Classical\n3. Pop\n4. Jazz\n5. Spoken Word")
        try:
            choice = int(input("\nEnter option: "))
        except ValueError:
            print("\nError: The data type you have entered is invalid.\n")
            self.GenreType()
        genre = ""
        if choice == 1:
            genre = "Rock"
        elif choice == 2:
            genre = "Classical"
        elif choice == 3:
            genre = "Pop"
        elif choice == 4:
            genre = "Jazz"
        elif choice == 5:
            genre = "Spoken Word"
        else:
            print("\nInvalid selection.\n")
            self.GenreType()
        for i in self.fileData[2:]:
            newData.append(i.split(", "))
        for i in range(len(newData)):
            if newData[i][2] == genre:
                validData.append(newData[i])
        print("\nARTIST, TITLE, GENRE, PLAY LENGTH, CONDITION, STOCK, COST\n")
        for i in validData:
            print(', '.join(i))

    def QueryByTitle(self, menu):
        newData = []
        title = input("\nEnter title name: ")
        for i in self.fileData[2:]:
            newData.append(i.split(", "))
        for i in range(len(newData)):
            if newData[i][1] == title:
                if int(newData[i][5]) > 0:
                    print("{} is available.".format(title))
                else:
                    print("{} is currently out of stock.".format(title))
                print("Match found.\n1. Add stock.\n2. Remove stock.\n3. Return to main menu.")
                try:
                    choice = int(input("\nEnter choice: "))
                except ValueError:
                    print("\nError: The data type you have entered is invalid.\n")
                    self.QueryByTitle()
                if choice == 1:
                    self.ipt.AddStock(title)
                elif choice == 2:
                    self.ipt.RemoveStock(title)
                elif choice == 3:
                    menu.MainMenu()
                else:
                    print("\nInvalid selection.\n")
                break
            else:
                print("No match was found, returning you to main menu.\n")  # If the user entered a name that doesn't exist they 
                                                                            # will be sent back to the main menu.
                menu.MainMenu()

    def BarChart(self):
        rock = 0
        classical = 0
        pop = 0
        spokenWord = 0
        jazz = 0
        newData = []
        for i in self.fileData[2:]:
            newData.append(i.split(", "))
        for i in range(len(newData)):
            if newData[i][2] == "Rock":
                rock += int(newData[i][5])
            if newData[i][2] == "Pop":
                pop += int(newData[i][5])
            if newData[i][2] == "Jazz":
                jazz += int(newData[i][5])
            if newData[i][2] == "Classical":
                classical += int(newData[i][5])
            if newData[i][2] == "Spoken Word":
                spokenWord += int(newData[i][5])

        fig = plt.figure(figsize=(7, 5))
        stock = [rock, classical, pop, spokenWord, jazz]
        names = ["Rock", "Classical", "Pop", "Spoken Word", "Jazz"]
        positions = [0, 1, 2, 3, 4]

        plt.bar(positions, stock, width=0.5)
        plt.xticks(positions, names)
        plt.show()
