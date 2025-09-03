import sqlite3

# Connect (this will create the DB file if it doesn’t exist)
conn = sqlite3.connect("cricbuzz.db")
cur = conn.cursor()

# Step 1: Create the table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    country TEXT,
    role TEXT
);
""")


players = cur.execute("SELECT player_id, full_name, country, role FROM players").fetchall()
for p in players:
    print(p)
