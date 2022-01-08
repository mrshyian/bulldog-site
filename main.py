from flask import Flask, request, render_template, redirect, session, url_for
import data_manager
import util


app = Flask(__name__)
app.secret_key = '9e33e7321f59a3fdc954607f32c9da3f6b74ec0bc36828e0555de5a37987727a'

@app.route('/', methods=['GET', 'POST'])
@app.route('/main', methods=['GET', 'POST'])
def home_page():
    return render_template('home_page.html')


@app.route('/cennik', methods=['GET', 'POST'])
def cennik():
    return render_template('cennik.html')


@app.route('/kontakt', methods=['GET', 'POST'])
def kontakt():
    return render_template('kontakt.html')


@app.route('/o_nas', methods=['GET', 'POST'])
def o_nas():
    return render_template('o_nas.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )


