import module

module.do_nothing("hello")

print ("Starting")

from pytube import YouTube 
url="https://www.youtube.com/watch?v=VsoGP_Gm-YQ" 
my_video = YouTube(url) 
print ("getting title")
print(my_video.title)

print ("getting thumbnail")
print(my_video.thumbnail_url)
