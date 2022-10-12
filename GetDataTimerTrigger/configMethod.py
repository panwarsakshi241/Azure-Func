from configparser import ConfigParser


# class Methods:

def db_params(parameter):

    # config method to read the db parameters from the config file.

    config = ConfigParser()
    config.read('config.ini')
    paramValue = config['db_params'][parameter]
    return paramValue

def fileversion(parameter):

    # config method to read the file version from the config file.

    config = ConfigParser()
    config.read('config.ini')
    paramValue = config['file_version'][parameter]
    return paramValue

def BaiFileCode(parameter):

    # Config method to read the Bai file codes.

    config = ConfigParser()
    config.read('config.ini')
    paramValue = config['BaiFileCodes'][parameter]
    return paramValue
