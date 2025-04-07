import pytest
import os
from ritidirtools.core import quake_structure

@pytest.fixture
def tmp_dir(tmp_path):
    return tmp_path

def test_quake_structure(tmp_dir, mocker):
    """Test deleting a directory structure."""
    yaml_data = {
        "directories": [
            {
                "path": os.path.join(tmp_dir, "test_dir"),
                "files": ["file1.txt"],
                               "subdirectories": [
                    {"path": "sub_dir", "files": ["sub_file.txt"]}
                ]
            }
        ]
    }
    mocker.patch("ritidirtools.core.update_states")
    
    # Create the structure
    os.makedirs(os.path.join(tmp_dir, "test_dir", "sub_dir"))
    open(os.path.join(tmp_dir, "test_dir", "file1.txt"), "w").close()
    open(os.path.join(tmp_dir, "test_dir", "sub_dir", "sub_file.txt"), "w").close()
    
    quake_structure(yaml_data)
    
    assert not os.path.exists(os.path.join(tmp_dir, "test_dir"))
