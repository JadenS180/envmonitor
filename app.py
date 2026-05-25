from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

def get_readings(limit=50):
    conn = sqlite3.connect('envmonitor.db')
    c = conn.cursor()
    c.execute('SELECT timestamp, temperature, humidity, air_quality FROM readings ORDER BY timestamp DESC LIMIT ?', (limit,))
    rows = c.fetchall()
    conn.close()
    return [{'timestamp': r[0], 'temperature': r[1], 'humidity': r[2], 'air_quality': r[3]} for r in rows]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/readings')
def api_readings():
    readings = get_readings()
    return jsonify(readings)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
