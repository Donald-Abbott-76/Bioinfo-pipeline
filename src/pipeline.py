
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
