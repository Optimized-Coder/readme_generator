from flask import render_template, request, session, url_for, redirect
from . import bp



@bp.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        doc_title = request.form.get('title')
        desc = request.form.get('desc')
        repo_link = request.form.get('repo_link')
        bugs_link = request.form.get('bugs_link')
        tech_used = request.form.get('tech_used')
        author = request.form.get('author')
        email = request.form.get('email')
        username = request.form.get('username')

        session['doc_title'] = doc_title
        session['desc'] = desc
        session['repo_link'] = repo_link
        session['bugs_link'] = bugs_link
        session['tech_used'] = tech_used
        session['author'] = author
        session['email'] = email
        session['username'] = username

        return redirect(url_for('main.template'))

    context = {
        'title': 'README Generator',
    }

    return render_template(
        'index.html',
        **context
    )

@bp.route('/template', methods=['GET', 'POST'])
def template():
    doc_title = session.get('doc_title', None)
    repo_link = session.get('repo_link', None)
    bugs_link = session.get('bugs_link', None)
    tech_used = session.get('tech_used', None)
    author = session.get('author', None)
    email = session.get('email', None)


    context = {
        'title': 'Your Template',
        'doc_title': doc_title,
        'repo_link': repo_link,
        'bugs_link': bugs_link,
        'tech_used': tech_used,
        'author': author,
        'email': email,
        
    }

    return render_template(
        'template.html',
    )