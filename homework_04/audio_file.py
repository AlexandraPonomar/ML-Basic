class AudioFile(MediaFile):
    """Класс для аудиофайлов"""

    def __init__(self, path: str, name: str, owner: Optional[str] = None,
                 duration: Optional[int] = None, bitrate: Optional[int] = None):
        super().__init__(path, name, owner)
        self.duration = duration  # длительность в секундах
        self.bitrate = bitrate  # битрейт в kbps
        self.format = self._detect_format()

        # Специфичные для аудио метаданные
        self.metadata.update({
            'duration': duration,
            'bitrate': bitrate,
            'format': self.format
        })

    def _detect_format(self) -> str:
        """Определить формат файла по расширению"""
        ext = os.path.splitext(self.name)[1].lower()
        formats = {'.mp3': 'MP3', '.wav': 'WAV', '.flac': 'FLAC', '.aac': 'AAC'}
        return formats.get(ext, 'Unknown')

    def get_info(self) -> str:
        return f"Аудиофайл: {self.name}, длительность: {self.duration}с, битрейт: {self.bitrate} kbps"

    def convert(self, target_format: str) -> 'AudioFile':
        """
        Конвертировать аудиофайл в другой формат
        Возвращает новый объект AudioFile с конвертированным файлом
        """
        print(f"Конвертация {self.name} из {self.format} в {target_format}")
        # Здесь была бы логика конвертации
        new_name = f"{os.path.splitext(self.name)[0]}.{target_format.lower()}"
        converted_file = AudioFile(self.path, new_name, self.owner, self.duration, self.bitrate)
        return converted_file

    def save(self, destination: str) -> bool:
        print(f"Сохранение аудиофайла {self.name} в {destination}")
        return True

    def delete(self) -> bool:
        print(f"Удаление аудиофайла {self.name}")
        return True