import sqlite3
import pandas as pd
from pandas import DataFrame

conn = sqlite3.connect('fugo_games_case.db')
c = conn.cursor()

read_tv_shows = pd.read_csv(r'***\fugo_games_case\database\tv_shows.csv')
read_tv_shows.to_sql('TV_SHOWS', conn, if_exists='replace', index=False)  # Insert the values from the csv file into the table 'TV_SHOWS'

read_cast = pd.read_csv(r'***\fugo_games_case\database\cast.csv')
read_cast.to_sql('CAST', conn, if_exists='replace', index=False)  # Insert the values from the csv file into the table 'CAST'

read_crew = pd.read_csv(r'***\fugo_games_case\database\crew.csv')
read_crew.to_sql('CREW', conn, if_exists='replace', index=False)  # Insert the values from the csv file into the table 'CREW'

read_crew = pd.read_csv(r'***\fugo_games_case\database\directors.csv')
read_crew.to_sql('DIRECTORS', conn, if_exists='replace', index=False)  # Insert the values from the csv file into the table 'CREW'


print(c.execute("""
SELECT * FROM CAST ORDER BY POPULARITY DESC"""))

print(c.fetchall())
