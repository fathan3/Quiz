from app import app, mysql
from flask import render_template, request, redirect, url_for, session, jsonify
from models import User, QuizCard, QuizManager

app.secret_key = app.config['SECRET_KEY']

# ---------------- INDEX ----------------
@app.route('/')
def index():
    return render_template('index.html')

# ---------------- LOGIN ADMIN ----------------
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        user = User(mysql, username, password)
        auth = user.authenticate()
        if auth:
            session['user_id'] = auth['id']
            session['username'] = auth['username']
            return redirect(url_for('admin_panel'))
        else:
            return render_template('login.html', error="Username/Password salah")
    return render_template('login.html')

# ---------------- ADMIN PANEL ----------------
@app.route('/admin', methods=['GET', 'POST'])
def admin_panel():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'add':
            card = QuizCard(
                db=mysql,
                question=request.form['question'],
                option_a=request.form['option_a'],
                option_b=request.form['option_b'],
                option_c=request.form['option_c'],
                option_d=request.form['option_d'],
                answer=request.form['answer']
            )
            card.save()

        elif action == 'edit':
            card = QuizCard(
                db=mysql,
                id=int(request.form['id']),
                question=request.form['question'],
                option_a=request.form['option_a'],
                option_b=request.form['option_b'],
                option_c=request.form['option_c'],
                option_d=request.form['option_d'],
                answer=request.form['answer']
            )
            card.update()

        elif action == 'delete':
            card = QuizCard(db=mysql, id=int(request.form['id']))
            card.delete()

        return redirect(url_for('admin_panel'))

    cards = QuizCard.get_all(mysql)
    return render_template('admin.html', cards=cards)

# ---------------- QUIZ GUEST ----------------
@app.route('/quiz')
def quiz():
    cards_obj = QuizCard.get_all(mysql)
    cards = [c.to_dict() for c in cards_obj]
    return render_template('quiz.html', cards=cards)

# ---------------- SUBMIT QUIZ ----------------
@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    data = request.get_json()
    guest_name = data.get('guest_name', 'Guest')
    answers_list = data.get('answers', [])

    qm = QuizManager(mysql, guest_name)

    for ans in answers_list:
        qid, selected = ans['id'], ans['selected']
        qm.check_answer(int(qid), selected)

    qm.save_score()

    return jsonify({'score': qm.score})

# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
