from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Veritabanı yapılandırması
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Görev modeli
class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# Uygulama bağlamı içinde tabloyu oluştur
with app.app_context():
    db.create_all()

# Yeni görev ekleme endpoint’i
@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    if not data or 'description' not in data:
        return jsonify({"error": "Görev açıklaması gerekli"}), 400

    task = Task(description=data['description'])
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Görev eklendi"}), 201

# Görev listesini alma endpoint’i
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    result = [
        {
            "id": task.id,
            "description": task.description,
            "completed": task.completed
        } for task in tasks
    ]
    return jsonify(result), 200

# Ana uygulama çalıştırıcısı
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5055)
