import jenkins
import matplotlib.pyplot as pit
import matplotlib
import time
import sys,getopt
from datetime import datetime
import numpy as np

class Durationmetrics:
    username = ""
    password = ""
    server = None

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def connectToJenkins(self):
        self.server = jenkins.
        user = self.server.

def main(argv):

    username = ""
    password = ""

    try:
        opts,args = getopt.getopt(argv, "hu:p", ["username=", "password="])
    except getopt.GetoptError:
        print('python jen_api_python -u <username> -p <password>')
        sys.exit(2)
    for opt,arg in opts:
        if opt == '-h':
            print('python jen_api_python -u <username> -p <password>')
            sys.exit()
        elif opt == '-u':
            username = arg
        elif opt == '-p':
            password = arg

    durationmetrics =  Durationmetrics(username,password)
if __name__ == "__main__":
    main(sys.argv[1:])
