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

print("Mengambil Data Comments Menggunakan ID Postingan (https://www.instagram.com/p/ID_POSTINGAN/)")

user_name = input("Username : ")
postingan = input("Id Postingan : ")

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
shortcode = [None]

for post in profile.get_posts():
        post = post.from_shortcode(L.context, postingan)
        print("Data dari " + username + "(" + postingan + ")")
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
        shortcode.append(postingan)
        captionlist.append(caption)
        hashtaglist.append(hashtag)
        likeslist.append(likes)
        commentlist.append(comments)
        break
        
pd.options.display.max_colwidth = 100
data = pd.DataFrame({"Account":usernamelist, "ID Postingan":shortcode, "Post":captionlist, "Tag":hashtaglist, "Likes":likeslist, "Comments":commentlist})
timestring = time.strftime("%Y%m%d_%H%M%S")
path =r'hasil/'
nama_file = os.path.join(path, "Dataset_" + username + "(" + postingan + ")" + timestring + ".csv")
data.to_csv(nama_file)
print("Dataset_" + username + "(" + postingan + ")" + timestring + ".csv")
print("DONE!!! Check csv file di Directori hasil")