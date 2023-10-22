# This is a sample Flask BluePrint
# https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy
from app import create_app


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    create_app().run(host='127.0.0.1', port=5000, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
