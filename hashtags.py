import functions as func

def normalize_hashtags(hashtag):
    hashtag = hashtag.casefold()
    hashtag = hashtag.replace("__", "_")
    hashtag = hashtag.replace("ー","")
    hashtag = hashtag.replace("-","")
    return hashtag

class Hashtags:
    def __init__(self, file):
        data = func.read_json_file(file)
        self.keys = []
        self.values = {}
        for indx, row in enumerate(data):
            self.keys.append(row['key'])
            for hashtag in row['similares']:
                self.values[normalize_hashtags(hashtag)] = indx
        
    def get_key_hashtag(self,hashtag):
        key_hashtag = None
        hashtag = normalize_hashtags(hashtag)
        if(hashtag in self.values):
            index = self.values[hashtag]
            key_hashtag = self.keys[index]
        return key_hashtag
    
    def get_all_key_hashtags(self):
        return self.keys

    