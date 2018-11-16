from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="chproxy",
    version="0.1",
    author="Joseph Shaaban",
    author_email="josephsha3ban@gmail.com",
    description="A simple proxy applier that applies proxy system-wide, on linux OS.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/josephshaaban/chproxy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
    ],
)