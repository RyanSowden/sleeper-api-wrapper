import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="sleeper.py",
    version="1.1.3",
    description="A Python API wrapper for Sleeper Fantasy Football.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/rswdn/sleeper.py",
    author="Ryan Sowden",
    author_email="rsowden@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["sleeper_wrapper"],
    include_package_data=True,
    install_requires=["requests==2.22.0", "pytest==4.6.2"]
)
