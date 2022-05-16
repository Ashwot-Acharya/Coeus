from flask import Flask , render_template,url_for,request,redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
app.config['WHOOSH_BASE'] = 'whoosh'
db = SQLAlchemy(app)


class News(db.Model):
    id = db.Column(db.Integer ,primary_key = True )
    title = db.Column(db.String(300),nullable = False)
    body = db.Column(db.String(2000),nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    
    def __repr__(self):
        return '<Task %r>' %self.id
        

@app.route("/")
def hello_world():
        Ne = News.query.order_by(News.date_created).all()
        return render_template('home.html', news =  Ne)

@app.route('/arti',methods=['POST'])
def get_arti():
    if request.method=='POST':
        task = request.form['content']
        get = News.query.filter_by(title=task).order_by(News.date_created).all()
        
        return render_template('home.html',news = get)
    else:
        pass
     
    

def add_news(title_new , body_main):
    ok = News(title = title_new, body = body_main)
    try:
        db.session.add(ok)
        db.session.commit()
        return "task successful"
    except Exception as E:
        return E
        






if __name__ == "__main__":
    app.run(debug=True)