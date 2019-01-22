#!/usr/bin/env python3
import psycopg2


# establishing database connection
def databaseconnection():
    try:
        connection = psycopg2.connect("dbname=news")
        cursor = connection.cursor()
        print("\n opened database \n")
        return cursor, connection
    except Exception:
            print("Unable to connect to the database")


# creating first query
def query1(cursor):
    # first question view
    q = """create view view_article as SELECT articles.title,count(*)
        from articles inner join log on log.path like concat
        ('/article/%', articles.slug) group by articles.title
        """
    # cursor[0].execute(q)
    # first query execution
    q1 = ("select * from view_article order by count desc limit 3;")
    cursor[0].execute(q1)
    cursor[1].commit()
    r = cursor[0].fetchall()
    print("1) What are the most popular three articles of all time?\n")
    for result in r:
        print("\t" + str(result[0]) + " - " + str(result[1]) + " views." +
              "\n")
    return


# creating second query
def query2(cursor):
    # second question view
    q2 = """create view view_author as select authors.name,count(*),
            articles.author from articles inner join log on log.path like
            concat ( '/article/%', articles.slug) inner join authors on
            authors.id = articles.author group by authors.name,
            articles.author order by count(*) desc"""
    # cursor[0].execute(q2)
    # second query execution
    qm = ("select * from view_author;")
    cursor[0].execute(qm)
    cursor[1].commit()
    r = cursor[0].fetchall()
    print("\n 2) Who are the most popular article authors of all time?\n")
    for result in r:
        print("\t" + str(result[0]) + " - " + str(result[1]) +
              " articles." + "\n")
    return


# third query
def query3(cursor):
    # third question view
    q3 = """create view view_error as  select date(time),
            round(100.0*sum(case log.status when '404 NOT FOUND' then 1 else 0
            end)/count(log.status) , 4) as error from log group by
            date(time) """
    # cursor[0].execute(q3)
    # third query execution
    qe = ("select date,error from view_error where error > 1.0")
    cursor[0].execute(qe)
    cursor[1].commit()
    r = cursor[0].fetchall()
    print("\n 3) On which days did more than 1% of requests lead to errors?\n")
    for result in r:
        print(" \t " + str(result[0]) + " - " + str(result[1]) + " % " +
              " \n ")
    return


if __name__ == "__main__":
    c = databaseconnection()
    if c:
        query1(c)
        query2(c)
        query3(c)
        c[1].close()
