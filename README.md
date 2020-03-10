Simple browser with a terminal on the bottom. Python 2.7. Use "virtualenv" to install the suitable python-version if possible. Otherwise use apt- or rpm:

1.Check python-interpreter-version:

`sudo su - `

`python -V`

2.If necessary, set a new link to the right python-version

`ls -ld $(which python)`

`cd "PATH TO PYTHON-BINS, probably /usr/bin/"`

`ls | sort | grep -i "pytho*"`

3.if there isn't a python2.7-interpreter, run an installation

`apt-get install python2.7 -y`

or download the interpreter with "curl" into the "bin"-directory and set it as "executeable"

4.set a link to the right version

`ln -s python python2.7`

