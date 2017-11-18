from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm, WeanForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/weaning', methods=['GET', 'POST'])
def weaning():
    form = WeanForm()
    if form.validate_on_submit():
        flash('{} piglets from {} litters'.format(form.n_weaned.data,
                                                  form.n_litters.data))
        return redirect('/index')
    return render_template('weaning_input.html',
                           title='enter wean dtls',
                           form=form)