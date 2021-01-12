# CodingPractice

### printFilteredData

We wish to train a machine learning algorithm on an array of floating-point numbers in the interval [0.0,
1.0). The data is not evenly distributed, and we wish to filter the dataset to obtain a subset containing an
equal number of values from each interval [0, 0.2), [0.2, 0.4), ... [0.8, 1.0), throwing away as little data as
possible.<br />
Write a program which reads comma-separated floating-point numbers in a single line from stdin and prints
the filtered data to stdout in the same format
Note: Solve this in linear time.<br />

Example 1<br />
Input: 0.1,0.3,0.5,0.7,0.9<br />
Output: 0.1,0.3,0.5,0.7,0.9<br />
Example 2<br />
Input: 0.1,0.3,0.5,0.7,0.9,0.5<br />
Output: 0.1,0.3,0.5,0.7,0.9<br />
Question 2 – Floating PointNumbers – Print Filtered Data<br />
<br />
Example 3<br />
Input: 0.15,0.12,0.35,0.38,0.55,0.56,0.57,0.75,0.77,0.9,0.94<br />
Output: 0.15,0.12,0.35,0.38,0.55,0.56,0.75,0.77,0.9,0.94<br />
Example 4<br />
Input: 0.11,0.12,0.13,0.23,0.34,0.35,0.47,0.59,0.77,0.83,0.85,0.91,0.95<br />
On classifying the above input data from example 4, Subset in each interval will look as below:<br />
Interval Data<br />
[0 - 0.2) 0.11,0.12,0.13<br />
[0.2 - 0.4) 0.23,0.34,0.35<br />
[0.4 - 0.6) 0.47,0.59<br />
[0.6 - 0.8) 0.77<br />
[0.8 - 1.0) 0.83,0.85,0.91,0.95<br />
Since the interval [0.6 - 0.8) has the minimum subset of size 1. We choose 1 element from the rest of the
intervals.<br />
Output: 0.11,0.23,0.47,0.77,0.83<br />
*if the interval [0.6 - 0.8) had more than 3 elements then we would choose 2 elements from all subset, since
the interval with minimum subset would be [0.4 - 0.6) and of size 2.<br />


### DateToEpochTimestamp

Convert the human readable date to epoch timestamp/time as on the start of the day.

Example:<br />
If the INPUT date is 21-01-2020, print the epoch time at the start of the day i.e 12:00 AM.<br />
<br />
Input Description:<br />
The input date will be in any of the following format.<br />
1) dd/mm/yyyy<br />
2) mm/dd/yyyy<br />
3) dd-mm-yyyy<br />
4) mm-dd-yyyy<br />
5) dd.mm.yyyy<br />
6) mm.dd.yyyy<br />
7) ddmmyyyy<br />
8) mmddyyyy<br />
Output Description:<br />
For all the types of above input date, the output should be an Epoch timestamp/time.<br />
Exceptions:<br />
Any input date other than the given formats must be handled and a message "Unable to convert the provided date" must be printed.<br />

More Examples:<br />
Example 1<br />
Input: 19-01-2020<br />
Output: 1579392000<br />
Example 2<br />
Input: 31122012<br />
Output: 1356912000<br />
Example 3<br />
Input: 251220202<br />
Output: Unable to convert the provided date<br />
Example 4<br />
Input: 17:04:2020<br />
Output: Unable to convert the provided date<br />

### WhoTweetedTheMost
You will be given a list of tweets
Your program should find the user who has tweeted the most

<ins>Input format:</ins>
Read the input from console.
First line of input should be number of test cases
Remaining lines of input should contain each test case input. 

For each test case input:
First line should contain number of tweets.
Followed by N lines, each containing user name and tweet id separated by a space.

<ins>Output format:</ins>
Find the user with max number of tweets. Print user name and total number of tweets.

Note:
If multiple users are having same number of tweets, then print all the users in alphabetical order of user names.

Sample 1:<br />
Input<br />
2<br />
4<br />
sachin tweet_id_1<br />
sehwag tweet_id_2<br />
sachin tweet_id_3<br />
sehwag tweet_id_4<br />
5<br />
dhoni tweet_id_10<br />
dhoni tweet_id_11<br />
kohli tweet_id_12<br />
dhoni tweet_id_13<br />
dhoni tweet_id_14<br />
<br />
Output<br />
sachin 2<br />
sehwag 2<br />
dhoni 4<br />
