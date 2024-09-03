## Overview

This project provides a set of tools for retrieving and processing protein sequence data from the UniProt database, along with capabilities for performing BLAST (Basic Local Alignment Search Tool) analysis. The pipeline is designed to handle various tasks, such as downloading reference proteomes, extracting specific gene sequences, and fetching sequences for particular organisms and protein families.

## Features

- **Download Reference Proteomes**: Retrieve complete reference proteomes for specified organisms.
- **Extract Gene Sequences**: Extract sequences corresponding to a list of gene names from a database.
- **Fetch Organism-Specific Sequences**: Download sequences for specific organisms and protein families with given annotation scores.
- **BLAST Analysis**: The scripts are designed to integrate with BLAST for sequence alignment and comparison, allowing for downstream analysis of retrieved sequences.

## Requirements

- Python 3.x
- `requests` library: Install via `pip install requests`
- BLAST+ command line tools (optional, for performing BLAST analysis)

## Usage

### 1. Download Reference Proteomes

Use the `proteomes.py` script to download reference proteomes for an organism.
This will download the proteome sequences in FASTA format for the specified organism.

```bash
python proteomes.py --organism "human"

```
### 2. Extract Specific Gene Sequences

Use the get_seq.py script to extract sequences for specific genes from a database.
This will print the extracted sequences to the console.

```bash
python get_seq.py --genesfile genes.txt --dbfile database.fa
```

### 3. Fetch Organism-Specific Sequences

Use the get_reforg.py script to fetch sequences for a particular organism and protein family.
This will download the sequences in FASTA format for the specified organism and protein family.

``` bash

python get_reforg.py --organism "human" --family "kinase" --annotation_score "5"
```

### 4. BLAST Analysis

Once you have retrieved the sequences, you can perform a BLAST analysis using BLAST+ command line tools. Here's an example command to perform a BLAST search:
This will compare the protein sequences against the nr database and output the results in a tabular format.

```bash

blastp -query your_sequences.fa -db nr -out results.out -evalue 1e-5 -outfmt 6
```

### 5. Automation

Run the general_script2.sh included in the project to automate the entire pipeline:

``` bash

bash general_script2.sh

```



