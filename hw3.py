# Создать форму для регистрации пользователей на сайте. Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль"
# и кнопку "Зарегистрироваться". При отправке формы данные должны сохраняться в базе данных, а пароль должен быть
# зашифрован.

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from forms import RegistrationForm
from models import db, Registers
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = b'0cfafd85fbe8046ce54db3d96d7ab752c9b80df76d8ec24bc6e6737b4f543cbf'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        init_db()
        add_user(form)
        return render_template('register_ok.html', form=form)
    return render_template('register.html', form=form)


def init_db():
    db.create_all()

def hash_password(password):
    hash_object = hashlib.sha256()
    hash_object.update(password.encode('utf-8'))
    password_hash = hash_object.hexdigest()
    return password_hash

def add_user(form):
    new_user = Registers(name=form.name.data, lastname=form.lastname.data, email=form.email.data, password=hash_password(form.password.data))
    db.session.add(new_user)
    db.session.commit()

if __name__ == '__main__':
    app.run('0.0.0.0', port= 5000, debug=True)