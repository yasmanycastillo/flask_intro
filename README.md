# flask_intro
App to be used in Flask Intro talk.

# Step 1 - Create your virtual enviroment
If you don't have install yet, following  <a href="http://virtualenvwrapper.readthedocs.io/en/latest/install.html">this.</a>

<code>mkvirtualenv flask_intro</code>
<code>workon flask_intro </code>
Or "path_to_your_virtual_environment/bin/actiuvate"


# Step 2 - Installing dependencies
Use Python Pip to install our app dependencies.
<code>pip install -r requirements/dev.txt</code>

# Step 3 - Installing main components
This command install npm (NodeJs Package Manager) and Bower.
If nodejs doesn't install, click <a href="https://nodejs.org/es/">here!</a>
<code>npm install -g bower</code>

Now go to the app dir and run
<code>bower init</code>
<code>bower install -S jquery bootstrap font-awesome</code>

# Step 4 - Enjoit!!!
<code>python run.py</code>