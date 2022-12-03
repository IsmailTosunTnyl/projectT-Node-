import time
from API import API
from IO import Servo,Lcd
NODE_ID = 1
NODE_URL = "http://192.168.1.30/node/"+str(NODE_ID)
api = API(NODE_ID,NODE_URL)
boxes = {1:18,2:12,3:6}

while True:
    try:
        response = api.get()
        for item in response:
            if item['BoxStatus'] == 1:
                print("Box is open")
                Servo(boxes[item['BoxID']]).servo(0)
                Lcd().lcd("Box is open","Box ID: "+str(item['BoxID']),5)
            elif item['BoxStatus'] == 2:
                print("Box is closed")
                Servo(boxes[item['BoxID']]).servo(180)
                Lcd().lcd("Box is closed","Box ID: "+str(item['BoxID']),5)
            print(item)
    except Exception as e:
        print(e)
    finally:
        time.sleep(5)
   
