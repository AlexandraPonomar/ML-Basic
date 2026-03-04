class MediaFile:
    def __init__(self, name, size, created_date, owner):
        self.name = name
        self.size = size
        self.created_date = created_date
        self.owner = owner
        self.metadata = {}  # словарь, для хранения доп. информации

    def get_info(self):
        """Получить базовую информацию о файле"""
        return f"Файл: {self.name}, размер: {self.size}MB, владелец: {self.owner}"

    def rename(self, new_name):
        """Переименовать файл"""
        old_name = self.name
        self.name = new_name
        print(f"Файл {old_name} переименован в {new_name}")

    def save(self, destination):
        """Сохранить файл (заглушка)"""
        print(f"Сохранение {self.name} в {destination}")
        return True

    def delete(self):
        """Удалить файл (заглушка)"""
        print(f"Удаление файла {self.name}")
        return True