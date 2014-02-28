Approximate Randomization Testing for F1
======


This repository contains a simple script that performs an approximate randomization test to assess the statistical significance of the difference in F1 score between two systems.

Usage
-----

$ python3 approximate\_randomization.py system1\_file system2\_file

The script then prints the p-value to standard output.

Input Format
------------

We assume that we want to check the statistical significance of the difference in F1 score between two systems S and T on the same corpus C. To compute the F1 score over the whole corpus, we compute for each document:

numerator\_recall, denominator\_recall, numerator\_precision, denominator\_precision

We then aggregate the above values over the whole corpus to compute recall and precision. From this we can compute the F1 score.

Hence, we assume that the input files contain in the i-th line contains

numerator\_recall, denominator\_recall, numerator\_precision, denominator\_precision

for the i-th document in the corpus.

Converting CoNLL Coreference score files
----------------------------------------

This repository also contains a script to create the required input from the output of the CoNLL coreference scorer (http://code.google.com/p/reference-coreference-scorers/).

Usage is

$ python3 from_conll_score_file.py conll_score_file

Here conll_score_file should have been created by using the official CoNLL scorer, e.g.

$ perl scorer.pl muc key response > conll_score_file

The script prints the extracted values for recall and precision to standard output.
