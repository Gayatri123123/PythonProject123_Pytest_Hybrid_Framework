import configparser


config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    #commerce
    @staticmethod
    def getApplicationURL1_of_comm():
        url = config.get('common info','comm_baseurl')
        return url
    #Magic Bricks
    @staticmethod
    def getMBApplicationURL_of_MB():
        mb_url = config.get('common info','MB_URL')
        return mb_url

    @staticmethod
    def getUseremail():
        username = config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password
