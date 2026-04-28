from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

DB_NAME = "mood_tracker.db"

# ---------- Ensure DB and Table ----------


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS moods (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mood TEXT NOT NULL,
        note TEXT,
        emoji TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()


# Call init_db() when app starts
init_db()

# ---------- Routes ----------


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mood = request.form["mood"]
        note = request.form.get("note", "")
        emoji = request.form.get("emoji", "")

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO moods (mood, note, emoji) VALUES (?, ?, ?)", (mood, note, emoji))
        conn.commit()
        conn.close()

        return redirect("/")

    # Fetch all entries
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT mood, note, emoji, timestamp FROM moods ORDER BY timestamp DESC")
    entries = cursor.fetchall()
    conn.close()

    return render_template("index.html", entries=entries)


if __name__ == "__main__":
    app.run(debug=True)
