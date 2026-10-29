import sqlite3

conn = sqlite3.connect('backend/interviewai.db')
c = conn.cursor()

print("--- QUESTIONS BY TOPIC ---")
c.execute("""
    SELECT t.name, s.name, COUNT(q.id) 
    FROM topics t 
    JOIN subjects s ON t.subject_id = s.id 
    LEFT JOIN questions q ON q.topic_id = t.id 
    GROUP BY t.id 
    ORDER BY COUNT(q.id) ASC
""")
rows = c.fetchall()
for t_name, s_name, count in rows:
    print(f"[{s_name}] {t_name}: {count} questions")

print("\n--- CODING PROBLEMS BY DIFFICULTY ---")
c.execute("SELECT difficulty, COUNT(*) FROM coding_problems GROUP BY difficulty")
for diff, count in c.fetchall():
    print(f"{diff}: {count} problems")

conn.close()

