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
