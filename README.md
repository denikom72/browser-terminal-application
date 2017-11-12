Browser-Terminal-Application is a pretty simple browser with a terminal on the bottom. The programm is written python2, so it is necessary to have a python2-interperter, if it is possible python2.7.

python-(re)installation on linux-debian:

1.Check out, is there any python-interpreter and if this is the case, which version of it:

`sudo su - `

`python -V`

2.find out the path of the python bins, see is there any other version of it and set the link on the right one

`ls -ld $(which python)`

`cd "PATH TO PYTHON-BINS, probably /usr/bin/"`

`ls | sort | grep -i "pytho*"`

3.if there is not a python2.7-interpreter, make an installation

`apt-get install python2.7 -y`

or donwload the interpreter with "curl" into this directory and don't forget to set the x-rights

4.set a link to the right version

`ln -s python python2.7`

Small how-to-video: installation of the right python-version and a [small demo of the browser-terminal-application](http://www.green-homepages.de/#brow_term) 


## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/denikom72/browser-terminal-application/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/denikom72/browser-terminal-application/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
