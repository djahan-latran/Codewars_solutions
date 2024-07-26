"""The mean and standard deviation of a sample of data can be thrown off if the sample contains one or many outlier(s).
For this reason, it is usually a good idea to check for
and remove outliers before computing the mean or the standard deviation of a sample.
To this aim, your function will receive a list of numbers representing a sample of data.
Your function must remove any outliers and return the mean of the sample,
rounded to two decimal places (round only at the end).

Since there is no objective definition of "outlier" in statistics, your function will also receive a cutoff,
in standard deviation units. So for example if the cutoff is 3,
then any value that is more than 3 standard deviations above or below the mean must be removed.
Notice that, once outlying values are removed in a first "sweep", other less extreme values may then "become" outliers,
that you'll have to remove as well!

Example :

sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
cutoff = 3
clean_mean(sample, cutoff) → 5.5"""


# My solution

from math import sqrt

def clean_mean(sample, cutoff):
    # calc the mean of the sample
    x_sum = sum(i for i in sample)
    x_amount = len(sample)

    x_mean = round(x_sum / x_amount, 2)

    # calc the standard deviation of the sample
    std_numerator = sum((i - x_mean) ** 2 for i in sample)
    std_denominator = len(sample)

    std_sample = sqrt(std_numerator / std_denominator)

    # calc the cutoff range
    cutoff_range = cutoff * std_sample

    # set boundaries for filtering outliers by cutoff range
    boundary_left = x_mean - cutoff_range
    boundary_right = x_mean + cutoff_range

    # calc the filtered sample
    filtered_sample = [i for i in sample if boundary_left < i < boundary_right]

    # base case (check if length is the same because then there was no filtering going on
    # which means there are no more outliers)
    if len(filtered_sample) == len(sample):
        return x_mean

    # calc the mean of new filtered sample
    filtered_sample_sum = sum(i for i in filtered_sample)
    filtered_sample_length = len(filtered_sample)
    filtered_sample_mean = round(filtered_sample_sum / filtered_sample_length, 2)

    # call the function recursively with the filtered sample to check if new outliers are present
    return clean_mean(filtered_sample, cutoff)