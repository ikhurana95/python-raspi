from sense_hat import SenseHat 
from datetime import datetime 

s = SenseHat() 


while True: 
	time_now = datetime.now().time() 
	time_now_string = str(time_now) 
	time_now_string_truncated = time_now_string[0:5] 
	s.show_message(time_now_string_truncated, 0.05, text_c 
	olour=[255,0,0]) 
