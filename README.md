# Software-Developer-Analysis
This is the course project of Intro to Data Science


First URL extraction:
total data: 2700
Date: 2/3/2018		11:20 pm

Next step:
1. record word frequency
(database for noisy words, database for technical skills, key words for regular expression)

	i. design LSE (what method: noise word hashmap, key word hashmap (OrderedDict), print function )

2. generate regular expression rule:
words like "web" need to be detect and record the following word
(collect such words)
3. separate most frequent words into technical words and non-technical words
4. find the relationship between companies and skill requirement
5. try text generator 

Problem:
1. Not every description includes the same number of people required
2. collision bwtween linkedin and glassdoor
3. keyword duplication (don't count frequency)
4. Keyword misunderstanding (Master degree or adj master)
5. set weight to each key word to distinguish a key word stress in a single company with a key word stree in serveral company 
