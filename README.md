# python-template

This is a [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) template for generating Python packages.

## Usage

- Install dependencies

```shell
brew install pipx
pipx install cookiecutter
brew install gh
```

- Run cookiecutter
```shell
cookiecutter gh:jordaneremieff/python-template

name []: My Test Project
description []: A generated project.
author []: Jordan Eremieff
author_email []: jordan@eremieff.com
package_name [my_test_project]:
package_version [0.0.1]:
python_version [3.8]:
matrix_versions [3.7, 3.8, 3.9]:
github_username [jordaneremieff]:
github_repo [jordaneremieff/my_test_project]:
Select include_sublime_project:
1 - yes
2 - no
Choose from 1, 2 [1]: 1
Select create_github_repo:
1 - none
2 - public
3 - private
Choose from 1, 2, 3 [1]: 3
```