import os
import yaml
import shutil
from datetime import datetime

CIC_FILE = ".ritidir.cic"
BCIC_FILE = ".ritidir.bcic"

def load_state(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return yaml.safe_load(f) or {}
    return {}

def save_state(file_path, state):
    with open(file_path, 'w') as f:
        yaml.safe_dump(state, f)

def update_states(new_state):
    current = load_state(CIC_FILE)
    if current:
        save_state(BCIC_FILE, current)
    save_state(CIC_FILE, {"state": new_state, "timestamp": datetime.utcnow().isoformat() + "Z"})

def create_structure(data, force=False, verbose=False):
    for dir_entry in data.get('directories', []):
        create_directory(dir_entry, "", force, verbose)
    update_states(data)

def create_directory(dir_entry, base_path, force, verbose):
    dir_path = os.path.join(base_path, dir_entry['path'])
    if os.path.exists(dir_path) and force:
        shutil.rmtree(dir_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        if verbose:
            print(f"Created directory: {dir_path}")
    for file_name in dir_entry.get('files', []):
        file_path = os.path.join(dir_path, file_name)
        if not os.path.exists(file_path) or force:
            open(file_path, 'a').close()
            if verbose:
                print(f"Created file: {file_path}")
    for subdir in dir_entry.get('subdirectories', []):
        create_directory(subdir, dir_path, force, verbose)

def modify_files(data, force=False, verbose=False):
    current_state = load_state(CIC_FILE).get('state', {})
    for file_mod in data.get('files', []):
        path = file_mod['path']
        if not os.path.exists(path) and force:
            open(path, 'a').close()
        if 'appendFile' in file_mod:
            with open(path, 'r') as f:
                lines = f.readlines()
            for append in file_mod['appendFile']:
                if 'deleteLines' in append:
                    x, y = map(int, append['deleteLines'].split('_'))
                    lines = lines[:x-1] + lines[y:]
                if 'lineNumber' in append and 'pasteContent' in append:
                    lines.insert(append['lineNumber']-1, append['pasteContent'])
            with open(path, 'w') as f:
                f.writelines(lines)
            if verbose:
                print(f"Appended to {path}")
        if 'reWrite' in file_mod:
            with open(path, 'w') as f:
                f.write(file_mod['reWrite'].get('newContent', ''))
            if verbose:
                print(f"Rewrote {path}")
    update_states(current_state)  # TODO: Merge with modifications

def delete_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    update_states({})

def quake_structure(data):
    for dir_entry in data.get('directories', []):
        dir_path = dir_entry['path']
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
    update_states({})

def rollback_state():
    backup = load_state(BCIC_FILE)
    if not backup:
        return False
    current = load_state(CIC_FILE)
    save_state(CIC_FILE, backup)
    save_state(BCIC_FILE, current)
    return True
