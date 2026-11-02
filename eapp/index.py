import math

from flask import render_template, request, redirect
from eapp import app, dao, login ,utils
from flask_login import login_user, login_required, logout_user


@app.route('/')
def index():
    products = dao.load_products(kw=request.args.get('kw'),
                                 cate_id=request.args.get('category_id'),
                                 page=int(request.args.get('page', 1)))

    page_size = app.config['PAGE_SIZE']
    return render_template('index.html', products=products,
                           pages=math.ceil(dao.count_products()/page_size))

@app.route('/login')
def login_view():
    return render_template('login.html')

@app.route('/logout',methods=['post'])
@login_required
def log_out():
    logout_user()
    return redirect('/')

@app.route('/login', methods=['post'])
def login_process():
    username = request.form.get('username')
    password = request.form.get('password')

    u = dao.authenticate(username=username, password=password)
    if u:
        login_user(user=u)

    return redirect('/')

@app.route('/register')
def register_view():
    return render_template('register.html')

@app.route('/register', methods = ['post'])
def register_process():
    confirm=request.form.get('confirm')
    password=request.form.get('password')
    err_msg = None
    if not password or not confirm or confirm != password:
        err_msg='Mat khau khong khop !'
    else :
        data = request.form.copy()
        del data['confirm']
        dao.create_user(**data)

    return render_template('register.html',err_msg=err_msg)

@app.route('/api/carts', methods = ['post'])
def add_to_cart():
    id = str(request.json.get('id'))
    if id in cart:

    print(request.json)
    return {
        'total_amount':0,
        'total_quantity':0
    }


@app.context_processor
def common_responses():
    return {
        'categories': dao.load_categories()
    }

@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == '__main__':
    with app.app_context():
        from eapp import admin
        app.run(debug=True)
