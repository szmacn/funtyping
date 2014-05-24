from flask import Flask,url_for,request,render_template,make_response,session,redirect,escape


app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s ' % escape(session['username'])
    return redirect(url_for('login'))
    

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=login>
        </form>

    '''
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


#@app.route('/')
#def index():
#    return redirect(url_for('login'))

#@app.route('/login')
#def login():
#    #abort(401)
#    #this_is_never_executed()
#    return render_template('login.html')

#@app.route('/send_cookie',methods=['GET','POST'])
#def send_cookie():
#    resp = make_response(render_template('login.html'))
#    resp.set_cookie('username','szmacn')
#    return resp

#@app.route('/recv_cookie',methods=['GET','POST'])
#def recv_cookie():
#    username = request.cookies.get('username')
#    return username


#@app.route('/')
#def index():
#    return 'Index Page'
#
#@app.route('/hello/')
#@app.route('/hello/<name>')
#def hello(name=None):
#    return render_template('hello.html',name=name)
#def hello():
#    return "Hello World!"
#
#@app.route('/user/<username>')
#def profile(username):
#    # show the user profile for that user
#    return 'User %s '% username
#
#@app.route('/post/<int:post_id>')
#def show_post(post_id):
#    #show the post with the given id ,the id is an integer
#    return 'Post %d '% post_id

#@app.route('/projects/')
#def projects():
#    return 'The project page'
#
#@app.route('/about')
#def about():
#    return 'The about page'
#@app.route('/index/')
#def index():
#    return render('login.html')
#
#@app.route('/login',methods=['GET','POST'])
#def login():
#    error = None
#    if request.method == 'POST':
#        if valid_login(request.form['username'],request.form['password']):
#            return log_the_user_in(request.form['username'])
#        else:
#            error = "Invalid username/password"
#        #do_the_login()
#        #return "post method"
#    #else:
#        #show_the_login_form()
#        #return "get method"
#    return render_template('login.html',error=error)
#
#def valid_login(username,password):
#    if len(username) <8 or len(password) < 8:
#        return False
#    else:
#        return True
#
#def log_the_user_in(username):
#    return username
#

#with app.test_request_context():
#    print url_for('index')
#    print url_for('login')
#    print url_for('login',next='/')
#    print url_for('profile',username='John Doe')


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
