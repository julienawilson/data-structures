"""The setup for Mailroom distribution."""

from setuptools import setup

setup(
    name='data_structures',
    description='Implementation of Data Structures.',
    version=0.1,
    author='Patrick Saunders, Julien Wilson',
    author_email='patrick.a.n.saunders@gmail.com, julienawilson@gmail.com',
    license='MIT',
    package_dir={'': 'src'},
    py_modules=['deque', 'dll'],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
)
