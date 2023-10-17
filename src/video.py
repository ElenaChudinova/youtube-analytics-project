from googleapiclient.discovery import build
import os


class Video:

    def __init__(self, video_id):
        self.video_id = video_id
        self.video = self.get_service().videos().list(id=video_id, part='snippet,statistics').execute()
        self.video_title = self.video['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/video/'
        self.view_count = self.video['items'][0]['statistics']['viewCount']
        self.like_count = self.video['items'][0]['statistics']['likeCount']


    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=os.environ.get('API-KEY-YT'))

    def __str__(self):
        return f'{self.video_title}'

    def get_video(self):
        return self.video



class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id



    def get_playlist_id(self):
        playlist_videos = self.get_service().playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        return playlist_videos




