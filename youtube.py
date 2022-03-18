from urllib import response
import requests
from apiclient.discovery import build
import sys
import os
import time

print('Loading Script:')
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")
user_input = input("Input Video ID (https://www.youtube.com/watch?v=VIDEO_ID): ")

stdoutOrigin=sys.stdout 
filename = 'log_youtube_'+user_input+'.txt'
sys.stdout = open(os.path.join('hasil/', filename), "w")

URL = 'https://www.googleapis.com/youtube/v3/'
#Enter API KEY here
API_KEY = 'AIzaSyARpEA5nl4hw7GFpGlBSO69Np6piY0h3Ho'
#Enter your Video ID here
VIDEO_ID = (user_input)

youtube = build('youtube', 'v3', developerKey=API_KEY)


results = youtube.videos().list(id=VIDEO_ID, part='snippet,statistics').execute()
for result in results.get('items', []):
    videoID   = print ('Video ID    = ' + result['id'])
    line      = print ('---------------------------------------------------')
    publish   = print ('Publish     = ' + result['snippet']['publishedAt'])
    line      = print ('---------------------------------------------------')
    views     = print ('Views       = ' + result['statistics']['viewCount'])
    line      = print ('---------------------------------------------------')
    likes     = print ('Likes       = ' + result['statistics']['likeCount'])
    line      = print ('---------------------------------------------------')
    #print ('Disliked    :' + result['statistics']['dislikeCount'])
    judul     = print ('Judul       = ' + result['snippet']['title'])
    line      = print ('---------------------------------------------------')
    deskripsi = print ('Deskripsi   =\n'+ result['snippet']['description'])
    line      = print ('---------------------------------------------------')
    comment   = print ('COMENT      = ' + result['statistics']['commentCount'])
    line      = print ('---------------------------------------------------')

def print_video_comment(video_id, next_page_token):
  params = {
    'key': API_KEY,
    'part': 'snippet',
    'videoId': video_id,
    'order': 'relevance',
    'textFormat': 'plaintext',
  }
  if next_page_token is not None:
    params['pageToken'] = next_page_token
  response = requests.get(URL + 'commentThreads', params=params)
  resource = response.json()

  for comment_info in resource['items']:
    user_name = print("Username     :",comment_info['snippet']['topLevelComment']['snippet']['authorDisplayName'])
    text      = print("Comment      :",comment_info['snippet']['topLevelComment']['snippet']['textDisplay'])
    like_cnt  = print("Comment Like :",comment_info['snippet']['topLevelComment']['snippet']['likeCount'])
    reply_cnt = print("Total Reply  :",comment_info['snippet']['totalReplyCount'])
    parentId  = comment_info['snippet']['topLevelComment']['id']
    print_video_reply(video_id, next_page_token, parentId)
    print('===========================================================')

  if 'nextPageToken' in resource:
    print_video_comment(video_id, resource["nextPageToken"])

def print_video_reply(video_id, next_page_token, id):
  params = {
    'key': API_KEY,
    'part': 'snippet',
    'videoId': video_id,
    'textFormat': 'plaintext',
    'parentId': id,
  }

  if next_page_token is not None:
    params['pageToken'] = next_page_token
  response = requests.get(URL + 'comments', params=params)
  resource = response.json()

  for comment_info in resource['items']:
    print("==>")
    user_name = print("Username Reply :",comment_info['snippet']['authorDisplayName'])
    text      = print("Reply          :",comment_info['snippet']['textDisplay'])
    like_cnt  = print("Reply Like     :",comment_info['snippet']['likeCount'])

  if 'nextPageToken' in resource:
    print_video_reply(video_id, resource["nextPageToken"], id)

video_id = VIDEO_ID
print_video_comment(video_id, None,)

sys.stdout.close()
sys.stdout=stdoutOrigin


print("DONE!!! Check txt file di Directori hasil")
