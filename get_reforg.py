  
import requests
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('--organism', type = str, required=True)
parser.add_argument('--family', type = str, required = True)
parser.add_argument('--annotation_score', type = str, required = True)
args = parser.parse_args()



proteinName = args.family
organism =args.organism
organism_id = ""
annotation_score = args.annotation_score
outputfilename = proteinName+'_'+organism+'.fa'

if organism == "human":
    organism_id = str(9606)


url = 'https://rest.uniprot.org/uniprotkb/stream?&format=fasta&query=%28%28protein_name%3A'+proteinName+'%29%29%20AND%20%28annotation_score%3A'+annotation_score+'%29%20AND%20%28model_organism%3A'+organism_id+'%29'


    
with requests.get(url, stream=True) as request:
    request.raise_for_status()
    with open(outputfilename, 'wb') as f:
              for chunk in request.iter_content(chunk_size=2**20):

                  f.write(chunk)
        

with open(outputfilename, "r") as g:
    text = g.readlines()
with open(outputfilename, "w") as f:
    for line in text:
        rmtail = re.sub("OS=.*", "", line).strip()
        new_header = re.sub("[\s|]", "_", rmtail)
        f.writelines(new_header+"\n")

        
              
