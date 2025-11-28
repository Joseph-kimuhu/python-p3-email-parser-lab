import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string
    
    def parse(self):
        tokens = re.split(r'[,\s]+', self.email_string)
        emails = [token for token in tokens if re.match(r'^[^@]+@[^@]+\.[^@]+$', token)]
        return sorted(list(set(emails)))