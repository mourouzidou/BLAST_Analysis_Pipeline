import requests
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--organism', type=str, required=True)
args = parser.parse_args()


# Get all the reference proteomes from Uniprot matched to organism IDs/scientific name/common name

ID_url = 'https://rest.uniprot.org/proteomes/stream?fields=upid%2Corganism%2Corganism_id%2Cprotein_count&format=tsv&query=%28%2A%29%20AND%20%28proteome_type%3A1%29&sort=protein_count%20asc'

with requests.get(ID_url, stream=True) as prtmRequest:
        prtmRequest.raise_for_status()
        with open('ReferenceProteomes', 'wb') as f:
            for chunk in prtmRequest.iter_content(chunk_size=2**20):
                f.write(chunk)


# Entries filtering

with open('ReferenceProteomes', encoding = 'utf-8') as f:
    text = f.readlines()
    d = {}

    for entry in text:
        commonName = re.sub("[()]", "\t", entry)
        edited = commonName.strip().split("\t")
        finalModName = [i.strip() for i in edited if i.strip()]

# remove entries with 0 proteins and duplicates

        if finalModName[-1] != '0':
            d[finalModName[0]] = finalModName[1:-1]


# Match the organism input to the UP proteome ID

for k, v in d.items():
    for i in v:
        if args.organism == i:
            prid = k




outputfilename = args.organism + '_proteome.fa'    

url='https://rest.uniprot.org/uniprotkb/stream?format=fasta&query=%28proteome%3A'+prid+'%29'

with requests.get(url, stream=True) as request:
    request.raise_for_status()
    with open(outputfilename, 'wb') as f:
        for chunk in request.iter_content(chunk_size=2**20):
            f.write(chunk)

    
