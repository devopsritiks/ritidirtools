import pytest
import os
from ritidirtools.core import create_structure

@pytest.fixture
def tmp_dir(tmp_path):
    """Fixture to provide a temporary directory."""
    return tmp_path

def test_create_structure_basic(tmp_dir, mocker):
    """Test creating a basic directory structure."""
    yaml_data = {
        "directories": [
            {
                "path": "test_dir",
                "files": ["file1.txt", "file2.txt"],
                "subdirectories": [
                    {"path": "sub_dir", "files": ["sub_file.txt"]}
                ]
            }
        ]
    }
    mocker.patch("ritidirtools.core.update_states")
    os.chdir(tmp_dir)  # Change to tmp_dir for relative paths
    create_structure(yaml_data, force=False, verbose=False)
    
    assert (tmp_dir / "test_dir").exists()
    assert (tmp_dir / "test_dir" / "file1.txt").exists()
    assert (tmp_dir / "test_dir" / "file2.txt").exists()
    assert (tmp_dir / "test_dir" / "sub_dir").exists()
    assert (tmp_dir / "test_dir" / "sub_dir" / "sub_file.txt").exists()

def test_create_structure_force(tmp_dir, mocker):
    """Test creating with --force overwrites existing structure."""
    yaml_data = {
        "directories": [
            {"path": "test_dir", "files": ["file1.txt"]}
        ]
    }
    mocker.patch("ritidirtools.core.update_states")
    
    # Create initial structure in tmp_dir
    test_dir = tmp_dir / "test_dir"
    test_dir.mkdir()
    old_file = test_dir / "old_file.txt"
    old_file.write_text("old content")
    
    os.chdir(tmp_dir)  # Change to tmp_dir for relative paths
    create_structure(yaml_data, force=True, verbose=False)
    
    assert (test_dir / "file1.txt").exists()
    assert not old_file.exists()
