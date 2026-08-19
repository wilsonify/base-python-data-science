#!/usr/bin/env python3
"""
Setup script for Data Scratch Library REST API.
"""

from setuptools import setup, find_packages

setup(
    name="data-scratch-rest-api",
    version="1.0.0",
    description="REST API for Data Scratch Library",
    author="Data Science Team",
    packages=find_packages(),
    install_requires=[
        "Flask==3.1.3",
        "Flask-CORS==6.0.0",
        "marshmallow==3.26.2",
        "dsl>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest==9.0.3",
            "pytest-flask==1.2.0",
        ]
    },
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "data-scratch-api=run:main",
        ],
    },
)
