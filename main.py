from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.environ.get('MYSQL_USER')}:{os.environ.get('MYSQL_PASSWORD')}"
    f"@{os.environ.get('MYSQL_HOST')}:3306/{os.environ.get('MYSQL_DATABASE')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Astronaut(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    image = db.Column(db.String(50))
    country = db.Column(db.String(50))

@app.route('/')
def index():
    
    astronauts = Astronaut.query.all()

    return render_template('index.html', astronauts=astronauts)

@app.route('/usa')
def usa_cosm():
    astronauts_usa = Astronaut.query.filter_by(country="США").all()
    return render_template('usa.html', astronauts=astronauts_usa)

@app.route('/ussr')
def ussr_cosm():
    astronauts_ussr = Astronaut.query.filter_by(country="СССР").all()
    return render_template("ussr.html", astronauts=astronauts_ussr)

with app.app_context():
    db.create_all()
    
    if Astronaut.query.count() == 0:
        names = ["Нил Армстронг", "Базз Олдрин", "Джон Гленн", 
                 "Юрий Гагарин", "Валентина Терешкова", "Алексей Леонов"]
        homeland = ["США", "США", "США", "СССР", "СССР", "СССР"]
        descriptions = [
            "Первый человек, ступивший на Луну (1969 год, миссия Аполлон-11).",
            "Второй человек на Луне, пилот лунного модуля Аполлон-11.",
            "Первый американец, совершивший орбитальный космический полёт (1962).",
            "Первый человек, совершивший космический полёт.",
            "Первая в мире женщина-космонавт.",
            "Первый человек в мире, вышедший в открытый космос."
        ]
        images = ["armstrong.jpg", "aldrin.jpg", "glenn.jpg", 
                  "gagarin.jpg", "tereshkova.jpg", "leonov.jpg"]
        
        for i in range(len(names)):
            test_astronaut = Astronaut(
                name=names[i], 
                country=homeland[i], 
                description=descriptions[i], 
                image=images[i]
            )
            db.session.add(test_astronaut)
        db.session.commit()
        print(f"Добавлено {Astronaut.query.count()} космонавтов")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)