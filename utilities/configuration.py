import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('C:\\Users\\hemank\\PycharmProjects\\pythonProject4\\utilities\\properties.ini')
    return config
