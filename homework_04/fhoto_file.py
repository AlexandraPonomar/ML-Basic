class PhotoFile:
    '''Класс для фото файлов'''
    def __init__(self, path, filename, data, owner ):
        self.path = path
        self.filename = filename
        self.data = data
        self.owner = owner

    def getPath(self):
        return self.path
    def SizeFile(self):
        return Path(self.path).stat().st_size
    def getInfo(self):
        return (self.path, self.filename, self.data, self.owner)

    def Save(self):
        with open(self.path, "wb") as file:
            file.write(self.data)