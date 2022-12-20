from app import create_app

"""
You can also use `flask run` in the terminal, 
Flask will automatically look for the package called `app`

Make sure you are running from the virtual environment
(venv) $ flask run
"""

if __name__ == "__main__":
    create_app().run()
