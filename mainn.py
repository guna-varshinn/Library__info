# # # import sqlite3
# # #
# # # db=sqlite3.connect("library_books.db")
# # # cursor=db.cursor()
# # # #cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# # # cursor.execute("INSERT INTO books VALUES( 1, 'heroslife','guna','10')")
# # # db.commit()
# from flask import Flask, session
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     bookname = db.Column(db.String(80), unique=True, nullable=False)
#     author = db.Column(db.String(120), unique=False, nullable=False)
#     rating = db.Column(db.Float, unique=False, nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username
#
#
# db.create_all()
#
# book1 = User(id=1, bookname="heroslife", author="guna", rating=10)
#
# db.session.add(book1)
# # alll=session.quer(User).all()
# # print(alll)
# db.session.commit()
