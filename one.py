import urllib.request
def ONE():
    

    def connect(host='http://google.com'):
        try:
            urllib.request.urlopen(host) #Python 3.x
            return True
        except:
            return False
# test
    print( "Internet connected" if connect() else "no internet!" )