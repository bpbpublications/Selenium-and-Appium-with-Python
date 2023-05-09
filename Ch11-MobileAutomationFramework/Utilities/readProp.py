import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")

username_qa = config.get('credentials', 'username')
password_qa = config.get('credentials', 'username')


contactName = config.get('ContactUsFrom', 'name')
contactEmail = config.get('ContactUsFrom', 'email')
contactAddress = config.get('ContactUsFrom', 'address')
contactPhone = config.get('ContactUsFrom', 'phone')