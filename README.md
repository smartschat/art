# Approximate Randomization Testing


This repository contains a package that allows to perform two-sided paired approximate randomization tests to assess the statistical significance of the difference in performance between two systems.

## Usage

You need to create an ApproximateRandomizationTest object to perform the test. Here is an example:

```
import approximate_randomization_test as art
import aggregators

test = art.ApproximateRandomizationTest(open('system1_file'), open('system2_file'), aggregators.f1)
test.run()
```

## Input Format

We assume that we want to check the statistical significance of the difference in score between two systems S and T on the same corpus C. To compute the score over the whole corpus, we compute for each document all scores needed to compute the final score, and then aggregate the above values over the whole corpus to compute an aggregated score. 

Hence, we assume that the input files contain in the i-th line

```
score_1 score_2 ... score_n
```

for the i-th document in the corpus. That is, a list of numbers divided by space.

## Examples

So far, three aggregation functions are implemented: average, dividing sums (suitable for precision and recall) and F1 score. All these are implemented in `aggregators.py`. We now briefly describe each such function and the expected input format for the `ApproximateRandomizationTest` object.

### Average

Aggregation function `average`. Expected input is a file containing one number per line. The function just computes the average of all the numbers.

### Dividing sums

Aggregations function `enum_sum_div_by_denom_sum`. Expected input is a file containing two numbers per line. The first number is interpreted as the enumerator, the second number as the demoninator. The aggregated score is computed by summing over each and then dividing. One use-case of this aggregation function is to compute recall or precision.

### F1

Aggregations function `f1`. Expected input is a file containing four numbers per line. The first two numbers are interpreted as enumerator and denominator for recall, the third and fourth number accordingly for precision. The aggregated score is aggregating recall and precision individually, by dividing sums, and then computing the F1 score.

## Converting CoNLL Coreference Score Files

This repository also contains a script to create the required input from the output of the CoNLL coreference scorer (http://code.google.com/p/reference-coreference-scorers/).

Usage is

```
$ python from_conll_score_file.py conll_score_file
```

Here conll_score_file should have been created by using the official CoNLL scorer, e.g.

```
$ perl scorer.pl muc key response > conll_score_file
```

The script prints the extracted values for recall and precision to standard output (sutiable for testing of differences in F1 score)
