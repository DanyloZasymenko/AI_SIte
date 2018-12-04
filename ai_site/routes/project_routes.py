from flask import render_template, flash, url_for, redirect, request

from ai_site import app, db
from ai_site.forms import ProjectForm
from ai_site.models.project import Project, ProjectPicture
from ai_site.utils import save_picture


@app.route("/project/save", methods=['GET', 'POST'])
def project_save():
    form = ProjectForm()
    if form.validate_on_submit():
        print(form.year.data)
        print(form.semester.data)
        project = Project(title=form.title.data, description=form.description.data, authors=form.authors.data,
                          url=form.url.data, image=save_picture(form.image.data, 'project_pics'))
        for picture in form.pictures.data:
            project_pict = ProjectPicture(image=save_picture(picture, 'project_pics'), project=project)
            db.session.add(project_pict)
        db.session.add(project)
        db.session.commit()
        flash('The project has been added!', 'success')
        return redirect(url_for('project_get_all'))
    return render_template("project/new_project.html", title='Add Project', form=form, legend='Add')


@app.route("/project/get-all")
def project_get_all():
    return render_template("project/project_all.html", title='Project', projects=Project.query.all())


@app.route("/project/update/<int:project_id>", methods=['GET', 'POST'])
def project_update(project_id):
    form = ProjectForm()
    project = Project.query.get_or_404(project_id)
    if form.validate_on_submit():
        if form.image.data:
            project.image = save_picture(form.image.data, 'project_pics')
        project.title = form.title.data
        project.description = form.description.data
        project.authors = form.authors.data
        project.url = form.url.data
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
    return render_template("project/new_project.html", title='Update Project', form=form, legend='Update')


@app.route("/project/delete/<int:project_id>")
def project_delete(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('project_get_all'))


@app.route("/project/delete-picture/<int:picture_id>")
def project_delete_picture(picture_id):
    picture = ProjectPicture.query.get_or_404(picture_id)
    db.session.delete(picture)
    db.session.commit()
    return redirect(url_for('project_get_all'))
