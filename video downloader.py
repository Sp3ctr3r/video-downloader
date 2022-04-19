import youtube_dl

path = "__import__('os').environ['USERPROFILE']"

ydl_opts = {'outtmpl': path + 'Desktop/videolar/%(title)s-%(id)s.%(ext)s'}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['link'])