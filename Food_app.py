from flask import Flask, request, render_template, jsonify
import os
from werkzeug.utils import secure_filename
import sqlite3
from datetime import datetime

# Import your custom ML pipeline!
from ml_pipeline import predict_image

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('food_history.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS predictions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  filename TEXT,
                  prediction TEXT,
                  timestamp TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload():
    try:
        # 1. Check if file is provided
        if 'file' not in request.files:
            return jsonify({"success": False, "message": "No file selected!"})
        
        f = request.files['file']
        if f.filename == '':
            return jsonify({"success": False, "message": "No file selected!"})
            
        # 2. Save the file temporarily
        file_path = secure_filename(f.filename)
        if not os.path.exists('uploads'):
            os.makedirs('uploads')
        
        full_path = os.path.join('uploads', file_path)
        f.save(full_path)
        
        # 3. Predict the image
        result = predict_image(full_path)
        
        # 4. Save to Database
        conn = sqlite3.connect('food_history.db')
        c = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO predictions (filename, prediction, timestamp) VALUES (?, ?, ?)",
                  (file_path, result, timestamp))
        conn.commit()
        conn.close()
        
        # 5. Clean up the image
        os.remove(full_path) 
        
        # 6. Return standard JSON
        return jsonify({
            "success": True,
            "prediction": result,
            "message": "Saved to database!"
        })
        
    except Exception as e:
        # If ANYTHING goes wrong, tell the frontend via JSON
        print(f"Backend Error: {e}")
        return jsonify({"success": False, "message": "Internal Server Error"})

@app.route('/history')
def history():
    conn = sqlite3.connect('food_history.db')
    c = conn.cursor()
    c.execute("SELECT * FROM predictions ORDER BY timestamp DESC")
    records = c.fetchall()
    conn.close()
    return render_template('history.html', history=records)

if __name__ == '__main__':
    # host='0.0.0.0' exposes the app outside the Docker container!
    app.run(host='0.0.0.0', port=5000)