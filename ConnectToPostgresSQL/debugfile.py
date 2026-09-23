import configparser
filename='textforconnection.ini'
parser = configparser.ConfigParser()
print(filename)
print(parser.read(filename))