from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from ics import Calendar
app = Flask(__name__)


@app.route("/")
def main():
    return "<p>test</p>"

@app.route("/upload_ics", methods=['GET', 'POST'])
def upload_ics():
    event_list = []
    if request.method == 'POST':
        f = request.form['file']
        if f: 
            contents = requests.get(f)
            calendar = Calendar(contents.text)
            event_list = list(calendar.events)
            event_times = [(event.begin,event.end) for event in event_list]
            
    
    return render_template('upload_ics.html', event_list=event_list)

if __name__ == '__main__':
    app.run()
