# CodingPractice

### DateToEpochTimestamp

Convert the human readable date to epoch timestamp/time as on the start of the day.

Example.
If the INPUT date is 21-01-2020, print the epoch time at the start of the day i.e 12:00 AM.
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
