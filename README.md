# flask_intro
App to be used in Flask Intro talk.

# Step 1 - Create your virtual enviroment
If you don't have install yet, following  <a href="http://virtualenvwrapper.readthedocs.io/en/latest/install.html">this.</a>

    mkvirtualenv flask_intro
    workon flask_intro
Or "path_to_your_virtual_environment/bin/activate"

# Step 2 - Installing dependencies
Use Python Pip to install our app dependencies.

    pip install -r requirements/dev.txt

# Step 3 - Installing main components
This command install npm (NodeJs Package Manager) and Bower.
If nodejs doesn't install, click <a href="https://nodejs.org/es/">here!</a>

    npm install -g bower

Now go to the app dir and run:

    bower init
    bower install -S jquery bootstrap font-awesome

# Step 4 - Enjoit!!!

    python run.py