from cProfile import Profile
from gpg import Data
import instaloader
import pandas as pd
import time
import getpass
import os
import json
import sys

print('Loading Script:')
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")

print("Mengambil Data Comments Semua Postingan Instagram dari list Username")
print("Masukan Username pada file userlist.json")

data_json_file = ()
with open("userlist.json", 'r') as f:
	data_json_file = json.loads(f.read())

print("Login Instagram (Gunakan Akun Smurf)")

user_login = input("Username Login : ")
user_pass = getpass.getpass("Password Login : ")

L = instaloader.Instaloader(max_connection_attempts=0)
L.login(user_login, user_pass)

for loop_userlist in data_json_file:
    count = 1
    profile = instaloader.Profile.from_username(L.context, loop_userlist)

    usernamelist = []
    captionlist = []
    hashtaglist = []
    likeslist = []
    commentlist = []
    followerlist = []

    json_data = []
    for post in profile.get_posts():
        print("Data dari " + loop_userlist + ", postingan ke " + str(count) + " dari " + str(profile.mediacount) + ".")
        caption = post.caption
        if caption is None:
            caption = ""
        if caption is not None:
            caption = caption.encode('ascii', 'ignore').decode('ascii')
        hashtag = post.caption_hashtags
        likes = post.likes
        comments = []
        for comment in post.get_comments() :
            comments.append(comment.text.encode('ascii', 'ignore').decode('ascii'))

        usernamelist.append(loop_userlist)
        captionlist.append(caption)
        hashtaglist.append(hashtag)
        likeslist.append(likes)
        commentlist.append(comments)
        count = count+1

    pd.options.display.max_colwidth = 100
    data = pd.DataFrame({"Account":usernamelist, "Post":captionlist, "Tag":hashtaglist, "Likes":likeslist,  "Comments":commentlist})
    timestring = time.strftime("%Y%m%d_%H%M%S")
    path =r'hasil/'
    nama_file = os.path.join(path, "Dataset_" + loop_userlist + "_" + timestring + ".csv")
    data.to_csv(nama_file)
    print("Dataset_" + loop_userlist + "_" + timestring + ".csv")
    print("DONE!!! Check csv file di Directori hasil")
    
