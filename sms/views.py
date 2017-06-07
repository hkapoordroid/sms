"""
Routes and views for the flask application.
"""
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from datetime import datetime
from sms import app
from wtforms import StringField, BooleanField, SelectField, TextAreaField
import awshelper


Types = ['Shoes', 'Watch', 'Hangbag', 'Clothes']


class UploadForm(FlaskForm):
    gaphoto = FileField('Example File')
    gatype = SelectField("gatype", choices=[(f, f) for f in Types])
    gatitle = StringField("gatitle")
    gadescription = TextAreaField("description")


@app.route('/sga', methods=['POST', 'GET'])
def upload_page():
    form = UploadForm()
    if form.validate_on_submit():
        print(form.gaphoto.data.filename)
        s3PhotoUrl = awshelper.upload_image_to_s3(form.gaphoto)

        #get the fields to display
        rwtitle = str(form.gatitle.data)
        rwdescription = str(form.gadescription.data)
        rwtype = str(form.gatype.data)
        rwphoto = "<img src=\"" + s3PhotoUrl + "\" height=\"150\" width=\"75\">"
        

        #now lets review the giveaway before final submission
        return render_template('giveawayconfirmation.html')
        
		#output = s3_upload(form.example)
        #flash('{src} uploaded to S3 as {dst}'.format(src=form.example.data.filename, dst=output))
    return render_template('giveawayform.html', form=form)