<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://seeklogo.com/images/C/cinema-logo-53411DFFE5-seeklogo.com.png" alt="Project logo"></a>
</p>

<h3 align="center">Cinema</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/likecodingloveproblems/cinema-management-sample-app/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/likecodingloveproblems/cinema-management-sample-app/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Few lines describing your project.
    <br> 
</p>

# 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Database configuration](#db_config)
- [Running local server](#local_server)
- [Usage](#usage)
- [Deployment](#deployment)
- [Acknowledgments](#acknowledgement)

# 🧐 About <a name = "about"></a>

This is a simple example of a Cinema application.
Customer can see different room's movies and reserve a seat.

# 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

## Prerequisites

You need to have Python 3.8.10 or later installed on your machine.
and git installed.

```
Python >= 3.8.10
```

## Configuration

## pipenv
- Install pipenv : `pip install pipenv`
- Create a virtual environment : `pipenv --three`
- Install project dependencies : `pipenv install`
- Activate virtual environment : `pipenv shell`

## python venv module
python -m venv venv-name
Activate the virtual environment : `source venv-name/bin/activate`
Install project dependencies : `pip install -r requirements.txt`

# Database configuration <a name = "db_config"></a>
As this is a simple example, we will use SQLite3 database.
But if you want to use other database, you can change the database configuration in `settings.py` file.
`Postgresql` is referred by django community.

# 🔧 Running local server <a name = "local_server"></a>
- Create database tables : `python manage.py migrate`
- Start server : `python manage.py runserver`
- Check it in browser : `http://localhost:8000`

## Coding style
Cinema is linted and formatted by `pylint` and `autopep8`

## VSCode

1. Install `pep8`, `autopep8`, `pylint`, `pylint-django` using `pip`. You
   probably installed them while installing all project dependencies using
   `pip install -r requirements.txt`
2. Add this lines to `settings.json` file in vscode (<kbd>Ctrl</kbd> + <kbd>,</kbd>
   or File > Preferences > Settings):

```
{
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.pycodestyleEnabled": true,
    "python.formatting.provider": "autopep8",
    "python.linting.pylintArgs": [
        "--load-plugins=pylint_django"
    ],
    "python.formatting.autopep8Args": [
        "--max-line-length",
        "80",
        "--aggressive",
        "--experimental"
    ],
    "editor.formatOnSave": true,
    "editor.formatOnSaveMode": "modifications",
}
```

# 🎈 Usage <a name="usage"></a>

There is huge amount of required analyzes to make this project work.
We need to many user stories to extract and implement them.
At this point, there isn't any usage of this project.

# 🚀 Deployment <a name = "deployment"></a>

For deployment it's recommended to use docker.
a Dockerfile is provided in `root` directory.
but it's seriously recommended to modify it for production environment.
Please refer to this [Tutorial](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/) for more information.

# 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Thanks to precise feedback of @Pargev
