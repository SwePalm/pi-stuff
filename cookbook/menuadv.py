#!/ust/bin/python3
#menuadv.py

import os
from subprocess import call

SCRIPT_DIR="." #use current dir
SCRIPT_NAME=os.path.basename(__file__)

print ("Start Menu:")
scripts=[]
item_num=1
for files in os.listdir(SCRIPT_DIR):
    if files.endswith(".py"):
        print ("%s:%s"%(item_num,files))
        scripts.append(files)
        item_num+=1
running = True
while (running):
    print ("Enter script number to run: 1-%d (x to exit)" % (len(scripts)))
    run_item = input()
    try:
        run_number = int(run_item)
        if len(scripts) >= run_number > 0:
            print ("Run script number:" + run_item)
            commands = ["python3", scripts[run_number-1]]
            print (commands)
            call(commands)
            running = False
    except ValueError:
        #otherwise ignore invalid input
        if run_item == "x":
            running = False
            print ("Exit")
#End
