
import requests



class API():
    def __init__(self, id,url):
        self.url = url
        self.id = id
    
    def get(self):
        return requests.get(self.url).json()

    
        

if __name__ == "__main__":
    API = API(1,"http://192.168.1.30/node/1")
    print(API.get())