<h1 id="the-blog-project">The Blog Project</h1>
<p>This is a BLOG project. Just like other blog it has diffrent features like Login-Logout, New Post, GitHub(Jump Link), Linkedin(Jump Link), About, Draft, Comment. It also uses mySQL DB.</p>
<h1 id="prerequisties">Prerequisties</h1>
<p>Software you would need.</p>
<ol>
<li>Python Version :- 3.8.3</li>
<li>DJango Version :- 3.0</li>
<li>PIP Version :- Any</li>
<li>mySQL Client :- mysqlclient-1.4.6-cp38-cp38-win32</li>
<li>XAMPP :- Any</li>
</ol>
<blockquote>
<p>You can use diffrent version, but you need to see compatibility.<br>
<mark>For Eg</mark> : mysqlclient-1.4.6-cp38-cp38-win32 is only compatible with python 32bit and will therefore give error if you are using 64bit python.</p>
</blockquote>
<h1 id="installing">Installing</h1>
<ol>
<li>Python
<ul>
<li>Go To :  <a href="https://www.python.org/">Official Pyhton Site</a></li>
<li>Scroll down a little and you’ll see  <strong>DOWNLOAD.</strong></li>
<li>It will automatically download latest version of python.</li>
<li>After download is complete click on .exe file</li>
<li>Keep pressing next and python will be installed.(By default it will be in C drive)</li>
</ul>
</li>
<li>PIP
<ul>
<li>Enter cmd
<ul>
<li><code>python get-pip.py</code></li>
</ul>
</li>
</ul>
</li>
<li>DJango
<ul>
<li>Enter cmd
<ul>
<li>For MAC/Linux User :- <code>python -m pip install</code></li>
<li>For Windows User :- <code>py -m pip install Django</code></li>
</ul>
</li>
<li>For a specific Version just put that version in last of the cmd.</li>
</ul>
</li>
<li>mySQL Client
<ul>
<li>Enter Cmd
<ul>
<li><code>pip install mysqlclient</code></li>
</ul>
</li>
</ul>
</li>
<li>XAMPP
<ul>
<li>Go To :  <a href="https://www.apachefriends.org/index.html">Official XAMPP Site</a></li>
<li>Click On download w.r.t your OS system</li>
<li>Open .exe file and complete process</li>
</ul>
</li>
</ol>
<p>Python-DJango Compatibility Table</p>

<table>
<thead>
<tr>
<th>DJango Version</th>
<th>Python Version</th>
</tr>
</thead>
<tbody>
<tr>
<td>1.11</td>
<td>2.7, 3.4, 3.5, 3.6, 3.7 (added in 1.11.17)</td>
</tr>
<tr>
<td>2.0</td>
<td>3.4, 3.5, 3.6, 3.7</td>
</tr>
<tr>
<td>2.1</td>
<td>3.5, 3.6, 3.7</td>
</tr>
<tr>
<td>2.2</td>
<td>3.5, 3.6, 3.7, 3.8 (added in 2.2.8)</td>
</tr>
<tr>
<td>3.0</td>
<td>3.6, 3.7, 3.8</td>
</tr>
</tbody>
</table><h3 id="errors">Errors</h3>
<p>If above cmd for mysql client doesn’t works then you cam download raw files and install them manually from <a href="https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient">Here</a></p>
<p>After Downloading go to your directory where you have downloaded raw file and enter cmd</p>
<pre><code>pip install mysqlclient-1.4.6-cp38-cp38-win32
</code></pre>
<blockquote>
<p>cp38 file is for python 3.8.x</p>
</blockquote>
<h2 id="features">Features</h2>
<ol>
<li>Login-Logout</li>
<li>New Post</li>
<li>Comments</li>
<li>Draft</li>
<li>mySQL Db</li>
</ol>
<h2 id="deployment">Deployment</h2>
<p>Deployment of SQL Db is simple you need to just change a few lines of code.<br>
First open your XAMPP Control Panel and start apache and mysql servers.</p>
<p><img src="https://devtuts.butlerccwebdev.net/testserver/xampp-control-panel.png" alt="enter image description here"></p>
<p>Now in <a href="http://settings.py">settings.py</a> file of your Django Project</p>
<pre><code>DATABASES = {

	'default': {

	'ENGINE': 'django.db.backends.mysql',

	'NAME': 'project name',

	'USER': 'root',

	'PASSWORD': '',

	'HOST': 'localhost',

	'PORT': 'whatever is set in your XAMPP app',

	} }
</code></pre>
<p>Run code <code>pyhton manage.py migrate</code><br>
Now you are all set to go.</p>
<h2 id="built-with">Built With</h2>
<ol>
<li>DJango</li>
<li>Python</li>
<li>CSS</li>
</ol>
<h2 id="author">Author</h2>
<p>Prakhar</p>
<h2 id="license">License</h2>
<p>Free To Use</p>
<h2 id="acknowledgments">Acknowledgments</h2>
<ul>
<li>StackoverFlow</li>
<li>DJango Documentaion</li>
<li>MySQL Documentation</li>
</ul>
