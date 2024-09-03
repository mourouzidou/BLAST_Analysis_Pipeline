reforg=$1
family_name=$2
annot=$3

python3 get_reforg.py --organism $reforg --family $family_name --annotation_score $annot


for org in `cat orglist.txt`;do
    echo "Downloading organism $org"
    python3 proteomes.py --organism $org
    echo "Done"
done


 
#  Blast search



for i in $( ls *_proteome.fa); do
    query=${family_name}_${reforg}.fa
    organism=$( echo $i | sed 's/_proteome.fa//')
    diamond makedb --in ${i} --db ${organism}
    diamond blastp --query ${query} --db ${organism}.dmnd --outfmt 6 --out ${query}_VS_${organism}.blast --ultra-sensitive --threads 5


cut -f2 ${family_name}_${reforg}.fa_VS_${organism}.blast | sort -u > ${organism}.genes
done

python3 get_seq.py --genesfile ${organism}.genes --dbfile ${i} > ${family_name}_${regorg}.fa

#____________________

cat ${family_name}_*fa > matched_${family_name}.fa

mafft matched_${family_name}.fa > ${family_name}.aln

iqtree -s ${family_name}.aln -m LG+G8+F 




