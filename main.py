import sys
from matplotlib import pyplot as plt


class FileManager:
    def __init__(self):
        pass

    def readFile(self, path):
        self.list = []
        self.file = open(path, "r")
        for line in self.file:
            self.list.append(line.strip("\n"))
        return self.list
        self.file.close()

    def writeFile(self, data, path):
        self.file = open(path, "w")
        self.file.write(data)
        self.file.close()

    def appendFile(self, data, path):
        self.file = open(path, "a")
        self.file.write(data)
        self.file.close()


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


class InputFunctions:
    def __init__(self):
        self.fm = FileManager()
        self.fileData = self.fm.readFile("data/DATA.txt")

    def AddStock(self, title):
        writeData = ""
        value = int(input("Amount of stock being added: "))
        newData = []
        for i in self.fileData[2:]:
            newData.append(i.split(", "))
        for i in range(len(newData)):
            if newData[i][1] == title:
                newData[i][5] = str(int(newData[i][5]) + value)
        print("Outcome:\n\nARTIST, TITLE, GENRE, PLAY LENGTH, CONDITION, STOCK, COST")
        for i in newData:
            print(', '.join(i))
        writeData += "#Listing showing sample record details\n#ARTIST, TITLE, GENRE, PLAY LENGTH, CONDITION, STOCK, COST\n"
        for i in newData:
            writeData += ', '.join(i)
            writeData += "\n"
        self.fm.writeFile(writeData, "data/DATA.txt")
        self.fileData = self.fm.readFile("data/DATA.txt")

    def RemoveStock(self, title):
        writeData = ""
        value = int(input("Amount of stock being removed: "))
        newData = []
        for i in self.fileData[2:]:
            newData.append(i.split(", "))
        for i in range(len(newData)):
            if newData[i][1] == title:
                newData[i][5] = str(int(newData[i][5]) - value)
                if int(newData[i][5]) <= 0:
                    newData[i][5] = "0"
                    print("Note: this will result in {} being out of stock.".format(title))
        print("Outcome:\n\nARTIST, TITLE, GENRE, PLAY LENGTH, CONDITION, STOCK, COST")
        for i in newData:
            print(', '.join(i))
        writeData += "#Listing showing sample record details\n#ARTIST, TITLE, GENRE, PLAY LENGTH, CONDITION, STOCK, COST\n"
        for i in newData:
            writeData += ', '.join(i)
            writeData += "\n"
        self.fm.writeFile(writeData, "data/DATA.txt")
        self.fileData = self.fm.readFile("data/DATA.txt")

    def AddRecord(self):
        writeData = ""
        artist = input("Enter the arist name: ")
        title = input("Enter the title name: ")
        genre = input("Enter the genre name: ")
        playLength = input("Enter the play length: ")
        condition = input("Enter condition: ")
        stock = input("Enter stock: ")
        cost = input("Enter cost: ")
        writeData += ("\n" + artist + ", " + title + ", " + genre + ", " + playLength + ", " + condition + ", " + stock + ", " + cost)
        self.fm.appendFile(writeData, "data/DATA.txt")
        self.fileData = self.fm.readFile("data/DATA.txt")



class Menu:
    def __init__(self):
        self.out = OutputFunctions()
        self.ipt = InputFunctions()

    def MainMenu(self):  # Void function.
        print("WELCOME TO VIRTUAL VINYL!\n")
        print("Please select an option:\n1. Query data.\n2. Add a new record.\n3. Quit.")

        try:
            choice = int(input("\nEnter choice: "))
        except ValueError:
            print("\nError: The data type you have entered is invalid.\n")  # Warning the user if the input isn't of type int.
            self.MainMenu()

        if choice == 1:
            self.OutputMenu()
        elif choice == 2:
            self.ipt.AddRecord()
            self.out.Refresh()
            self.out.SummaryReport()
            self.out.TotalTitles()
            self.out.TotalValue()
            self.QuitMenu()
        elif choice == 3:
            sys.exit()
        else:
            print("\nError: Number should be only 1, 2 or 3.\n")  # If the type is int, but isn't 1, 2 or 3.
            self.MainMenu()  # Calling the function inside itself to bring us back to the start of the function.

        print("\nInvalid input.\n")
        self.MainMenu()

    def OutputMenu(self):  # Void function.
        print("\nPlease select an option:\
            \n1. Summary report.\
            \n2. Record titles within a price threshold.\
            \n3. Records by genre.\
            \n4. Query availability.\
            \n5. Bar Chart")

        try:
            choice = int(input("\nEnter choice: "))
        except ValueError:
            print("\nError: The data type you have entered is invalid.")
            self.OutputMenu()

        if choice == 1:
            self.out.SummaryReport()
            self.out.TotalTitles()
            self.out.TotalValue()
            self.QuitMenu()
        elif choice == 2:
            self.out.PriceThreshold()
            self.QuitMenu()
        elif choice == 3:
            self.out.GenreType()
            self.QuitMenu()
        elif choice == 4:
            self.out.QueryByTitle(self)
            self.out.Refresh()
            self.QuitMenu()
        elif choice == 5:
            self.out.BarChart()
            self.QuitMenu()
        else:
            print("Error: Number should be only 1, 2, 3, 4 or 5.")
            self.OutputMenu()

    def QuitMenu(self):  # Allows the user to quit the program after calling a function.
        print("\n-------------------------------------------")
        print("\nWould you like to return to the main menu, or quit?\n\n1. Return to main menu.\n2. Quit.")

        choice = int(input("Enter choice: "))

        if choice == 1:
            self.MainMenu()
        if choice == 2:
            sys.exit()


app = Menu()
app.MainMenu()
