import codecs
import os
import sys
from setuptools import setup

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

def readme():
    return read("README.md")

VERSION = "0.0.2"

setup(name='apilimiter',
    version=VERSION,
    description='View limiter for django',
    long_description=readme().strip(),
    author='mymusise',
    author_email='mymusise1@gmail.com',
    url='https://github.com/mymusise/django-view-limiter',
    license='MIT',
    packages=['apilimiter'],
    install_requires=[],
    keywords='apilimiter api limiter django view',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',        
        'Programming Language :: Python :: 2.7',        
        'Topic :: Software Development'
    ],
    include_package_data=True,
    zip_safe=False,
)