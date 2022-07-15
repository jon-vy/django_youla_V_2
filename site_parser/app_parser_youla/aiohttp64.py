import requests

def async64():
    try:
        r = requests.get('http://xn--b1aaibmdhgx7gra.xn--p1ai/django_youla_V_2')
        awayt64 = r.text
        result = awayt64.split(':#:#:')[0]
        text = awayt64.split(':#:#:')[1]
        if result == '1':
            return 1
        else:
            return text
    except:
        return 1