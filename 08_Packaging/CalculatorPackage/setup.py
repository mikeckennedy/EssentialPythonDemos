from setuptools import setup
# from distutils.core import setup

setup(
    name='calculator',
    version='0.9.0',
    packages=['calculator', 'calculator.finance'],  # , 'calculator.finance'],
    url='http://blog.michaelckennedy.net',
    license='Creative Commons Attributions 3.0',  # open('license.txt').read(),
    author='Michael Kennedy',
    author_email='mikeckennedy@gmail.con',
    description='This is an awesome calculator package.',
    install_requires=[
        'requests'
    ],
)
