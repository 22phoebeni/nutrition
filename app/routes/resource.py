from app import app, login
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Resource
from app.classes.forms import ResourceForm
from flask_login import login_required
import datetime as dt

@app.route('/resource/new', methods=['GET', 'POST'])
# This means the user must be logged in to see this page
@login_required
# This is a function that is run when the user requests this route.
def resourceNew():
    # This gets the form object from the form.py classes that can be displayed on the template.
    form = ResourceForm()

    # This is a conditional that evaluates to 'True' if the user submitted the form successfully.
    # validate_on_submit() is a method of the form object. 
    if form.validate_on_submit():

        # This stores all the values that the user entered into the new post form. 
        # Post() is a mongoengine method for creating a new post. 'newPost' is the variable 
        # that stores the object that is the result of the Post() method.  
        newResource = Resource(
            # the left side is the name of the field from the data table
            # the right side is the data the user entered which is held in the form object.
            owner = current_user.id,
            title = form.title.data
        )
        if form.image.data:
            newResource.image.put(form.image.data, content_type = 'image/jpeg')
        # This is a method that saves the data to the mongoDB database.
        newResource.save()

        # Once the new post is saved, this sends the user to that post using redirect.
        # and url_for. Redirect is used to redirect a user to different route so that 
        # routes code can be run. In this case the user just created a post so we want 
        # to send them to that post. url_for takes as its argument the function name
        # for that route (the part after the def key word). You also need to send any
        # other values that are needed by the route you are redirecting to.
        return redirect(url_for('resource',resourceID=newResource.id))

    # if form.validate_on_submit() is false then the user either has not yet filled out
    # the form or the form had an error and the user is sent to a blank form. Form errors are 
    # stored in the form object and are displayed on the form. take a look at postform.html to 
    # see how that works.
    return render_template('resourceform.html',form=form)
