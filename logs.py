import psycopg2 #Imports the library which allows this python program to communicate with the news database


DB = "news" #Variable DB is given the value of the database news
db = psycopg2.connect(database=DB)#The variable db connects to the database which is the variable DB which of course
#has the value of the news database.
c = db.cursor()# I give my database a cursor

#This variable has within it the SQL queries I used to find the answer for the first question within the database.
article = "\
SELECT path,count(*) AS views \
FROM log \
GROUP BY path \
ORDER BY views DESC \
LIMIT 3 OFFSET 1;\
"
#This variable has within it the SQL queries I used to find the answer for the second question within the database.
author = "\
SELECT authors.name,count(*) AS num \
FROM authors, articles \
WHERE articles.author = authors.id \
GROUP BY authors.name \
ORDER BY count(*) DESC \
LIMIT 3;\
"

#This variable has within it the SQL queries I used to find the answer for the third question within the database.
errors = "\
SELECT * \
FROM (SELECT time::DATE, count(*) FILTER ( WHERE status = '404 NOT FOUND')/(count(*) * 1.0 ) \
* 100.0 AS error FROM log GROUP BY time::DATE) \
AS fail  \
WHERE error > 1;\
"

#This function executes the first question which looks for the most viewed article in the database
def articles():
	c.execute(article)#This line executes the first question
	print c.fetchall()#This returns the data that my querie receives

def authors():
	c.execute(author)#This line executes the second question
	print c.fetchall()#This returns the data that my querie receives
	
def error():
	c.execute(errors)#This line executes the third question
	print c.fetchall()#This returns the data that my querie receives
	

articles()
authors()
error()

db.close()#This line coses the database for good coding practice

#Special thanks to my mentor Trey for the help 