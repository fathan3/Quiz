from werkzeug.security import generate_password_hash, check_password_hash

# ---------------- User Admin ----------------
class User:
    def __init__(self, db, username, password):
        self.db = db
        self.username = username
        self.password = password

    def authenticate(self):
        cursor = self.db.connection.cursor()
        cursor.execute(
            "SELECT id, username, password, role FROM users WHERE username=%s",
            (self.username,)
        )
        user = cursor.fetchone()
        if user:
            user_id, username_db, password_db, role = user
            # Cek password plaintext (sementara) atau hash
            if self.password == password_db and role == 'admin':
                return {'id': user_id, 'username': username_db}
        return None


# ---------------- QuizCard ----------------
class QuizCard:
    def __init__(self, db, id=None, question=None, option_a=None, option_b=None,
                 option_c=None, option_d=None, answer=None):
        self.db = db
        self.id = id
        self.question = question
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.option_d = option_d
        self.answer = answer

    def to_dict(self):
        return {
            'id': self.id,
            'question': self.question,
            'option_a': self.option_a,
            'option_b': self.option_b,
            'option_c': self.option_c,
            'option_d': self.option_d,
            'answer': self.answer
        }

    def save(self):
        """Insert card ke database"""
        cursor = self.db.connection.cursor()
        ans = self.answer.upper() if self.answer else ''
        cursor.execute(
            "INSERT INTO quiz_cards (question, option_a, option_b, option_c, option_d, answer) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (self.question, self.option_a, self.option_b, self.option_c, self.option_d, ans)
        )
        self.db.connection.commit()
        self.id = cursor.lastrowid

    def update(self):
        """Update card yang sudah ada"""
        if not self.id:
            raise ValueError("Card harus punya id untuk update")
        ans = self.answer.upper() if self.answer else ''
        cursor = self.db.connection.cursor()
        cursor.execute(
            "UPDATE quiz_cards SET question=%s, option_a=%s, option_b=%s, option_c=%s, option_d=%s, answer=%s "
            "WHERE id=%s",
            (self.question, self.option_a, self.option_b, self.option_c, self.option_d, ans, self.id)
        )
        self.db.connection.commit()

    def delete(self):
        """Hapus card dari database"""
        if not self.id:
            raise ValueError("Card harus punya id untuk delete")
        cursor = self.db.connection.cursor()
        cursor.execute("DELETE FROM quiz_cards WHERE id=%s", (self.id,))
        self.db.connection.commit()

    @staticmethod
    def get_all(db):
        cursor = db.connection.cursor()
        cursor.execute("SELECT id, question, option_a, option_b, option_c, option_d, answer FROM quiz_cards")
        result = cursor.fetchall()
        return [QuizCard(db,
                         id=row[0],
                         question=row[1],
                         option_a=row[2],
                         option_b=row[3],
                         option_c=row[4],
                         option_d=row[5],
                         answer=row[6]) for row in result]

# ---------------- QuizManager ----------------
class QuizManager:
    def __init__(self, db, guest_name=None):
        self.db = db
        self.guest_name = guest_name
        self.score = 0

    def check_answer(self, question_id, selected):
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT answer FROM quiz_cards WHERE id=%s", (question_id,))
        answer = cursor.fetchone()
        if answer and answer[0] and answer[0].upper() == selected.upper():
            self.score += 1
            return True
        return False

    def save_score(self):
        cursor = self.db.connection.cursor()
        cursor.execute("INSERT INTO scores (guest_name, score) VALUES (%s, %s)",
                       (self.guest_name, self.score))
        self.db.connection.commit()
