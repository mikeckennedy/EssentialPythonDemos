#from distutils.core import setup
from setuptools import setup, find_packages
import calculator

requires = [
    'requests'
]

setup(
    name='calculator',
    version=calculator.version,
    packages=['calculator', 'calculator.graphing'],
    url='http://whitehouse.gov',
    license='MIT',
    author='Jeff Stevens',
    install_requires=requires,
    tests_require=requires,
    author_email='j@steven.com',
    description='Some Desc.'
)
