# ritidirtools

A command-line tool to manage directories and files using YAML configurations.

## Overview

`ritidirtools` is a powerful utility designed to streamline directory and file management through simple YAML templates. Whether you're setting up consistent project structures, managing configuration files, or automating repetitive tasks, this tool makes it easy to create, modify, and delete directories and files with precision.

### Key Features
- **Create**: Build directories and files from YAML templates
- **Modify**: Update existing files and directories
- **Delete**: Remove specified directories and files
- **Preview**: See changes before applying them
- **Rollback**: Revert to a previous state if needed

## Installation

### Prerequisites
- Ubuntu 24.04 or later
- Python 3 (installed automatically with the package)

### Installation via APT
Follow these steps to install `ritidirtools` using the APT package manager:

1. Add the PPA to your system:
   ```bash
   sudo add-apt-repository ppa:devopsritiks/ritidirtools
   ```
2. Update the package list:
   ```bash
   sudo apt update
   ```
3. Install the tool:
   ```bash
   sudo apt install ritidirtools -y
   ```

### Manual Installation
If you prefer a manual installation, download the Debian package from the link below:

- [Download ritidirtools_0.1.0-4_all.deb](https://launchpad.net/~devopsritiks/+archive/ubuntu/ritidirtools/+build/30617485/+files/ritidirtools_0.1.0-4_all.deb)

Then, install it with these commands:
```bash
sudo dpkg -i ritidirtools_0.1.0-4_all.deb
sudo apt install -f  # To resolve any dependencies
```

## Usage

Once installed, you can use the `ritidir` command directly from your terminal. Below are the core commands and examples to get you started.

### Basic Commands
- **Create directories and files**:
  ```bash
  ritidir create -fd your_template.yaml
  ```
  Use the `-fd` flag to create both files and directories as defined in the YAML.

- **Preview changes**:
  ```bash
  ritidir prep your_template.yaml
  ```
  This lets you review the planned changes without applying them.

- **Modify existing structures**:
  ```bash
  ritidir modify -f modification_template.yaml
  ```
  Adjust files or directories based on a new YAML template.

- **Delete directories and files**:
  ```bash
  ritidir destroy directory_path
  ```
  Remove the specified path and its contents.

- **Rollback changes**:
  ```bash
  ritidir rollback
  ```
  Revert to the previous state if something goes wrong.

### Example YAML Configuration
Here’s a sample YAML file (`project_template.yaml`) to create a basic project structure:

```yaml
directories:
  - path: my_project
    subdirectories:
      - path: src
        files:
          - main.py
      - path: tests
        files:
          - test_main.py
    files:
      - README.md
```

Run this command to apply it:
```bash
ritidir create -fd project_template.yaml
```

This will generate the following structure:
```
my_project/
├── README.md
├── src/
│   └── main.py
└── tests/
    └── test_main.py
```

## Getting Help

- To see all available commands and options:
  ```bash
  ritidir --help
  ```

- For details on a specific command:
  ```bash
  ritidir [command] --help
  ```

- For additional support or to report issues, visit the [GitHub repository](https://github.com/devopsritiks/ritidirtools).

---

With `ritidirtools`, managing your file system is as simple as writing a YAML file. Get started today and simplify your workflow!
