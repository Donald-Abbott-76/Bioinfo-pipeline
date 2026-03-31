# fastqc script that handles both zipped and unzipped fastq files.
# automatically process all of them and give the output to the results/ directory.

for file in *.fastq *.fastq.gz
do
    [ -e "$file" ] || continue
    fastqc "$file" -o results/
done
