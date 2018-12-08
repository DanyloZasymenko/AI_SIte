from flask import render_template, flash, url_for, redirect, request
from flask_login import login_required

from ai_site import app, db
from ai_site.forms import CourseForm
from ai_site.models.course import Course


@app.route("/course/save", methods=['GET', 'POST'])
@login_required
def course_save():
    form = CourseForm()
    if form.validate_on_submit():
        course = Course(name=form.name.data, credits=form.credits.data, year=form.year.data,
                        semester=form.semester.data)
        db.session.add(course)
        db.session.commit()
        flash('The course has been added!', 'success')
        return redirect(url_for('course_get_all'))
    return render_template("course/new_course.html", title='Add Course', form=form, legend='Add')


@app.route("/course/get-all")
@login_required
def course_get_all():
    return render_template("course/course_all.html", title='Course', courses=Course.query.all())


@app.route("/course/update/<int:course_id>", methods=['GET', 'POST'])
@login_required
def course_update(course_id):
    course = Course.query.get_or_404(course_id)
    form = CourseForm()
    if form.validate_on_submit():
        course.name = form.name.data
        course.credits = form.credits.data
        course.year = form.year.data
        course.semester = form.semester.data
        db.session.commit()
        flash('The course has been updated!', 'success')
        return redirect(url_for('course_get_all'))
    elif request.method == 'GET':
        form.name.data = course.name
        form.credits.data = course.credits
        form.year.data = course.year
        form.semester.data = course.semester
    return render_template("course/new_course.html", title='Update Course', form=form, legend='Update')


@app.route("/course/delete/<int:course_id>")
@login_required
def course_delete(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    flash('The course has been deleted!', 'danger')
    return redirect(url_for('course_get_all'))
