from flask import Flask, render_template, request, redirect, url_for
from job_ser import get_jobs, subscribe_user


app = Flask(__name__)

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# Jobs listing route
@app.route('/jobs')
def job_list():
    jobs = get_jobs()
    return render_template('job_list.html', jobs=jobs)

# Subscription route
@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    preferences = request.form.get('preferences')
    subscribe_user(email, preferences)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
