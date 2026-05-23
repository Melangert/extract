import zipfile
import tarfile
import gzip
import bz2
import lzma 
import os
from pathlib import Path
from .formats import detect_format

def _decompresss_single(src:str, dest: str, open_fn, suffix: str) -> None:
    out_path =os.path.join(dest, os.path.basename(src).replace(suffix, ""))
    os.makedirs(dest, exist_ok=True)
    with open_fn(src, "rb") as f_in:
        with open(out_path, "wb") as f_out:
            f_out.write(f_in.read())




def  extract_file(src: str, dest: str) -> None:
    fmt = detect_format(src)

    if  fmt is None: 
        raise ValueError (f"Unsupported archive format for file: {src}")
    
    if fmt == "zip":
        with zipfile.ZipFile(src, "r") as zf:
            zf.extractall(dest)

    
    if fmt == "tar.gz": 
        with tarfile.open(src, "r:gz") as tf:
            tf.extractall(dest)
    
       
    if fmt == "gz":
        _decompresss_single(src, dest, gzip.open, ".gz")

    if fmt == "bz2":
        _decompresss_single(src, dest, bz2.open, ".bz2")

    if fmt == "xz":
        _decompresss_single(src, dest, lzma.open, ".xz")

    if fmt == "tar.bz2":
        with tarfile.open(src, "r:bz2") as tf:
            tf.extractall(dest)
    
    if fmt == "tar.xz:":
        with tarfile.open(src, "r:xz") as tf:
            tf.extractall(dest)

            