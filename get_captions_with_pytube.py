import time
from pytube import YouTube
from database import lista_videos
import xml.etree.ElementTree as ElementTree

videos = lista_videos(True, 360)
# print(len(videos))

# yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
# yt.bypass_age_gate()

# caption = yt.captions.get_by_language_code('en')
# print(caption.xml_captions)
# print(caption.generate_srt_captions())


for video in videos:
	source = YouTube('https://www.youtube.com/watch?v=' + video.yt_video_id)
	try:
		source.bypass_age_gate()
		if 'a.pt' in source.captions:
			caption = source.captions['a.pt']
			

			#caption_convert_to_srt = caption.generate_srt_captions()
			tree =  ElementTree.fromstring(caption.xml_captions)
			caption_convert_to_srt = ElementTree.tostring(tree, encoding='unicode', method='text')

			# save the caption to a file named Output.txt
			text_file = open("coleta-youtube/captions/"+video.yt_video_id + ".txt", "w", encoding="utf8")
			text_file.write(caption_convert_to_srt)
			text_file.close()

	except Exception as e:
		print(e)
		pass

	# print(source.captions)

	
