class PhotoFile(MediaFile):
    def __init__(self, name, size, created_date, owner, resolution, camera, location):
        super().__init__(name, size, created_date, owner)
        self.resolution = resolution
        self.camera = camera
        self.location = location

        self.metadata['resolution'] = resolution
        self.metadata['camera'] = camera
        self.metadata['location'] = location

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, фото: {self.resolution}, камера: {self.camera}, место: {self.location}"

    # Специфичный для фото метод
    def resize(self, new_resolution):
        """Изменить размер фото"""
        print(f"Изменение размера {self.name} с {self.resolution} на {new_resolution}")
        new_photo = PhotoFile(
            f"resized_{self.name}",
            self.size // 2,  # примерно в 2 раза меньше размер
            self.created_date,
            self.owner,
            new_resolution,
            self.camera,
            self.location
        )
        return new_photo