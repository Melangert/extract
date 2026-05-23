import zipfile
import pytest
from pathlib import Path
from extract.archive import extract_file



def test_extract_zip(tmp_path):
    # create a sample zip file 
    archive_path = tmp_path / "text.zip"
    with zipfile.ZipFile(archive_path, "w") as zf:
        zf.writestr("hello.txt", "hello world")
    
    #extract it
    out = tmp_path / "output"
    extract_file(str(archive_path), str(out))

    # check if file is there
    assert (out / "hello.txt").exists()
    assert (out / "hello.txt").read_text() == "hello world"

    def test_extract_zip_nested(tmp_path):
        # create a nested zip file
        archive = tmp_path / "test.zip"
        with zipfile.ZipFile(archive, "w") as zf:
            zf.writestr("subdir/nested.txt", "nested content")

        out = tmp_path / "out"
        extract_file(str(archive), str(out))

        assert (out / "subdir" / "nested.txt").exists()
        assert (out / "subdir" / "nested.txt").read_text() == "nested content"

def test_test_extract_zip_unsoppurted_format(tmp_path):
    # create a fake file with unsupported format
    fake = tmp_path / "fake.xyz"
    fake.write_bytes(b"\x00" * 16)


    with pytest.raises(ValueError):
        extract_file(str(fake), str(tmp_path / "out"))