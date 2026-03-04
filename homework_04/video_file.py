class VideoFile(MediaFile):
    def __init__(self, name, size, created_date, owner, duration, resolution, fps):
        super().__init__(name, size, created_date, owner)
        self.duration = duration
        self.resolution = resolution  # например "1920x1080"
        self.fps = fps  # кадры в секунду

        self.metadata['duration'] = duration
        self.metadata['resolution'] = resolution
        self.metadata['fps'] = fps

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, видео: {self.resolution}, {self.fps}fps, {self.duration}сек"

    # Специфичный для видео метод
    def extract_audio(self):
        """Извлечь аудиодорожку"""
        print(f"Извлечение аудио из видео {self.name}")
        # Создаем аудиофайл из видео
        audio = AudioFile(
            f"audio_from_{self.name}.mp3",
            self.size // 10,  # примерно 10% от размера видео
            self.created_date,
            self.owner,
            self.duration,
            128,  # стандартный битрейт
            "mp3"
        )
        return audio
