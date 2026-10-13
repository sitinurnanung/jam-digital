from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('jam.html')

@app.route('/api/waktu')
def waktu():
    now = datetime.now()
    
    # Format 12 jam
    h = now.hour % 12 or 12
    ampm = "PM" if now.hour >= 12 else "AM"
    
    # Nama hari & bulan dalam Bahasa Indonesia
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
             "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    
    data = {
        "jam": f"{h:02d}",
        "menit": f"{now.minute:02d}",
        "detik": f"{now.second:02d}",
        "ampm": ampm,
        "hari": hari[now.weekday() + 1 if now.weekday() < 6 else 0], # Penyesuaian
        "tanggal": now.day,
        "bulan": bulan[now.month - 1],
        "tahun": now.year
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)