class VideoFile(MediaFile):
    """Класс для видеофайлов"""

    def __init__(self, path, name, owner, duration, resolution, fps):
        self.path = path
        self.name = name
        self.owner = owner
        self.duration = duration # длительность
        self.resolution = resolution  # например, "1920x1080"
        self.fps = fps  # кадров в секунду


    def get_info(self) -> str:
        return f"Видеофайл: {self.name}, разрешение: {self.resolution}, {self.fps}fps"

    def save(self, destination: str) -> bool:
        print(f"Сохранение видеофайла {self.name} в {destination}")
        return True

    def delete(self) -> bool:
        print(f"Удаление видеофайла {self.name}")
        return True