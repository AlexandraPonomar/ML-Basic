class main:
    def __init__(self):
        print("=== СОЗДАНИЕ ФАЙЛОВ ===\n")

        # Создаем разные медиа-файлы
        song = AudioFile(
            name="YONAKA_Guilty.mp3",
            size=5,
            created_date="2000-11-23",
            owner="Саничка",
            duration=180,
            bitrate=320,
            format="mp3"
        )

        video = VideoFile(
            name="бельтайн.mp4",
            size=500,
            created_date="2024-05-04",
            owner="Саничка",
            duration=3600,
            resolution="1920x1080",
            fps=60
        )

        photo = PhotoFile(
            name="Юки.jpg",
            size=5,
            created_date="2020-12-30",
            owner="Саня",
            resolution="4000x3000",
            camera="honor 40",
            location="Ульяновск"
        )

        # Получаем информацию о файлах
        print(song.get_info())
        print(video.get_info())
        print(photo.get_info())

        print("\n=== ОБНОВЛЕНИЕ ФАЙЛОВ ===\n")

        # Переименовываем файл
        photo.rename("малышка_юки.jpg")

        # Добавляем метаданные
        photo.metadata['tags'] = ['собака', 'снег', 'зима']
        print(f"Обновлены метаданные фото: {photo.metadata}")

        print("\n=== ДЕЙСТВИЯ С ФАЙЛАМИ ===\n")

        # Конвертируем аудио
        converted_song = song.convert_to("wav")
        print(f"Создан конвертированный файл: {converted_song.name}")

        # Извлекаем аудио из видео
        extracted_audio = video.extract_audio()
        print(f"Извлечено аудио: {extracted_audio.name}")

        # Изменяем размер фото
        resized_photo = photo.resize("1920x1080")
        print(f"Изменен размер фото: {resized_photo.name}")

        print("\n=== РАБОТА С ХРАНИЛИЩАМИ ===\n")

        # Работа с локальным хранилищем
        local = LocalStorage("/мои_файлы/")
        local.upload(song)
        local.upload(video)
        print(f"Файлы в локальном хранилище: {local.list_files()}")

        # Работа с облаком
        cloud = CloudStorage("Яндекс Диск", "euxa2017@yandex.ru")
        cloud.upload(photo)
        cloud.upload(converted_song)
        print(f"Файлы в облаке: {cloud.list_files()}")

        # Работа с S3
        s3 = S3Storage("my-media-bucket")
        s3.upload(video)
        s3.upload(extracted_audio)
        print(f"Файлы в S3: {s3.list_files()}")

        print("\n=== УДАЛЕНИЕ ФАЙЛОВ ===\n")

        # Удаляем файлы из разных хранилищ
        local.delete("YONAKA_Guilty.mp3")
        cloud.delete("Юки.jpg")
        s3.delete("бельтайн.mp4")

        print(f"\nОсталось в локальном: {local.list_files()}")
        print(f"Осталось в облаке: {cloud.list_files()}")
        print(f"Осталось в S3: {s3.list_files()}")
