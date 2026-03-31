# Bioinfo-Pipeline-31031927

## Project Description
This repository contains a lightweight bioinformatics pipeline designed to automate Quality control
of raw sequencing data (FASTQ) files for downstream analysis of alignment to a reference genome
and performs indexing to generate BAM and BAI files for downstream analysis.

## Dependencies
To run this pipeline, you need the following software installed:
* **Python 3.8+** (for file validation scripts)
* **Fastqc** (v0.12.1)
* **Git**
* **R v4.0+** (optional)
* **BWA** (Burrows-Wheeler Aligner)
* **Samtools** (v1.13 or later)
* **Bash/Zsh** (Unix-based terminal from either MobaXterm or Ubuntu)

## Installation Instructions
1. **Clone the repository:**
open your Unix-bsed terminal or Git and clone the repo to your local terminal and cd to it.
   git clone [https://github.com/Donald-Abbott-76/Bioinfo-pipeline.git](https://github.com/Donald-Abbott-76/Bioinfo-pipeline.git)
   cd Bioinfo-pipeline

2. **Installing python**
https://www.python.org/downloads/

3. **Installing tools**
mamba install bwa
mamba install samtools

## Project Organization
The bioinformatics pipeline organization strucure:
data: where the raw reads are stored.
src: where the scripts are writen and stored.
     available scripts are;
	* pipeline.py
	* pipeline.R
	* automated_qc.py
results: where the output are diplayed and stored.
