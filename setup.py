from setuptools import setup

install_requires = [
    'requests',
]

tests_require = [
    'coverage',
    'nose',
    'flake8',
]

setup(
    name='juju-plugin',
    version='0.0.1',
    description='A plugin to install and manage juju plugins',
    install_requires=install_requires,
    author='Marco Ceppi',
    author_email='marco@ceppi.net',
    url="https://jujuplugins.com",
    packages=['jujuplugin'],
    entry_points={
        'console_scripts': [
            'juju-plugin=jujuplugin.cli:main',
        ]
    }
)
