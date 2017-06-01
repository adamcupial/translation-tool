# this python file uses the following encoding utf-8

from setuptools import setup

setup(
    name='translation_tool',
    packages=['translation_tool'],
    include_package_data=True,
    install_requires=[
        'click==6.7',
        'Flask==0.12.2',
        'Flask-SQLAlchemy==2.2',
        'itsdangerous==0.24',
        'Jinja2==2.9.6',
        'MarkupSafe==1.0',
        'SQLAlchemy==1.1.10',
        'Werkzeug==0.12.2',
    ]
)
