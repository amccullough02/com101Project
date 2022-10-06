from fileManager import FileManager


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
