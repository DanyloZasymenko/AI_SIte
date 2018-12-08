from flask import render_template, flash, url_for, redirect, request
from flask_login import login_required

from ai_site import app, db
from ai_site.forms import TeacherForm
from ai_site.models.teacher import Teacher
from ai_site.utils import save_picture, delete_picture


@app.route("/teachers/page/<int:page_number>")
def teachers(page_number):
    page = request.args.get('page', page_number, type=int)
    teachers = Teacher.query.order_by(Teacher.id.desc()).paginate(page=page, per_page=4)
    return render_template("teachers.html", title='Teachers', teachers_list=teachers)


@app.route("/teacher/save", methods=['GET', 'POST'])
@login_required
def teacher_save():
    form = TeacherForm()
    if form.validate_on_submit():
        teacher = Teacher(name=form.name.data, position=form.position.data, link=form.link.data, hobby=form.hobby.data,
                          incumbency=form.incumbency.data, description=form.description.data,
                          interests=form.interests.data,
                          research_directions=form.research_directions.data,
                          scopus_id=form.scopus_id.data,
                          scholar_id=form.scholar_id.data,
                          image=save_picture(form.image.data, 'teacher_pics'))
        db.session.add(teacher)
        db.session.commit()
        flash('The teacher has been added!', 'success')
        return redirect(url_for('teacher_get_all'))
    return render_template("teacher/new_teacher.html", title='Add teacher', form=form, legend='Add')


@app.route("/teacher/get-all")
@login_required
def teacher_get_all():
    return render_template("teacher/teacher_all.html", title='Teacher', teachers=Teacher.query.all())


@app.route("/teacher/update/<int:teacher_id>", methods=['GET', 'POST'])
@login_required
def teacher_update(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    form = TeacherForm()
    if form.validate_on_submit():
        teacher.name = form.name.data
        teacher.position = form.position.data
        teacher.link = form.link.data
        teacher.hobby = form.hobby.data
        teacher.incumbency = form.incumbency.data
        teacher.description = form.description.data
        teacher.interests = form.interests.data
        teacher.scopus_id = form.scopus_id.data
        teacher.scholar_id = form.scholar_id.data
        teacher.research_directions = form.research_directions.data
        if form.image.data:
            delete_picture('teacher_pics', teacher.image)
            teacher.image = save_picture(form.image.data, 'teacher_pics')
        db.session.commit()
        flash('The teacher has been updated!', 'success')
        return redirect(url_for('teacher_get_all'))
    elif request.method == 'GET':
        form.name.data = teacher.name
        form.position.data = teacher.position
        form.link.data = teacher.link
        form.hobby.data = teacher.hobby
        form.incumbency.data = teacher.incumbency
        form.description.data = teacher.description
        form.interests.data = teacher.interests
        form.research_directions.data = teacher.research_directions
        form.scopus_id.data = teacher.scopus_id
        form.scholar_id.data = teacher.scholar_id
    return render_template("teacher/new_teacher.html", title='Update teacher', form=form, legend='Update')


@app.route("/teacher/delete/<int:teacher_id>")
@login_required
def teacher_delete(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    delete_picture('teacher_pics', teacher.image)
    db.session.delete(teacher)
    db.session.commit()
    flash('The teacher has been deleted!', 'danger')
    return redirect(url_for('teacher_get_all'))
