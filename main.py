from flask import Flask, render_template, request, redirect, url_for, flash
from flask import send_file
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import SubmitField, StringField
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
import smtplib

app = Flask(__name__)
# app wont  work without security autorisation
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['TEMPLATES_AUTO_RELOAD'] = True
bootstrap = Bootstrap(app)
ckeditor = CKEditor(app)

class ContactForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    name = StringField('Name', validators=[InputRequired()])
    message = CKEditorField('Message', validators=[InputRequired()])
    submit = SubmitField('Send')



@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == "POST":
        return render_template('index.html')

other_email = "afolayantimilola880@gmail.com"
my_email = "isaacpythondev@gmail.com"
password = "bkxcjvzkoiwshpok"
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)

@app.route('/contact-me', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        title_of_message = form.title.data
        name_of_sender = form.name.data
        message = form.message.data
        flash('Message sent !!')
        connection.sendmail(from_addr=my_email, to_addrs=other_email, msg=f"subject:{title_of_message} \n\n "
                                                                          f"name of sender {name_of_sender} \n\n "
                                                                          f"{message}")
        connection.close()
        return redirect(url_for('main'))
    return render_template('contact.html', form=form)

@app.route('/download')
def download():
    path = 'Afolayan_Isaac_Ademide+resume.docx'
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
