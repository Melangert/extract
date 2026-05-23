import tarfile
import pytest
from pathlib import Path
from extract.archive import extract_file

def test_extract_tar_gz(tmp_path):
    #create  a sample tar.gz file
    archive = tmp_path / "test.tar.gz"
    
    #write a real file to the temp dir first
    dummy_file  = tmp_path / "hello.txt"
    dummy_file.write_text("tarball content")

    #pack it into a tar.gz
    with tarfile.open(archive, "w:gz") as tf:
        tf.add(dummy_file, arcname="hello.txt")


    #Test your extraction function
    out = tmp_path / "out"
    extract_file(str(archive), str(out))

    #4 Verify extraction worked
    assert (out / "hello.txt").exists()
    assert (out / "hello.txt").read_text() == "tarball content"

    