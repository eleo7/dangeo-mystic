
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

auth_bp = Blueprint("auth", __name__)

def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        db = get_db()
        user = db.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            return redirect(url_for("index"))
        flash("Credenciais inválidas.")
    return render_template("login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        db = get_db()
        existing_user = db.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        if existing_user:
            flash("Usuário já existe.")
            return redirect(url_for("auth.register"))
        hashed_password = generate_password_hash(password)
        db.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed_password))
        db.commit()
        flash("Registrado com sucesso. Faça login.")
        return redirect(url_for("auth.login"))
    return render_template("register.html")
