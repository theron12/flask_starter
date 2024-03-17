"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for


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

@app.route('/properties/create',methods=["GET","POST"])
def create():
    myform=PropertyForm()
    if request.method=="POST":
        if myform.validate_on_submit():
            title=myform.title.data
            desc=myform.description.data
            rooms=myform.rooms.data
            bathrooms=myform.bathrooms.data
            price=myform.price.data
            ptype=dict(myform.ptype.choices).get(myform.ptype.data)
            #print(ptype)
            loc=myform.location.data
            photo=myform.photo.data

            #saving photo to file
            filename=secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            #saving property to database
            prop=Property(title,desc,rooms,bathrooms,price,ptype,loc,filename)
            db.session.add(prop)
            db.session.commit()
            
            # success flash message
            flash("Property added","success")

            #redirect to properties page
            return redirect(url_for('properties'))        
        else:
            #flash_errors(myform)
            return render_template('createp.html',form=myform)
   
    else:
        return render_template('createp.html',form=myform)

@app.route('/properties',methods=["GET"])
def properties():
     # retrieve list of properties
    proplist=db.session.query(Property).all()
   
    # return render template properties
    return render_template('properties.html',plist=proplist)

@app.route('/properties/<pid>') 
def showproperty(pid):
    p=Property.query.get(pid)
    return render_template('showprop.html',property=p)

@app.route('/property/image/<filename>')
def get_image(filename):
    #print("IMG URL"+os.getcwd())
    return send_from_directory(os.getcwd()+"/"+app.config['UPLOAD_FOLDER'],filename)




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




if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
