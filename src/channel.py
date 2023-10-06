import json
import os

from googleapiclient.discovery import build

import isodate


# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('API-KEY-YT')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


'''
получить данные о канале по его id
docs: https://developers.google.com/youtube/v3/docs/channels/list

сервис для быстрого получения id канала: https://commentpicker.com/youtube-channel-id.php
'''
# channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'  # MoscowPython
channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'  # HighLoad Channel
channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = channel

    def print_info(self) -> str:
        """Выводит в консоль информацию о канале."""
        return self.channel


