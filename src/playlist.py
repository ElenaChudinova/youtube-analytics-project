import datetime
from googleapiclient.discovery import build
import os
import isodate

class PlayList:
    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.playlist = self.get_service().playlistItems().list(playlistId=playlist_id, part='contentDetails, snippet').execute()
        self.title = self.playlist['items'][0]['snippet']['title']
        self.url = "https://www.youtube.com/playlist/" + self.playlist["items"][0]['snippet']["playlistId"]


    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=os.environ.get('API-KEY-YT'))


    @property
    def total_duration(self):
        # Функция получает общую длительность видеороликов в плейлисте
        self.video_ids = [video['contentDetails']['videoId'] for video in self.playlist['items']]
        self.video_response = self.get_service().videos().list(part='contentDetails,statistics',
                                               id=','.join(self.video_ids)
                                               ).execute()
        if self.video_response is not None and 'items' in self.video_response:
            for video in self.video_response['items']:
                # YouTube video duration is in ISO 8601 format
                iso_8601_duration = video['contentDetails']['duration']
                duration = isodate.parse_duration(iso_8601_duration)
                print(duration)
                return datetime.timedelta


    def show_best_video(self):
        self.video_ids = [video['contentDetails']['videoId'] for video in self.playlist['items']]
        self.video_response = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=self.video_ids
                                               ).execute()
        like_count = self.video_response['items'][0]['statistics']['likeCount']
        max = like_count[0]
        for i in range(1, len(like_count)):
            if like_count[i] > max:
                max = like_count[i]
        return "https://youtu.be/" + f'{self.video_response['items'][0]['id']}'


