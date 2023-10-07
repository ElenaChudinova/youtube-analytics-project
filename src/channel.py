import json
import os

from googleapiclient.discovery import build

import isodate

class Channel:
    """Класс для ютуб-канала"""

    api_key = os.environ.get('API-KEY-YT')

    def __init__(self, channel_id):
        self.channel_id = channel_id


    def get_service(self):
        service = build('youtube', 'v3', developerKey=self.api_key)
        return service

    def get_info(self):
        youtube = self.get_service()
        response = youtube.channels().list(id=self.channel_id,part='snippet,statistics').execute()
        return response

    def print_info(self):
        response = self.get_info()
        print(json.dumps(response, indent=2, ensure_ascii=False))




