import json
import os

from googleapiclient.discovery import build

path = "./moscowpython.json"


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id):
        self.channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        self.__channel_id = channel_id
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.url = 'https://www.youtube.com/channel/' + self.channel["items"][0]["id"]
        self.subscriber_count = self.channel["items"][0]["statistics"]["subscriberCount"]

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __le__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __eq__(self, other):
        return int(self.subscriber_count) == int(other.subscriber_count)

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        if channel_id:
            raise 'AttributeError: запрещено'
        else:
            self.__channel_id = channel_id

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=os.environ.get('API-KEY-YT'))

    def get_info(self):
        youtube = self.get_service()
        response = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        return response

    def print_info(self):
        info_channel = {}
        response = self.get_info()
        info_channel['id канала'] = response["items"][0]["id"]
        info_channel['название канала'] = response["items"][0]["snippet"]["title"]
        info_channel['описание канала'] = response["items"][0]["snippet"]["description"]
        info_channel['ссылка на канал'] = 'https://www.youtube.com/channel/' + response["items"][0]["id"]
        info_channel['количество подписчиков'] = response["items"][0]["statistics"]["subscriberCount"]
        info_channel['количество видео'] = response["items"][0]["statistics"]["videoCount"]
        info_channel['количество просмотров'] = response["items"][0]["statistics"]["viewCount"]
        return info_channel

    def to_json(self, path):
        response = self.print_info()
        json_object = json.dumps(response, indent=2, ensure_ascii=False)
        with open(path, 'w', encoding='utf-8') as outfile:
            outfile.write(json_object)
            return json_object
