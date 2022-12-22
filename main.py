from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookname = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    def __init__(self, id, bookname, author, rating):
        self.rating = rating
        self.author = author
        self.id = id
        self.bookname = bookname


@app.route('/')
def home():
    db.create_all()
    all_books = User.query.all()
    #print(all_books)
    return render_template("index.html", books=all_books)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        #POST should be caps
        book_id = request.form["id"]
        User.query.get(book_id).rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = User.query.get(book_id)
    return render_template("edit.html", book=book_selected)

@app.route("/delete")
def delete():
    book_id=request.args.get("id")
    book_is=User.query.get(book_id)
    db.session.delete(book_is)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        db.session.add(User(id=len(all_books) + 1, bookname=new_book["title"], author=new_book["author"],
                            rating=new_book["rating"]))
        db.session.commit()
        # NOTE: You can use the redirect method from flask to redirect to another route
        # e.g. in this case to the home page after the form has been submitted.
        return redirect(url_for('home'))

    return render_template("add.html")


if __name__ == "__main__":
    db.create_all()
    all_books = User.query.all()
    print(all_books)
    app.run(debug=True)
