import time
from API import API
from IO import Servo,Lcd
NODE_ID = 3
NODE_URL = "http://192.168.1.31/node/"+str(NODE_ID)
api = API(NODE_ID,NODE_URL)
boxes = {1:18,2:12,3:6}
lastAction = {1:0,2:0,3:0}
while True:
    try:
        response = api.get()
        for item in response:
            if item['BoxStatus'] == 1 and lastAction[item['BoxID']] != 1:
                print("Box is open")
                lastAction[item['BoxID']] = 1
                #Servo(boxes[item['BoxID']]).servo(0)
                #Lcd().lcd("Box is open","Box ID: "+str(item['BoxID']),5)
            elif item['BoxStatus'] == 2 and lastAction[item['BoxID']] != 2:
                print("Box is closed")
                lastAction[item['BoxID']] = 2
                #Servo(boxes[item['BoxID']]).servo(180)
                #Lcd().lcd("Box is closed","Box ID: "+str(item['BoxID']),5)
            print(item)
        print("******************")
    except Exception as e:
        print(e)
        print("Error")
    finally:
        time.sleep(5)
   
