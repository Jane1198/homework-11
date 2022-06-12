import utils
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def page_list():
    candidates = utils.load_candidates()
    return render_template('list.html', candidates=candidates)

@app.route("/candidate/<int:id>/")
def page_candidate_by_id(id):
    candidates = utils.get_candidate_by_id(id)
    return render_template('card.html', candidates=candidates)

@app.route("/search/<int:candidate_name>/")
def page_candidate_by_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    quantity = len(candidates)
    return render_template('search.html', candidates=candidates, quantity=quantity)

@app.route("/skills/<int:skill_name>/")
def page_candidates_by_skills(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    quantity = len(candidates)
    return render_template('skill.html', candidates=candidates, quantity=quantity, skill_name=skill_name)


app.run(debug=True)
