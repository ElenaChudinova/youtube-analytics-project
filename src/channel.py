import json
import os

from googleapiclient.discovery import build

import isodate

class Channel:
    """Класс для ютуб-канала"""


    def __init__(self, channel_id):
        self.__channel_id = channel_id


    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=os.environ.get('API-KEY-YT'))


    @property
    def get_info(self):
        youtube = self.get_service()
        response = youtube.channels().list(id=self.__channel_id,part='snippet,statistics').execute()
        return response


    def print_info(self):
        response = self.get_info()
        return json.dumps(response, indent=2, ensure_ascii=False)



    def playlists_info(self):
        youtube = self.get_service()
        playlists = youtube.playlists().list(channelId=self.__channel_id,
                                             part='contentDetails,snippet',
                                             maxResults=50,
                                             ).execute()
        for i in playlists['items']:
            id_cannel = i['snippet']['channelId']
            title = i['snippet']['title']
            description = i['snippet']['description']
            channelTitle = i['snippet']['channelTitle']
            url = i['snippet']['thumbnails']['default']['url']
            itemCount = i['contentDetails']['itemCount']
            return id_cannel, title, description, channelTitle, url, itemCount

    def to_json(self):
        response = self.playlists_info()
        json_object = json.dumps(response, indent=2, ensure_ascii=False)
        with open("moscowpython.json", 'w') as outfile:
            outfile.write(json_object)
            return json_object
