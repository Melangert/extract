import zipfile
import tarfile
import gzip
import bz2
import lzma 
import os
from pathlib import Path
from .formats import detect_format

def _decompresss_single(src:str, dest: str, open_fn, suffix: str, verbose: bool) -> None:
    out_path =os.path.join(dest, os.path.basename(src).replace(suffix, ""))
    os.makedirs(dest, exist_ok=True)
    if verbose:
        print(f"  extracting {os.path.basename(out_path)}")
    with open_fn(src, "rb") as f_in:
        with open(out_path, "wb") as f_out:
            f_out.write(f_in.read())




def  extract_file(src: str, dest: str,  verbose: bool = False) -> None:
    fmt = detect_format(src)

    if  fmt is None: 
        raise ValueError (f"Unsupported archive format for file: {src}")
    
    if fmt == "zip":
        with zipfile.ZipFile(src, "r") as zf:
            for memeber in zf.infolist():
                if verbose:
                    print(f"Extracting {memeber.filename}")
                zf.extract(memeber, dest)

    
    if fmt == "tar.gz": 
        with tarfile.open(src, "r:gz") as tf:
            for member in tf.getmembers():
                if verbose:
                    print(f"Extracting {member.name}")
                tf.extract(member, dest, filter='data')
    
       
    if fmt == "gz":
        _decompresss_single(src, dest, gzip.open, ".gz", verbose)

    if fmt == "bz2":
        _decompresss_single(src, dest, bz2.open, ".bz2", verbose)

    if fmt == "xz":
        _decompresss_single(src, dest, lzma.open, ".xz", verbose)

    if fmt == "tar.bz2":
        with tarfile.open(src, "r:bz2") as tf:
            for member in tf.getmembers():
                if verbose:
                    print(f"Extracting {member.name}")
                tf.extract(member, dest, filter='data')
    
    if fmt == "tar.xz":
        with tarfile.open(src, "r:xz") as tf:
            for member in tf.getmembers():
                if verbose:
                    print(f"Extracting {member.name}")
                tf.extract(member, dest, filter='data')

