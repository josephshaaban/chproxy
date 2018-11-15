from setuptools import setup

setup(
    name='chproxy',
    version='0.1',
    description='A simple proxy applier that applies proxy system-wide, on linux OS.',
    url='http://github.com/josephshaaban/chproxy',
    author='Joseph Shaaban',
    author_email='josephsha3ban@gmail.com',
    license='MIT',
    packages=['chproxy'],
    install_requires=[
        'getopt',
        'subprocess'
    ],
    zip_safe=False
)