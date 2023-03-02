from flask import Flask, redirect, render_template,url_for,request,redirect,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.datastructures import ImmutableMultiDict
import os
from flask import session
import smtplib


port = int(os.environ.get('PORT', 5000))


app=Flask('__name__' ,template_folder='templates', static_folder='static')
app.secret_key = 'BAD_SECRET_KEY'
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path,'static'),'favicon.ico',mimetype='image/favicon.png')

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=="POST":
        try:
            a=request.form.getlist('email')[0]
            b=request.form.getlist('password')[0]
            session['email']=a
            session['password']=b
            return render_template('formFINAL.html')
        except:
            return render_template("Error.html")
    else:
        return render_template('loginpageFINAL.html')




#Saad Code
@app.route("/api/send_email", methods=["POST"])
def send_email():
    if request.method == 'POST':
        try:
            username =session['email']
            password =  session['password']
            print(username)
            # print(password)
            recipient = request.form['recipient']
            subject = request.form['subject']
            if (subject=="Others"):
                subject=request.form['subject1']
            venue= request.form['venue']
            date=request.form['date']


            
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(username, password)
            message=message_make(recipient,subject,venue,date,username)
            server.sendmail(username, recipient, message)
            server.close()
            return render_template('message.html')
        except:
            return render_template('Error.html')
    else:
        return render_template('Error.html')


def message_make(recipient,subject,venue,date,username):
    message=" "
    if (recipient=="mdsaad12386@gmail.com"):
        message=(f"Subject: Requesting permission to {subject} on {date} in {venue}\n\nSir,\nI hope this email finds you well. We have planned to {subject} on {date} at the {venue} and are requesting you to grant us the permission to do so.\n I would be grateful if you could grant us the permission to host the event on the specific date and\n venue and if not possible would like to discuss the possibility of conducting it at a different venue or\n on a different date.\n\nThanking You,\n{username}\n")
    elif (recipient=="csea@nitc.ac.in"):
        message=(f"Subject: Requesting permission to {subject} on {date} in {venue}\n\nSir,\nI hope this email finds you well. We have planned to {subject} on {date} at the {venue} and are requesting you to grant us the permission to do so.\n I would be grateful if you could grant us the permission to host the event on the specific date and\n venue and if not possible would like to discuss the possibility of conducting it at a different venue or\n on a different date.\n\nThanking You,\n{username}\n")
    elif(recipient=="_office.csas@nitc.ac.in"):
        message=(f"Subject: Checking the {subject}0 on {date}\n\nSir,\n\nI hope this email finds you well. I wanted to check the {subject} on {date} as we are\n hosting an event there on the specified date.\n\nI would be grateful if you could grant us the permission to host the event on the specified date and\n venue and if not possible would like to discuss the possibility of conducting it at a different venue or\n on a different date.\n\nThanking You,\n{username}\n")
    elif(recipient=="_chiefwarden@nitc.ac.in"):
        message=(f"Subject: Requesting extension of curfew timings\n\nSir,\nI would like to request an extension on the curfew timings on {date} as we are conducting an event\n  on the given date.\nI hope you can grant the extension as the students are going to be outside due to the event.\n\nThanking you\n{username}\n")
    elif(recipient=="anuj.haval@gmail.com"):
        message=(f"Subject: Requesting permission to {subject} on {date} in {venue}\n\nSir,\nI hope this email finds you well. We have planned to {subject} on {date} at the {venue} and are requesting you to grant us the permission to do so.\n I would be grateful if you could grant us the permission to host the event on the specific date and\n venue and if not possible would like to discuss the possibility of conducting it at a different venue or\n on a different date.\n\nThanking You,\n{username}\n")
    
    return message






if __name__== "__main__":
    app.debug=True
    app.run()

    