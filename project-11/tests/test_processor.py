import os
import json
from src.data_processor.main import generate_report

def test_generate_report(tmpdir):
    # tmpdir is a built-in pytest fixture for temporary directories
    out_dir = str(tmpdir.mkdir("data"))
    filepath = generate_report(out_dir)
    
    assert os.path.exists(filepath)
    with open(filepath, "r") as f:
        data = json.load(f)
        
    assert data["status"] == "success"
    assert "metrics" in data
    assert data["metrics"]["users"] == 150
