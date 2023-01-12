
import requests



class API():
    def __init__(self, id,url):
        self.url = url
        self.id = id
    
    def get(self):
        return requests.get(self.url).json()

    
        

if __name__ == "__main__":
    api = API(3,"http://192.168.1.38/node/3")
    print(api.get())