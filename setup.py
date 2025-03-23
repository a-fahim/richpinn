'''
richpinn
├── richpinn
│   ├── data_struct.py
│   ├── __init__.py
│   └── internals.py
├── README
├── requirements.txt
├── scripts
│   ├── cool
│   └── skype
└── setup.py
'''

from setuptools import setup

setup(
   name='richpinn',
   version='1.0',
   description='A Useful Module to Study Application of Richardson Extrapolation in Physics Informed Neural Networks',
   long_description=open('README.md').read(),
   license="MIT",
   author='Ali Fahimi',
   author_email='a.fahimi@gmail.com',
   url="https://github.com/a-fahimi/richpinn",
   packages=['richpinn'],  #same as name
   install_requires=['numpy',], #external packages as dependencies
   scripts=[
            'scripts/cool',
            'scripts/skype',
           ]
)

'''
# To install the package locally:
$ python setup.py build && python setup.py install

# To upload the package to test.pypi.org:
# prereq: wheel (pip install wheel)
$ python setup.py sdist bdist_wheel
# then using twine for uploading either to test.pypi.org or pypi.org:
$ twine upload --repository testpypi dist/*
username: ***
password: ***

# To upload the package to pypi.org:
$ twine upload dist/*
username: ***
password: ***
'''


