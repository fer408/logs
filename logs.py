# Python 2.7
import psycopg2
# program to communicate with the news database

DB = "news"  # Variable DB is given the value of the database news
# The variable db connects to the database which is the variable
# DB which of course
db = psycopg2.connect(database=DB)
# has the value of the news database.
c = db.cursor()  # I give my database a cursor

# This variable has within it the SQL queries I used to find the
# answer for the second question within the database.
article = "\
SELECT path,count(*) AS views \
FROM log \
GROUP BY path \
ORDER BY views DESC \
LIMIT 3 OFFSET 1;\
"
# This variable has within it the SQL queries I used to find the
# answer for the first question within the database.
author = "\
SELECT authors.name,count(*) AS num \
FROM authors, articles \
WHERE articles.author = authors.id \
GROUP BY authors.name \
ORDER BY count(*) DESC \
LIMIT 3;\
"

# This variable has within it the SQL queries I used to find the
# answer for the third question within the database.
errors = "\
SELECT * \
FROM (SELECT time::DATE, count(*)\
FILTER ( WHERE status = '404 NOT FOUND')/(count(*) * 1.0 ) \
* 100.0 AS error FROM log GROUP BY time::DATE) \
AS fail  \
WHERE error > 1;\
"

# This function executes the first question which looks for the
# most viewed article in the database


def articles():
        # print "The top three articles are:"
    print "1. What are the most popular three articles of all time? "
    c.execute(article)
    rows = c.fetchall()
    for row in rows:
        print row[0]
        print row[1]
        print "\n"


def authors():
        # print " The 3 most popular authors are:"
    print "2. Who are the most popular article authors of all time?"
    c.execute(author)  # This line executes the first question
    rows = c.fetchall()
    for row in rows:
        print row[0]
        print row[1]
        print "\n"


def error():
    # print "On which days did more than 1 percent of requests lead to errors?"
    print "3. On which days did more than 1% of requests lead to errors?"
    c.execute(errors)  # This line executes the third question
    rows = c.fetchall()
    for row in rows:
        print row[0]
        print row[1]
        print "\n"


articles()
authors()
error()

db.close()  # This line coses the database for good coding practice
