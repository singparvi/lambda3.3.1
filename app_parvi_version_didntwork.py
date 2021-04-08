from flask import Flask, render_template
import json
# sqlalhemy object relation mapping system
from data_model import DB, User, Tweet


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////db.sqlite3'
    DB.init_app(app)  # initialize app

    # a view function or route
    # someone comes to our landing page this will help route the traffic. Another page will have another.
    @app.route("/")  # decorator, wrapper this runs first and then runs in the end.
    def landing():
        DB.drop_app()
        DB.create_all()  # create table
        app_user = User(id=1, name='app_user')
        DB.session.add(app_user)
        DB.session.commit()
        # args = {'title': 'Landing', 'body': 'landing body'}
        # return render_template('base.html', **args)
        with open(
                'templates/landing.json') as f:  # keep only in memory for the following command, keep it in ram for just a moment
            args = json.load(f)  # loading as a dictionary and then unpack it
        # return render_template('base.html', title='Landing', body = 'landing body')
        return render_template('base.html', **args)

    @app.route("/products")  # decorator, wrapper this runs first and then runs in the end.
    def products():
        new_tweet = Tweet(id=1, text='tweet', user_id=1)
        DB.session.add(new_tweet)
        DB.session.commit()
        return render_template('base.html', title='Products', body='product body')

    return app


if __name__ == "__main__":
    create_app().run(host='0.0.0.0', port=8888)
