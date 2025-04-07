import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def preview_structure(data):
    for dir_entry in data.get('directories', []):
        print(f"Would create directory: {dir_entry['path']}")
        for file_name in dir_entry.get('files', []):
            print(f"  Would create file: {file_name}")
        for subdir in dir_entry.get('subdirectories', []):
            preview_subdir(subdir, f"  {dir_entry['path']}/")

def preview_subdir(subdir, prefix):
    print(f"{prefix}Would create directory: {subdir['path']}")
    for file_name in subdir.get('files', []):
        print(f"{prefix}  Would create file: {file_name}")
    for nested in subdir.get('subdirectories', []):
        preview_subdir(nested, f"{prefix}  ")

def preview_modifications(data):
    for file_mod in data.get('files', []):
        print(f"Would modify: {file_mod['path']}")
        if 'appendFile' in file_mod:
            for append in file_mod['appendFile']:
                if 'deleteLines' in append:
                    print(f"  Delete lines {append['deleteLines']}")
                if 'lineNumber' in append:
                    print(f"  Append at line {append['lineNumber']}: {append.get('pasteContent', '').strip()}")
        if 'reWrite' in file_mod:
            print(f"  Rewrite with: {file_mod['reWrite'].get('newContent', '[empty]')}")
