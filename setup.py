from setuptools import setup
setup(
    name = 'robot',
    version = '0.1.0',
    packages = ['robot'],
    entry_points = {
        'console_scripts': [
            'robot = robot.__main__:main'
        ]
    })