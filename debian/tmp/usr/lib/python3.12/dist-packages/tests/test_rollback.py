import pytest
import os
from ritidirtools.core import save_state, load_state, rollback_state, CIC_FILE, BCIC_FILE

@pytest.fixture
def tmp_dir(tmp_path):
    return tmp_path

def test_rollback_success(tmp_dir, mocker):
    """Test rolling back to a previous state."""
    os.chdir(tmp_dir)  # Change to temp directory for state files
    
    current_state = {"state": {"directories": [{"path": "new_dir"}]}}
    backup_state = {"state": {"directories": [{"path": "old_dir"}]}}
    
    save_state(CIC_FILE, current_state)
    save_state(BCIC_FILE, backup_state)
    
    assert rollback_state() is True
    
    new_current = load_state(CIC_FILE)
    new_backup = load_state(BCIC_FILE)
    
    assert new_current["state"] == backup_state["state"]
    assert new_backup["state"] == current_state["state"]

def test_rollback_no_backup(tmp_dir):
    """Test rollback when no backup exists."""
    os.chdir(tmp_dir)
    
    save_state(CIC_FILE, {"state": {"directories": [{"path": "dir"}]}})
    os.remove(BCIC_FILE) if os.path.exists(BCIC_FILE) else None
    
    assert rollback_state() is False
