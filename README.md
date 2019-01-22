# LogAnalysisProject
Udacity  FullStack Nanodegree Project
## About Project 
In this project, we'll analyze data from a web service's logs, practicing
command-line and database  skills, particularly with a focus on building advanced 
SQL queries.

## Techologies Used 
1.PostgreSQL
2.Python
3.Vagrant
4.Virtual Box


## Installation Process: ##
1. Install Vagrant and VirtualBox
2. Download the database setup: [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
3. Unzip the data to get the newsdata.sql file.

**Process After Installation:**
Open terminal and the commands to install any virtual software:
```vagrant box add ubuntu/trusty64
   vagrant init 
   ```

Open terminal and the following commands to connect to virtual box:
```vagrant up
   vagrant ssh 
   ```

After connection established install the softwares need to execute the the project as follows:
```
	sudo apt-get install pyhton3
	sudo apt-get install python-pip
	sudo apt-get install postgresql
	sudo apt-get install python-psycopg2
```
	
After installation of softwares we need to create roles in database as follows:
```	CREATE ROLE vagrant
	ALTER USER vagrant with superuser
	ALTER USER vagrant with createrole
	ALTER USER vagrant with createDB
	ALTER USER vagrant with Replication
	CREATE DATABASE vagrant
	CREATE DATABASE news
	ALTER DATABASE vagrant OWNER TO vagrant
	ALTER DATABASE news OWNER TO vagrant
```

After creation, we need to load database as 
``` psql -d news -f newsdata.psql ```

# Questions & Answers #
1.What are the most popular three articles of all time?
In this question, we need to create a view , query to find the top three articles 
from the database of all the time.

2.Who are the most popular article authors of all time? 
In this question, we need to create a view , query to find the most popular article author 
from the database of all the time.

3.On which days did more than 1% of requests lead to errors? 
In this question, we need to create a view , query to find the error that is more than 
one percent in one day from the database of all the time.


In python file we need to write views and queries for the given questions.The views are as follows:
```
 	1st query view:
	"""create view view_article as SELECT articles.title,count(*)
        from articles inner join log on log.path like concat
        ('/article/%', articles.slug) group by articles.title
        order by count(*) desc limit 3;"""

	2nd query view:
	"""create view view_author as select authors.name,count(*),
            articles.author from articles inner join log on log.path like
            concat ( '/article/%', articles.slug) inner join authors on
            authors.id = articles.author group by authors.name,
            articles.author order by count(*) desc;"""

	3rd query view:
	"""create view view_error as  select date(time),
            round(100.0*sum(case log.status when '404 NOT FOUND' then 1 else 0
            end)/count(log.status) , 4) as error from log group by
            date(time) """
```


# Output:

 opened database

1) What are the most popular three articles of all time?

        Candidate is jerk, alleges rival-338647views

        Bears love berries, alleges bear-253801views

        Bad things gone, say good people-170098views


 2) Who are the most popular article authors of all time?

        Ursula La Multa-507594

        Rudolf von Treppenwitz-423457

        Anonymous Contributor-170098

        Markoff Chaney-84557


 3) On which days did more than 1% of requests lead to errors?

         2016-07-17 - 2.2627 %

* To complete this project I have taken support of my Mentor and some Github references



