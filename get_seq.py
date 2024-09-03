import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('--genesfile', type = str, required = True)
parser.add_argument('--dbfile',    type = str, required = True)
args = parser.parse_args()

# Create a complex motif with all gene names

motif = r''
with open(args.genesfile, 'r') as g:
    for ln in g:
        motif = motif + re.escape(ln.strip()) + "|"
    motif = motif[:-1]

pattern = re.compile(motif)
pattern2 = re.compile(r">")

readflag = 0

with open(args.dbfile, 'r') as db:
    while True:
        if not readflag:
            ln = db.readline().strip()
        readflag = 0
        if pattern.search(ln):
            newnamev = ln.split()
            newname = newnamev[0]+"_"+newnamev[1]
            print(newname)
            ln = db.readline().strip()
            while not pattern2.search(ln):
                print(ln)
                ln = db.readline().strip()
                readflag = 1
        if not ln:
            break
