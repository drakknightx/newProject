
import random
import string


def getCode(length = 10, char = string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation):
    try:
      crtPass = "".join(random.choice( char) for x in range(length))
      print 'Use The Password in side the '
      return crtPass

    except TypeError:
        print'Incorrect parameter'
        
    
    """
    This is a Alphanumeric Password Genarator
    it is default setting is for 10 characters
    you can enter the any other length you desire
    """
