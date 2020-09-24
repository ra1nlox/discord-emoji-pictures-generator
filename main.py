import configparser

config = configparser.ConfigParser()
config.read('config.ini')

emoji1 = config(['emojis']['emoji1'])
emoji2 = config(['emojis']['emoji2'])
emoji3 =config(['emojis']['emoji3'])