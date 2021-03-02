#!/usr/bin/env python

import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='physiogradient',
    version="0.0.1-alpha.1",
    author='Hao-Ting Wang',
    author_email='htwangtw@gmail.com',
    description='Exploring physiology related FC gradient',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/htwangtw/physiogradient",
    packages=setuptools.find_packages(),
    license="Apache License 2.0",
    python_requires=">=3.6",
    test_require=["pytest"],
    project_urls={
        "Documentation": "TBA",
        "Bug Reports": "https://github.com/htwangtw/physiogradient/issues",
        "Source": "https://github.com/htwangtw/physiogradient",
    },
)