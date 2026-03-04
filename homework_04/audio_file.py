class AudioFile(MediaFile):
    def __init__(self, name, size, created_date, owner, duration, bitrate, format):
        # Вызываем конструктор родительского класса
        super().__init__(name, size, created_date, owner)
        # Добавляем специфичные для аудио атрибуты
        self.duration = duration  # длительность в секундах
        self.bitrate = bitrate  # битрейт
        self.format = format  # формат (mp3, wav и т.д.)

        # Добавляем в метаданные
        self.metadata['duration'] = duration
        self.metadata['bitrate'] = bitrate
        self.metadata['format'] = format

    # Переопределяем метод get_info
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, аудио: {self.duration}сек, {self.bitrate}kbps, {self.format}"

    # Специфичный для аудио метод
    def convert_to(self, new_format):
        """Конвертировать в другой формат"""
        print(f"Конвертация {self.name} из {self.format} в {new_format}")
        # Создаем новый объект с новым форматом
        new_file = AudioFile(
            self.name.replace(f".{self.format}", f".{new_format}"),
            self.size,
            self.created_date,
            self.owner,
            self.duration,
            self.bitrate,
            new_format
        )
        return new_file