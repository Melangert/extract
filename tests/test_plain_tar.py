import tarfile
import pytest
from extract.archive import extract_file

def test_extract_tar(tmp_path):
    archive = tmp_path / "test.tar"
    dummy = tmp_path / "hello.txt"
    dummy.write_text("plain tar content")
    with tarfile.open(archive, "w") as tf:
        tf.add(dummy, arcname="hello.txt")


    out = tmp_path / "out"
    extract_file(str(archive), str(out))

    assert (out / "hello.txt").read_text() == "plain tar content"

def test_extract_tar_unsupported_format(tmp_path):
    # create a file that is not a valid tar file
    bad_file = tmp_path / "bad.tar.gz"
    bad_file.write_bytes(b"\xDE\xAD\xBE\xEF" * 4)

    # should raise error since it's not a valid tar.gz file
    # will return None, or the extraction will fail with an error
    with pytest.raises(ValueError, match="Unsupported file format"):
        extract_file(str(bad_file), str(tmp_path / "out"))