
from .JekyllPost import * 
import os 

class JekyllPostContainer:
    def __init__(self, dir_path):
        self.posts = list([JekyllPost(dir_path + "/" + filename) for filename in os.listdir(dir_path)])
    
    def get_posts(self):
        return self.posts