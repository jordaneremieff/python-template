from setuptools import find_packages, setup


def get_long_description():
    return open("README.md", "r", encoding="utf8").read()


setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.package_version }}",
    packages=find_packages(),
    license="MIT",
    url="https://github.com/{{ cookiecutter.github_repo }}",
    description="{{ cookiecutter.description }}",
    long_description=get_long_description(),
    python_requires=">={{ cookiecutter.python_version }}",
    package_data={"{{ cookiecutter.package_name }}": ["py.typed"]},
    long_description_content_type="text/markdown",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.author_email }}",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: {{ cookiecutter.python_version }}",
    ],
)
