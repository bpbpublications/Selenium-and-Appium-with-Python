import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")

base_url = config.get('urls', 'base_url')
login_url = config.get('urls', 'login_url')

username_qa = config.get('credentials', 'username')
password_qa = config.get('credentials', 'username')


"""
In the code we first create a configparser object and call the method "read()" to read the contents of config.ini file. Then the
"get()" method of configparser is used to retrieve the values of the parameters as string type added in .ini file, that can be used in the test code.

"""