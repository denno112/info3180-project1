import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from werkzeug.utils import secure_filename
from app.models import PropertyInfo
from app.forms import PropertyForm

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=['POST', 'GET'])
def property():
    form = PropertyForm()

    if request.method == "POST":

        if form.validate_on_submit():
            title = form.title.data
            description = form.description.data
            bedrooms = form.bedrooms.data
            bathrooms = form.bathrooms.data
            price = form.price.data
            pType = form.pType.data
            location = form.location.data
            photo = form.photo.data

            filename = secure_filename(photo.filename)

            newProperty = PropertyInfo(
                title, description, bedrooms, bathrooms, price, pType, location, filename)
            db.session.add(newProperty)
            db.session.commit()

            photo.save(os.path.join(
                app.config['UPLOAD_FOLDER'], filename
            ))

            flash('Property Added Successfully', 'success')
            return redirect(url_for('getProperties'))
    return render_template("newproperty.html", form = form)


@app.route('/properties')
def getProperties():
    """Render the website's properties page."""
    properties = PropertyInfo.query.all()
    return render_template('properties.html', properties=properties)


@app.route('/properties/<propertyid>')
def getProperty(propertyid):
    """Render the website's individual property page."""
    idvProperty = PropertyInfo.query.filter_by(id=propertyid).first()
    return render_template('property.html', property=idvProperty)


@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
