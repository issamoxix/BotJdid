import re 
class Brain:
    def __init__(self, client):
        self.client = client
        self.members = {}
        self.channels = {}

    def set_brain(self):
        if not self.client:
            raise Exception("Client not functioning !")
        self._get_channels()
        self._get_members()

    def _get_members(self):
        for member in self.client.get_all_members():
            self.members[member.id] = member

    def _get_channels(self):
        for channel in self.client.get_all_channels():
            self.channels[channel.id] = channel
    
    def get_id_from_mention(self,mention):
        return int(re.search(r'\d+',mention).group())
