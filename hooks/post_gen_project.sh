#!/bin/bash

set -ex

poetry add \
-D setuptools \
-D twine \
-D wheel \
-D flake8 \
-D mypy \
-D pytest \
-D pytest-cov \
-D codecov \
-D mkdocs \
-D mkdocs-material \
-D mkautodoc \
-D pygments \
-D pymdown-extensions \
-D rich \
-D python-lsp-server \
-D mypy-ls \
-D pyls-flake8

{% if cookiecutter.create_github_repo in ["public", "private"] %}
git init
git add .
git commit -m "Initial commit."
gh config set prompt disabled
gh repo create {{ cookiecutter.package_name }} --{{ cookiecutter.create_github_repo }} --confirm
git push origin main
{% endif %}

{% if cookiecutter.include_sublime_project == "no" %}
rm "{{ cookiecutter.package_name }}.sublime-project"
{% endif %}