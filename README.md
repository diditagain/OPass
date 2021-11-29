# OPass Password Generator and Clerk

## About the Project

This is a portfolio project. OPass data is not encrypted. Use it at you own risk.

Opass is a simple password manager that has built in functions such as:

1. Save Login infos to a json file named data
2. Generate password
3. Copy generated password to clipboard

## Built With

Opass has been built with Python and built-in python modules except tkinter and pyclip.

[You can see the pypi page of pyperclip here](https://pypi.org/project/pyperclip/)

## How to use

Before registering any website or app, you can run OPass and generate a secure password and save you login info on your system.

### Generate

Generate button generates a secure password and copies it to clipboard

### Search

Search button looks for existing info depending on website entry value

For example, if you write amazon.com to website space and click on search button, OPass will look for previus logs for amazon.com login infos.

### Add

Easy enough, adds given infos to a json file.

-------
# Delete the existing json file before using. That's there for test purposes