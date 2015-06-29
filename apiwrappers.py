import urllib.parse
import urllib.request
import json

class APIBase:
    @staticmethod
    def _get(url, headers={}):
        try:
            req = urllib.request.Request(url, None, headers)
            response = urllib.request.urlopen(req)
        except Exception as e:
            return None

        try:
            return response.read().decode('utf-8')
        except Exception as e:
            print(e)
            return None

        return None

    def getraw(self, endpoints, parameters={}):
        url = self.base_url + '/'.join(endpoints) + ('' if len(parameters) == 0 else '?'+urllib.parse.urlencode(parameters))

        return APIBase._get(url, self.headers)

    def get(self, endpoints, parameters={}):
        try:
            data = self.getraw(endpoints, parameters)
            if data:
                return json.loads(data)
            else:
                return data
        except Exception as e:
            print(e)
            return None

        return None

class ChatDepotAPI(APIBase):
    def __init__(self):
        APIBase.__init__(self)

        self.base_url = 'http://chatdepot.twitch.tv/'

        self.headers = {
                'Accept' : 'application/vnd.twitchtv.v3+json'
                }

class ImraisingAPI(APIBase):
    def __init__(self, apikey):
        APIBase.__init__(self)

        self.base_url = 'https://imraising.tv/api/v1/'

        self.headers = {
                'Authorization' : 'APIKey apikey="{0}"'.format(apikey),
                'Content-Type' : 'application/json',
                }

class StreamtipAPI(APIBase):
    def __init__(self, client_id, access_token):
        APIBase.__init__(self)

        self.base_url = 'https://streamtip.com/api/'

        self.headers = {
                'Authorization' : client_id + ' ' + access_token,
                }

class TwitchAPI(APIBase):
    def __init__(self, client_id, oauth, type='kraken'):
        APIBase.__init__(self)

        self.base_url = 'https://api.twitch.tv/{0}/'.format(type)

        self.headers = {
                'Accept': 'application/vnd.twitchtv.v3+json',
                'Client-ID': client_id,
                'Authorization': 'OAuth ' + oauth
                }