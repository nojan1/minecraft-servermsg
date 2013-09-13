#!/usr/bin/python

from subprocess import *
import re, sched, time, random, sys

def say(what):
    try:
        command = "screen -S minecraft-%s -X stuff 'say %s \n'" % (SRVNAME, what)
        #print("Executing:", command)
        check_output(command, shell=True)
    except CalledProcessError:
        print("Failed to send data to screen")

def getTemp():
    output = check_output("sensors -u", shell=True)
    return int(re.findall("temp2_input: (\d*)", str(output))[0])


def getFortune():
    data = check_output("fortune -s", shell=True, universal_newlines=True)
    data = data.replace("'","").strip()
    return data

def doEvent():
    msg = msgs[random.randint(0, len(msgs)-1)]
    
    formatted = None
    if msg[1]:
        try:
            formatted = msg[0] % tuple( [f() for f in msg[1]] )
        except Exception as e:
            print("Failed to build msg;", msg, str(e))
    else:
        formatted = msg[0]

    if formatted:
        for line in formatted.split("\n"):
            print("About to say: %s" % line)
            say(line)

    delay = random.randint(20, 30)
    print("Next message in %i minutes" % delay)

    s.enter((delay * 60), 1, doEvent)
    

if len(sys.argv) < 2:
   print("You have to enter a server name")
   sys.exit(1)

SRVNAME = sys.argv[1]

template_msgs = [("Hi! My name is Angelica", None, 1),
                 ("I am currently %i degrees warm", (getTemp,), 1),
                 ("I live in a card board box", None, 1),
                 ("All my fans are spinning out of control", None, 1),
                 ("%s", (getFortune,), 7)]

msgs = []
for tm in template_msgs:
    for i in range(tm[2]):
        msgs.append(tm)

s = sched.scheduler(time.time, time.sleep)
s.enter(1, 1, doEvent)
s.run()
    
