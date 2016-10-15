import sys, select, string
import socket
import codecs
import pickle
import datetime
import calendar, re
#import StringIO
def prompt() :
    sys.stdout.write('<You> ')
    sys.stdout.flush()

i = 0
big = 60000
small = 0
num = 0
#num = [0 for x in range(80000)]
#first = 1000
# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 9999)
print >>sys.stderr, 'connecting to %s port %s' % server_address
s.connect(server_address)
#prompt()
while 1:
        socket_list = [sys.stdin, s]

        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])

        for sock in read_sockets:
            #incoming message from remote server
            if sock == s:
                data = sock.recv(4096)
                sys.stdout.write(data)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                if "Who are you" in data:
                    msg = "yiyi\n"
                    s.send(msg)
                if "Tell me your secret to start" in data:
                    msg = "54916e2dc3e1b030034cc3324f14bd4e\n"
                    s.send(msg)
                if "thinking a number" in data:
                    num = 20000
                    st = str(num)
                    msg = st+"\n"
                    s.send(msg)


                if "bigger" in data:
                    small = num
                    num = (small + big)/2
                    st = str(num)
                    msg = st+"\n"
                    s.send(msg)

                if "smaller" in data:
                    big = num
                    num = (small + big)/2
                    st = str(num)
                    msg = st+"\n"
                    s.send(msg)
                if "Look at the next 8" in data:
                   # print "yes"
                #    time = datetime.datetime.now()
                 #   with codecs.open('save.p', 'w', encoding='utf-8') as f:
                    f = open("save.p","w")
                    f.write(data)
                    with open("save.p","r") as f:
                        with open("save1.p","w") as g:
                            for line in f.readlines():
                                if "Look at" not in line:
                                    if "That was" not in line:
                                        if "Can you" not in line:
                                            if "ckle it" not in line:
                                                g.write(line)
                    date = pickle.load(open("save1.p","rb"))
                    date = str(date)
                   # f = open("save.p","w")
                   # f.write(date)
                    match = date.split(".")
                    date = match[1]
                    print  date
                    msg = date+"\n"
                    s.send(msg)
                if "My secret" in data:
                #    print data
                    f = open("save.p","w")
                    f.write(data)
                    with open("save.p","r") as f:
                        with open("save1.p","w") as g:
                            for line in f.readlines():
                                if "Well Done" not in line:
                                    if "My secret is" not in line:
                                        g.write(line)
                    sec = open("save1.p").read()
                    print sec
                    s.send(sec)
                if "Which day" in data:
                    if "Jan" in data:
                        mm = 01
                    if "Feb" in data:
                        mm = 02
                    if "Mar" in data:
                        mm = 03
                    if "Apr" in data:
                        mm = 04
                    if "May" in data:
                        mm = 05
                    if "Jun" in data:
                        mm = 06
                    if "Jul" in data:
                        mm = 07
                    if "Aug" in data:
                        mm = 8
                    if "Sep" in data:
                        mm = 9
                    if "Oct" in data:
                        mm = 10
                    if "Nov" in data:
                        mm = 11
                    if "Dec" in data:
                        mm = 12
                    t = re.findall(r'(\w*[0-9]+)\w*',data)
                  #  print t[0], t[1]
                    yy = int(t[1])
                    dd = int(t[0])
                    get = datetime.datetime(yy,mm,dd).weekday()
                    week = int(get)
                    print week
                    if week == 6:
                      msg = "Sunday\n"
                      s.send(msg)
                    if week == 0:
                      msg = "Monday\n"
                      s.send(msg)
                    if week == 1:
                      msg = "Tuesday\n"
                      s.send(msg)
                                                              145,1         75%
                    if week == 2:
                      msg = "Wednesday\n"
                      s.send(msg)
                    if week == 3:
                      msg = "Thursday\n"
                      s.send(msg)
                    if week == 4:
                      msg = "Friday\n"
                      s.send(msg)
                    if week == 5:
                      msg = "Saturday\n"
                      s.send(msg)
            #user entered a message
            else :
#               prompt()
                msg = sys.stdin.readline()
                s.send(msg)
