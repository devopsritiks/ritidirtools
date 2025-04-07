# ritidirtools

A command-line tool to create, modify, and destroy directories and files using YAML configurations.

## Overview

`ritidirtools` simplifies directory and file management by allowing you to define structures and modifications in YAML files. It supports commands like `create`, `modify`, `quake`, and `rollback`, with features like state tracking and dry-run previews.

## Installation

Install via PyPI:
```bash
pip install ritidirtools

(APT support planned: sudo apt install ritidirtools -y)
Usage
Create a Directory Structure

ritidir create -fd app1_directory.yaml --force

Creates directories and files defined in app1_directory.yaml, overwriting existing ones if --force is used.
Modify Files
bash
ritidir modify -f modified_files.yaml --verbose

Applies changes (append or rewrite) to files as specified in modified_files.yaml.
Preview Changes
bash
ritidir prep example.yaml

Shows what would happen without making changes.

Delete Structure

bash
ritidir quake app1_directory.yaml --force

Deletes all directories and files listed in app1_directory.yaml.
Rollback
bash
ritidir rollback

Reverts to the previous state stored in .ritidir.bcic.

See the examples/ directory for sample YAML files.

Features

    Create full directory structures with empty files
    Modify files by appending or rewriting content
    Delete directories or entire structures
    Preview changes with prep
    Rollback to previous state
    Flags: --force, --dry-run, --verbose

Contributing

See  for guidelines on how to contribute.

License

This project is licensed under the MIT License - see  for details.
Contact

    Author: Ritik Sharma
    Email: devopsritiks@gmail.com
    GitHub: https://github.com/devopsritiks/ritidirtools
