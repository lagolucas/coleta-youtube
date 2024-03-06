import os
import re
from database import insere_captions
from database import insere_video




for folder in os.listdir('coleta-youtube/captions/'):
	for filename in os.listdir(os.path.join('coleta-youtube/captions/')):
		with open(os.path.join('coleta-youtube/captions/', filename), 'r', encoding="utf8") as f:
			
			insere_video(filename.split('.')[0])
			data = f.read()
			a = []
			b = {}
			for line in data.splitlines():
				if line:
					a.append(line)

			print(folder)	
			print(filename.split('.')[0])
			insere_captions(a, filename.split('.')[0])
		
		# os.remove(os.path.join('captions', filename))

