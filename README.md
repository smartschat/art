Approximate Randomization Testing
======


This repository contains a package that allows to perform approximate randomization tests to assess the statistical significance of the difference in performance between two systems.

Usage
-----

You need to create an ApproximateRandomizationTest object to perform the test. Here is an example:

```
import approximate_randomization_test as art
import aggregators

test = art.ApproximateRandomizationTest(open('system1_file'), open('system2_file'), aggregators.f1)
test.run()
```


Input Format
------------

We assume that we want to check the statistical significance of the difference in score between two systems S and T on the same corpus C. To compute the score over the whole corpus, we compute for each document:

score_1, score_2, ..., score_n

We then aggregate the above values over the whole corpus to compute an aggregated score. This can be for example the average (then n = 1) or the F1 score (then n = 4).

Hence, we assume that the input files contain in the i-th line

score_1, score_2, ..., score_n

for the i-th document in the corpus.

Converting CoNLL Coreference score files
----------------------------------------

This repository also contains a script to create the required input from the output of the CoNLL coreference scorer (http://code.google.com/p/reference-coreference-scorers/).

Usage is

$ python from_conll_score_file.py conll_score_file

Here conll_score_file should have been created by using the official CoNLL scorer, e.g.

$ perl scorer.pl muc key response > conll_score_file

The script prints the extracted values for recall and precision to standard output.
