import pafy
from json import load
from database import lista_videos
from database import update_video

with open("coleta-youtube/config.json") as jsonfile:
    config = load(jsonfile)['youtube']

pafy.set_api_key(config["key"])

videos = lista_videos(False)
for video in videos:
	try:
		source = pafy.new(video.yt_video_id, gdata=True)
		print(source)

		update_video(source)
	except:
		print("removido: " + video.yt_video_id)
		print()