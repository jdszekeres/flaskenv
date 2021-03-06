#! /usr/bin/env python3
import os
import sys
import urllib.request
if "-h" in sys.argv:
    print("flaskenv.py [options]")
    print("""-h show this message and exit
    --dir specify a directory besides the curent directory
    --extra-dir specify an extra directory to make besides templates and static""")
    
if "--dir" in sys.argv:
    directory = sys.argv[sys.argv.index("--dir")+1]
else:
    directory = "."
try:
    os.chdir(directory)
except Exception as e:
    print(e)
    os.mkdir(directory)
    os.chdir(directory)
with open("app.py", "w+") as f:
    f.write("""from flask import *
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello World'
app.run(debug=True, port=80, host="0.0.0.0")""")
    f.close()
os.mkdir("static")
os.mkdir("templates")
os.chdir("static")
urllib.request.urlretrieve("http://transparent-favicon.info/favicon.ico", "favicon.ico")
os.chdir("../templates")
open("index.html", "w+").close()
os.chdir("..")
if "--extra-dir" in sys.argv:
    os.mkdir(sys.argv[sys.argv.index("--extra-dir")+1])
