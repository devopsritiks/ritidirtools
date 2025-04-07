import click
from .core import create_structure, modify_files, delete_directory, quake_structure, rollback_state
from .utils import load_yaml, preview_structure, preview_modifications
from . import __version__

@click.group()
@click.version_option(__version__, "--version", "-v")  # Add version option
def cli():
    """ritidirtools: A CLI tool to manage directories and files with YAML."""
    pass

@cli.command()
@click.option('-fd', '--full-directory', type=click.Path(exists=True), help="YAML file for full directory creation")
@click.option('--force', is_flag=True, help="Override existing directories/files")
@click.option('--dry-run', is_flag=True, help="Simulate without applying changes")
@click.option('--verbose', is_flag=True, help="Print detailed output")
def create(full_directory, force, dry_run, verbose):
    """Create directories and files from a YAML file."""
    data = load_yaml(full_directory)
    if dry_run or verbose:
        click.echo(f"Previewing creation from {full_directory}:")
        preview_structure(data)
    if not dry_run:
        create_structure(data, force, verbose)
        click.echo(f"Created structure from {full_directory}")

@cli.command()
@click.option('-f', '--files', type=click.Path(exists=True), help="YAML file for file modifications")
@click.option('--force', is_flag=True, help="Override without prompting")
@click.option('--dry-run', is_flag=True, help="Simulate without applying changes")
@click.option('--verbose', is_flag=True, help="Print detailed output")
def modify(files, force, dry_run, verbose):
    """Modify files based on a YAML file."""
    data = load_yaml(files)
    if dry_run or verbose:
        click.echo(f"Previewing modifications from {files}:")
        preview_modifications(data)
    if not dry_run:
        modify_files(data, force, verbose)
        click.echo(f"Modified files from {files}")

@cli.command()
@click.argument('directory', type=click.Path(exists=True))
@click.option('--force', is_flag=True, help="Override without prompting")
def destroy(directory, force):
    """Delete a directory and its contents."""
    if force or click.confirm(f"Delete {directory} and all contents?"):
        delete_directory(directory)
        click.echo(f"Deleted {directory}")

@cli.command()
@click.argument('yaml_file', type=click.Path(exists=True))
def prep(yaml_file):
    """Preview changes and validate YAML syntax."""
    data = load_yaml(yaml_file)
    click.echo(f"Valid YAML: {yaml_file}")
    if 'directories' in data:
        preview_structure(data)
    elif 'files' in data:
        preview_modifications(data)

@cli.command()
@click.argument('yaml_file', type=click.Path(exists=True))
@click.option('--force', is_flag=True, help="Override without prompting")
@click.option('--dry-run', is_flag=True, help="Simulate without applying changes")
def quake(yaml_file, force, dry_run):
    """Delete all directory content specified in YAML."""
    data = load_yaml(yaml_file)
    if dry_run:
        click.echo(f"Previewing deletion from {yaml_file}:")
        preview_structure(data)
    elif force or click.confirm("Delete all specified directories and files?"):
        quake_structure(data)
        click.echo(f"Deleted structure from {yaml_file}")

@cli.command()
def rollback():
    """Revert to the previous state from .ritidir.bcic."""
    if rollback_state():
        click.echo("Rolled back to previous state")
    else:
        click.echo("No backup state found in .ritidir.bcic")
