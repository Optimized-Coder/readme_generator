from flask import render_template, request
from . import bp

@bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        doc_title = request.form.get('title')
        repo_link = request.form.get('repo_link')
        bugs_link = request.form.get('bugs_link')
        tech_used = request.form.get('tech_used')
        author = request.form.get('author')
        print(f'Title: {doc_title}\nRepo Link: {repo_link}\nBugs Link: {bugs_link}\nTech Used: {tech_used}\nAuthor: {author}')

    return render_template(
        'index.html',
        title='README Generator',
    )