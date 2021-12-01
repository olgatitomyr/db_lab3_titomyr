import psycopg2
import matplotlib.pyplot as plt


username = 'titomyr_labs'
password = '13579'
database = 'lab2'
host = 'localhost'
port = '5432'

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

query_1 = '''
create view CountriesSportsmen as
select country, count(country) as number_of_sportsmen from sportsman group by country
'''

query_2 = '''
create view MedalsSportsmen as
select medal, count(medal) from sportsman_games
join sportsman on sportsman_games.sportsman_id = sportsman.sportsman_id group by medal
'''

query_3 = '''
create view GamesSportsmen as
select games_name, count(distinct(sportsman.sportsman_id)) from sportsman
join sportsman_games on sportsman.sportsman_id = sportsman_games.sportsman_id group by games_name
'''

with con:

    cur2 = con.cursor()
    cur2.execute('DROP VIEW IF EXISTS CountriesSportsmen')
    cur2.execute(query_1)
    cur2.execute('SELECT * FROM CountriesSportsmen')
    countries = []
    sportsmen1 = []

    for row in cur2:
        countries.append(row[0])
        sportsmen1.append(row[1])

    cur2 = con.cursor()
    cur2.execute('DROP VIEW IF EXISTS MedalsSportsmen')
    cur2.execute(query_2)
    cur2.execute('SELECT * FROM MedalsSportsmen')
    medals = []
    sportsmen2 = []

    for row in cur2:
        medals.append(row[0])
        sportsmen2.append(row[1])

    cur3 = con.cursor()
    cur3.execute('DROP VIEW IF EXISTS GamesSportsmen')
    cur3.execute(query_3)
    cur3.execute('SELECT * FROM GamesSportsmen')
    games = []
    sportsmen3 = []

    for row in cur3:
        games.append(row[0])
        sportsmen3.append(row[1])


plt.bar(countries, sportsmen1, width=0.5)
plt.xlabel('Countries')
plt.ylabel('Number of sportsmen')
plt.show()

fig, ax = plt.subplots()
ax.pie(sportsmen2, labels=medals, normalize=True)
plt.axis('equal')
plt.show()

plt.scatter(games, sportsmen3)
plt.show()

