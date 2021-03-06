import os

from setuptools import setup, find_packages


def read(fname):
    """
    Helper to read README
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()


ASSETS = "buzzword/static"
DOCS = "docs"

assets = [os.path.join(ASSETS, i) for i in os.listdir(ASSETS)]

docs = [os.path.join(DOCS, i) for i in os.listdir(DOCS)]

setup(
    name="buzzword",
    version="1.4.0",  # bump2version will edit this automatically!
    description="Web-app for corpus linguistics",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Danny McDonald",
    include_package_data=True,
    zip_safe=False,
    scripts=["bin/buzzword", "bin/create"],
    packages=find_packages(),
    author_email="daniel.mcdonald@uzh.ch",
    license="MIT",
    keywords=["nlp", "linguistics", "corpora"],
    install_requires=[
        "buzz>=4.0.0",
        "django-guardian==2.2.0",
        "martor==1.4.9",
        "pyocr==0.7.2",
        "whitenoise==4.1.4",
        "tesseract==0.1.3",
        "dash-core-components==1.9.0",
        "dash-daq==0.5.0",
        "dash-html-components==1.0.3",
        "dash-renderer==1.3.0",
        "dash-table==4.7.0",
        "dash==1.10.0",
        "django-plotly-dash==1.3.1",
        "django==3.0.7",
        "dpd_static_support==0.0.5",
        "flask==1.1.2",
        "python-dotenv==0.10.3",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
