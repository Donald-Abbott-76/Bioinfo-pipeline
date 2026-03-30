
#FASTQC script

print("beginning sequence analysis.........")

sample_ID = 0
for i in range(10):
    print(f"Analyzing sequence: {i}")
    sample_ID += 1
print("compiling sequences")

print("Analysis complete")

print("samples found:", sample_ID)

print("fastqc.html" "\n" "fastqc.zipped")







#Variant calling

print("Started analysis for variant calling.....")

variants_found = 0

for i in range(10):
    print(f"Analyzing variant sequence {i}")
    variants_found += 1

print("compiling variant sequences")

print("Variant Analysis completed")

print("samples found:", variants_found)

print("variant_name.txt" "\n" "variant.zipped")
