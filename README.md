# 🏏 Cricbuzz LiveStats

A **Streamlit-based Cricket Analytics Dashboard** that integrates with the **Cricbuzz API** and a local database to provide live match updates, top player stats, and database CRUD operations.  

---

## 🚀 Features

### 📌 Pages
1. **Home Page**
   - Project description, tools used, navigation guide.
   - Shows folder structure and documentation links.

2. **Live Matches Page**
   - Displays ongoing matches using Cricbuzz API.
   - Live scorecards with batsmen, bowlers, match status, and venue details.

3. **Top Player Stats Page**
   - Shows batting and bowling leaders (most runs, highest scores, most wickets, etc.).
   - Data visualized with charts and tables.

4. **CRUD Operations Page**
   - Perform **Create, Read, Update, Delete** on player and match data.
   - Uses forms to interact with the database (SQLite/MySQL/PostgreSQL).

5. **SQL Queries Page**
   - Predefined optimized queries for learning (joins, aggregations, indexing tips).
   - Interactive examples for filtering and performance tuning.

---

## 🛠️ Tech Stack

- **Frontend/UI** → [Streamlit](https://streamlit.io/)
- **Backend/API** → Cricbuzz API (via RapidAPI / open endpoints)
- **Database** → SQLite (default), MySQL, or PostgreSQL
- **Python Libraries**:
  - `requests`
  - `sqlite3` / `mysql-connector-python` / `psycopg2`
  - `pandas`
  - `streamlit`

---

## 📂 Project Structure

```bash
cricbuzz_livestats/
│── requirements.txt          # Python dependencies
│── README.md                 # Project documentation
│── cricbuzz.db               # SQLite database (sample)
│
├── pages/
│   ├── Home.py               # Home page
│   ├── live_matches.py       # Live Matches page
│   ├── top_stats.py          # Top Player Stats page
│   ├── crud_operations.py    # CRUD Operations page
│   ├── sql_queries.py        # SQL Queries page
│
├── utils/
│   ├── db_connection.py      # Database connection handler
