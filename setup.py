from setuptools import find_packages, setup

setup(
    name="blog",
    version=verstr,
    description='blog',
    url='https://github.com/benhoff/vexbot',
    license='GPL3',
    author='Ben Hoff',
    author_email='beohoff@gmail.com',
    packages= find_packages(), # exclude=['docs', 'tests']
    install_requires=[
        'pelican',
        'ghp-import',
        ],

    extras_require={
        'dev': ['flake8', 'twine'],
    }
)