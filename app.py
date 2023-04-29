from flask import Flask,render_template,flash,redirect,url_for,session, logging,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/eray2/Desktop/ToDoProject/todos.db"
db = SQLAlchemy(app)

class Todos(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    isDone = db.Column(db.Boolean())


@app.route('/')
def index():
    todos = Todos.query.all()
    return render_template('index.html',todos=todos)

@app.route('/add_todo', methods=['POST'])
def add_todo():
    title = request.form['title']
    description = request.form['description']
    todo = Todos(title=title, content=description,isDone = 0)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/delete<string:id>')
def delete(id):
    todo = Todos.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/done/<string:id>')
def done(id):
    
    done = Todos.query.filter_by(id = id).first()
    if done.isDone == False:
        done.isDone = True
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/ny/<string:id>')
def ny(id):
    background_color = "background-color:  rgba(255, 0, 0, 0.5);"
    ny = Todos.query.filter_by(id = id).first()
    print(ny)
    if ny.isDone == True:
        ny.isDone = False
    db.session.commit()
    return redirect(url_for("index"))


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)