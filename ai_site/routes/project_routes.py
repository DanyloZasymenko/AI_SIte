from flask import render_template, flash, url_for, redirect, request
from flask_login import login_required

from ai_site import app, db
from ai_site.forms import ProjectForm
from ai_site.models.project import Project, ProjectPicture
from ai_site.utils import save_picture, delete_picture


@app.route("/projects/<int:year>/page/<int:page_number>")
def projects(year, page_number):
    page = request.args.get('page', page_number, type=int)
    projects = Project.query.filter_by(year=year).order_by(Project.semester.desc()).paginate(page=page, per_page=12)
    return render_template("projects.html", title='Projects', year=year, project_list=projects)


@app.route("/project/save", methods=['GET', 'POST'])
@login_required
def project_save():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(title=form.title.data, description=form.description.data, authors=form.authors.data,
                          url=form.url.data, image=save_picture(form.image.data, 'project_pics'),
                          year=form.year.data, semester=form.semester.data)
        if not form.pictures.data[0] == '':
            for picture in form.pictures.data:
                project_pict = ProjectPicture(image=save_picture(picture, 'project_pics'), project=project)
                db.session.add(project_pict)
        db.session.add(project)
        db.session.commit()
        flash('The project has been added!', 'success')
        return redirect(url_for('project_get_all'))
    return render_template("project/new_project.html", title='Add Project', form=form, legend='Add')


@app.route("/project/get-all")
@login_required
def project_get_all():
    return render_template("project/project_all.html", title='Project', projects=Project.query.all())


@app.route("/project/update/<int:project_id>", methods=['GET', 'POST'])
@login_required
def project_update(project_id):
    form = ProjectForm()
    project = Project.query.get_or_404(project_id)
    if form.validate_on_submit():
        if form.image.data:
            delete_picture('project_pics', project.image)
            project.image = save_picture(form.image.data, 'project_pics')
        project.title = form.title.data
        project.description = form.description.data
        project.authors = form.authors.data
        project.url = form.url.data
        project.year = form.year.data
        project.semester = form.semester.data
        for picture in form.pictures.data:
            project_pict = ProjectPicture(image=save_picture(picture, 'project_pics'), project=project)
            db.session.add(project_pict)
        db.session.commit()
        flash('The project has been updated!', 'success')
        return redirect(url_for('project_get_all'))
    elif request.method == 'GET':
        form.title.data = project.title
        form.description.data = project.description
        form.authors.data = project.authors
        form.url.data = project.url
        form.year.data = project.year
        form.semester.data = project.semester
    return render_template("project/new_project.html", title='Update Project', form=form, legend='Update')


@app.route("/project/delete/<int:project_id>")
@login_required
def project_delete(project_id):
    project = Project.query.get_or_404(project_id)
    delete_picture('project_pics', project.image)
    for picture in project.pictures:
        delete_picture('project_pics', picture.image)
    db.session.delete(project)
    db.session.commit()
    flash('The project has been deleted!', 'danger')
    return redirect(url_for('project_get_all'))


@app.route("/project/delete-picture/<int:picture_id>")
@login_required
def project_delete_picture(picture_id):
    picture = ProjectPicture.query.get_or_404(picture_id)
    delete_picture('project_pics', picture.image)
    db.session.delete(picture)
    db.session.commit()
    return redirect(url_for('project_get_all'))
