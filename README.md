Simple browser with a terminal on the bottom. Python 2.7. You can use "virtualenv" to install the suitable python-version or 
to install with apt- or rpm the suitable python version, here an example:

1.Check out, is there any python-interpreter and if this is the case, which version of it:

`sudo su - `

`python -V`

2.find out the path of the python bins, see is there any other version of it and set the link on the right one

`ls -ld $(which python)`

`cd "PATH TO PYTHON-BINS, probably /usr/bin/"`

`ls | sort | grep -i "pytho*"`

3.if there isn't a python2.7-interpreter, make an installation

`apt-get install python2.7 -y`

or donwload the interpreter with "curl" into this directory and don't forget to set the x-rights

4.set a link to the right version

`ln -s python python2.7`

