emotion = {'happy':0.4,'sad':0.9,'exicted':0.5,'xeutral':0.7}
dominent_emotion = max(emotion)
print(f"output without get key {dominent_emotion}")

emotion1 = {'happy':0.4,'sad':0.9,'exicted':1,'xeutral':0.7}
dominent_emotion1 = max(emotion1,key=emotion1.get)
print(f"output with get key {dominent_emotion1}")
