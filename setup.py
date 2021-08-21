"""
Setup for lookatme.contrib.notes
"""


from setuptools import setup, find_namespace_packages
import os


setup(
    name="lookatme.contrib.notes",
    version="0.0.0",
    description="Simplistic speaker notes",
    author="",
    author_email="",
    python_requires=">=3.5",
    packages=find_namespace_packages(include=["lookatme.*"]),
)
