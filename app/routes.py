from flask import render_template, redirect, url_for, flash, send_from_directory
from app import app
from app import db 
from app.forms import AnnouncementForm
from app.models import Announcement
from datetime import datetime 
from weasyprint import HTML 

@app.route('/')
@app.route('/index')
def index():
    announcements = Announcement.query.all()
    return render_template('index.html', announcements = announcements)

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = AnnouncementForm()
    if form.validate_on_submit():
        announcement = Announcement(
            title=form.title.data,
            body=form.body.data,
            datetime=form.dt.data,
            location = form.location.data
        )
        db.session.add(announcement)
        db.session.commit()
        flash('Created Successfully!')
        return redirect(url_for('index'))
    
    return render_template('create.html', form=form)

@app.route('/render/<id>')
def render(id):
    announcement = Announcement.query.filter_by(id=id).first_or_404()
    data = {}
    data['title'] = announcement.title 
    data['body'] = announcement.body
    data['datestring'] = announcement.datetime.strftime("%B %d, %Y")
    data['timestring'] = announcement.datetime.strftime("%H:%M")
    data['location'] = announcement.location 
    data['id'] = id
    return render_template('render.html', data = data)

@app.route('/generate_pdf/<id>')
def generate_pdf(id):
    announcement = Announcement.query.filter_by(id=id).first_or_404()
    data = {}
    data['title'] = announcement.title 
    data['body'] = announcement.body
    data['datestring'] = announcement.datetime.strftime("%B %d, %Y")
    data['timestring'] = announcement.datetime.strftime("%H:%M")
    data['location'] = announcement.location 
    html = render_template('pdf.html', data=data)
    path = app.config['PDF_PATH']
    fname = data['title'].replace(' ', '_') + '.pdf'
    stylesheets = [path + 'style.css']
    doc = HTML(string=html).write_pdf(path +fname, stylesheets=stylesheets)
    return send_from_directory(path, filename=fname, as_attachment=True)