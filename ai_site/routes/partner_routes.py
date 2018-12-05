from flask import render_template, flash, url_for, redirect, request

from ai_site import app, db
from ai_site.forms import PartnerForm
from ai_site.models.partner import Partner
from ai_site.utils import save_picture, delete_picture


@app.route("/partner/save", methods=['GET', 'POST'])
def partner_save():
    form = PartnerForm()
    if form.validate_on_submit():
        partner = Partner(name=form.name.data, description=form.description.data,
                          image=save_picture(form.image.data, "partner_pics"))
        db.session.add(partner)
        db.session.commit()
        flash('The partner has been added!', 'success')
        return redirect(url_for('partner_get_all'))
    return render_template("partner/new_partner.html", title='Add Partner', form=form, legend='Add')


@app.route("/partner/get-all")
def partner_get_all():
    return render_template("partner/partner_all.html", title='Partners', partners=Partner.query.all())


@app.route("/partner/update/<int:partner_id>", methods=['GET', 'POST'])
def partner_update(partner_id):
    partner = Partner.query.get_or_404(partner_id)
    form = PartnerForm()
    if form.validate_on_submit():
        if form.image.data:
            partner.image = save_picture(form.image.data, "partner_pics")
        partner.name = form.name.data
        partner.description = form.description.data
        db.session.commit()
        flash('The partner has been updated!', 'success')
        return redirect(url_for('partner_get_all'))
    elif request.method == 'GET':
        form.name.data = partner.name
        form.description.data = partner.description
    return render_template("partner/new_partner.html", title='Update Partner', form=form, legend='Update')


@app.route("/partner/delete/<int:partner_id>")
def partner_delete(partner_id):
    partner = Partner.query.get_or_404(partner_id)
    delete_picture('partner_pics', partner.image)
    db.session.delete(partner)
    db.session.commit()
    flash('The partner has been deleted!', 'danger')
    return redirect(url_for('partner_get_all'))
