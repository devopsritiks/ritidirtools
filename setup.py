import os  # Added this line
from setuptools import setup, find_packages

setup(
    name="ritidirtools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.0",    # For CLI
        "pyyaml>=5.4",   # For YAML parsing
    ],
    entry_points={
        "console_scripts": [
            "ritidir = ritidirtools.cli:cli",  # Maps 'ritidir' command to cli()
        ],
    },
    author="Ritik Sharma",
    author_email="devopsritiks@gmail.com",
    description="A CLI tool to manage directories and files with YAML",
    long_description=open("README.md").read() if os.path.exists("README.md") else "See docs/README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/devopsritiks/ritidirtools",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    extras_require={
        "test": ["pytest", "pytest-mock"],
    },
)
