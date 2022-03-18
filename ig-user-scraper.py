from gpg import Data
import instaloader
import pandas as pd
import time
import getpass
import os
import sys

print('Loading Script:')
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")

print("Mengambil Data Comments Semua Postingan Instagram Username")

user_name = input("Username : ")

print("Login Instagram (Gunakan Akun Smurf)")

user_login = input("Username Login : ")
user_pass = getpass.getpass("Password Login : ")

username = user_name
L = instaloader.Instaloader(max_connection_attempts=0)
L.login(user_login, user_pass)

L.load_session_from_file(user_login)

profile = instaloader.Profile.from_username(L.context, username)

usernamelist = [None]
captionlist = [None]
hashtaglist = [None]
likeslist = [None]
commentlist = [None]
followerlist = [None]

count = 1
for post in profile.get_posts():
        print("Data dari " + username + ", postingan ke " + str(count) + " dari " + str(profile.mediacount) + ".")
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

        usernamelist.append(username)
        captionlist.append(caption)
        hashtaglist.append(hashtag)
        likeslist.append(likes)
        commentlist.append(comments)
        count = count+1
        
pd.options.display.max_colwidth = 100
data = pd.DataFrame({"Account":usernamelist, "Post":captionlist, "Tag":hashtaglist, "Likes":likeslist,  "Comments":commentlist})
timestring = time.strftime("%Y%m%d_%H%M%S")
path =r'hasil/'
nama_file = os.path.join(path, "Dataset_" + username + "_" + timestring + ".csv")
data.to_csv(nama_file)
print("Dataset_" + username + "_" + timestring + ".csv")
print("DONE!!! Check csv file di Directori hasil")