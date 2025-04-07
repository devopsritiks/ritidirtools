import pytest
import os
from ritidirtools.core import modify_files

@pytest.fixture
def tmp_dir(tmp_path):
    return tmp_path

def test_modify_append_file(tmp_dir, mocker):
    """Test appending content to a file."""
    yaml_data = {
        "files": [
            {
                "path": os.path.join(tmp_dir, "test.txt"),
                "appendFile": [
                    {"lineNumber": 1, "pasteContent": "Line 1\n"},
                    {"lineNumber": 2, "pasteContent": "Line 2\n"}
                ]
            }
        ]
    }
    mocker.patch("ritidirtools.core.update_states")
    
    # Create an empty file
    open(os.path.join(tmp_dir, "test.txt"), "w").close()
    
    modify_files(yaml_data, force=True, verbose=False)
    
    with open(os.path.join(tmp_dir, "test.txt"), "r") as f:
        content = f.readlines()
    assert content == ["Line 1\n", "Line 2\n"]

def test_modify_rewrite_file(tmp_dir, mocker):
    """Test rewriting a file's content."""
    yaml_data = {
        "files": [
            {
                "path": os.path.join(tmp_dir, "test.txt"),
                "reWrite": {"newContent": "New content\n"}
            }
        ]
    }
    mocker.patch("ritidirtools.core.update_states")
    
    # Create a file with initial content
    with open(os.path.join(tmp_dir, "test.txt"), "w") as f:
        f.write("Old content\n")
    
    modify_files(yaml_data, force=True, verbose=False)
    
    with open(os.path.join(tmp_dir, "test.txt"), "r") as f:
        content = f.read()
    assert content == "New content\n"
