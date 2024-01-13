from flask import Flask, render_template, request, redirect
from surveys import satisfaction_survey

responses = []
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("start_page.html", satisfaction_survey)

@app.route('/questions/<int:question_id>')
def show_question(question_id):

    if len(responses) == len(satisfaction_survey.questions):
        return redirect('/thanks')
    else:
        return render_template("questions.html", question=satisfaction_survey.questions[question_id])

@app.route('/answer')
def save_response():
    answer_choice = request.form['answer']
    responses.append(answer_choice)

    return redirect(f"/questions/{len(responses)}")

@app.route('/thanks')
def thank_you():
    return render_template("thanks.html")

