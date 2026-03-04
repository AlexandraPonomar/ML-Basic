
from datetime import datetime
import os


class MediaFile(ABC):
    """Базовый класс для всех медиа-файлов"""

    def __init__(self, path, name, owner):
        self.path = path
        self.name = name
        self.owner = owner
        self.created_at = datetime.now()
        self.modified_at = datetime.now()
        self.metadata: Dict[str, Any] = {}

    def get_info(self) -> str:
        """Получить основную информацию о файле"""
        pass

    def get_size(self) -> int:
        """Получить размер файла """
        return 0

    def rename(self, new_name: str) -> None:
        """Переименовать файл"""
        self.name = new_name
        self.modified_at = datetime.now()
        print(f"Файл переименован в {new_name}")

    def save(self, destination: str) -> bool:
        """Сохранить файл по указанному пути"""
        pass

    def delete(self) -> bool:
        """Удалить файл"""
        pass

    def update_metadata(self, key: str, value: Any) -> None:
        """Обновить метаданные файла"""
        self.metadata[key] = value
        self.modified_at = datetime.now()