# pyaug - our practice project
This directory is structured the same way a typical Python package would be. It is also the primary place you will be making your own changes as part of our git drills. 

So far, the package is very simple. We have:
- another directory, also named pyaug.
    - This is where the codes lives
- a directory called tests.
    - This directory will house scripts used to test that our code works correctly
- a Python file called setup.py.
    - This script contains the commands needed to install pyaug.
    - If you want to test it out using your clone (local copy), then navigate to this folder in your standard OS terminal or command prompt and run
        ```python 
	$ python setup.py install
	$ python -c "import pyaug; pyaug.welcome()"
	```
    - If that worked you should see the pyaug welcome message displayed
- collaborators.md
    - This isn't something you would normally see, but for this project, we'll use it to keep track of folks who have contributed.
- README.md
    - That's the markdown file that contains all this stuff you're reading now!
