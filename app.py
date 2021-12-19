from flask import Flask, render_template, request, redirect, url_for
from models import db, User, Responses
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inglhart.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/questionnaire")
def quest():
    return render_template('quest.html')


@app.route('/process', methods=['get'])
def answer_process():
    if not request.args:
        return redirect(url_for('quest'))
    # достаем параметры
    born_year = request.args.get('born_year')
    gender = request.args.get('gender')
    education = request.args.get('education')

    # создаем профиль пользователя
    user = User(
        born_year=born_year,
        gender=gender,
        education=education
    )

    db.session.add(user)
    db.session.commit()
    # получаем юзера с айди (автоинкремент)
    db.session.refresh(user)

    stress = request.args.get('stress')
    happiness = request.args.get('happiness')
    proudness = request.args.get('proudness')
    labor = request.args.get('labor')
    two_leaders = request.args.get('two_leaders')
    rules = request.args.get('rules')

    # привязываем к пользователю (см. модели в проекте)
    responses = Responses(id=user.id, stress=stress, happiness=happiness, proudness=proudness,
                          labor=labor, two_leaders=two_leaders, rules=rules)
    db.session.add(responses)
    db.session.commit()

    return 'Ok'


@app.route('/statistics')
def statistics():
    total = User.query.count()
    all_info = {}
    age_stats = db.session.query(
        func.avg(User.born_year),
        func.min(User.born_year),
        func.max(User.born_year)
    ).one()

    all_info['born_year_mean'] = age_stats[0]
    all_info['born_year_min'] = age_stats[1]
    all_info['born_year_max'] = age_stats[2]
    all_info['stress_mean'] = db.session.query(func.avg(Responses.stress)).one()[0]
    all_info['happiness_mean'] = db.session.query(func.avg(Responses.happiness)).one()[0]
    all_info['proudness_mean'] = db.session.query(func.avg(Responses.proudness)).one()[0]
    all_info['labor_mean'] = db.session.query(func.avg(Responses.labor)).one()[0]
    all_info['two_leaders_mean'] = db.session.query(func.avg(Responses.two_leaders)).one()[0]
    all_info['rules_mean'] = db.session.query(func.avg(Responses.rules)).one()[0]
    return render_template('statistics.html', all_info=all_info, total=total)


if __name__ == '__main__':
    app.run(debug=True)
