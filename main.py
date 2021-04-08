from flask import Flask, render_template
from random import randint
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/member')
def index():
    with open('templates/users.json', encoding="utf-8") as f:
        data = json.load(f)
    users = data["users"]
    random_member = users[randint(-100, 100) % len(users)]
    random_member["professions"].sort()
    return render_template("random_member.html", title="Случайный член экипажа", name=random_member["name"],
                           image=random_member["image"], list_prof=', '.join(random_member["professions"]))


if __name__ == '__main__':
    app.run()
