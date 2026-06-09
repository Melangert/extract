import zipfile
import tarfile
import gzip
import bz2
import lzma
import os
import subprocess
from .formats import detect_format

def _decompress_single(src: str, dest: str, open_fn, suffix: str, verbose: bool) -> None:
    out_path = os.path.join(dest, os.path.basename(src).replace(suffix, ""))
    os.makedirs(dest, exist_ok=True)
    if verbose:
        print(f"  extracting {os.path.basename(out_path)}")
    with open_fn(src, "rb") as f_in:
        with open(out_path, "wb") as f_out:
            f_out.write(f_in.read())

def extract_file(src: str, dest: str, verbose: bool = False):
    fmt = detect_format(src)
    if fmt is None:
        raise ValueError(f"Unsupported file format: {src}")

    os.makedirs(dest, exist_ok=True)

    if fmt == "zip":
        with zipfile.ZipFile(src, "r") as zf:
            for member in zf.infolist():
                if verbose:
                    print(f"  extracting {member.filename}")
                zf.extract(member, dest)
    elif fmt == "tar.gz":
        with tarfile.open(src, "r:gz") as tf:
            for member in tf.getmembers():
                if verbose:
                    print(f"  extracting {member.name}")
                tf.extract(member, dest, filter='data')
    elif fmt == "tar.bz2":
        with tarfile.open(src, "r:bz2") as tf:
            for member in tf.getmembers():
                if verbose:
                    print(f"  extracting {member.name}")
                tf.extract(member, dest, filter='data')
    elif fmt == "tar.xz":
        with tarfile.open(src, "r:xz") as tf:
            for member in tf.getmembers():
                if verbose:
                    print(f"  extracting {member.name}")
                tf.extract(member, dest, filter='data')
    elif fmt == "tar":
        with tarfile.open(src, "r:") as tf:
            for member in tf.getmembers():
                if verbose:
                    print(f"  extracting {member.name}")
                tf.extract(member, dest, filter='data')
    elif fmt == "gz":
        _decompress_single(src, dest, gzip.open, ".gz", verbose)
    elif fmt == "bz2":
        _decompress_single(src, dest, bz2.open, ".bz2", verbose)
    elif fmt == "xz":
        _decompress_single(src, dest, lzma.open, ".xz", verbose)

    elif fmt == "tar.zst":
        result = subprocess.run(
            ["tar", "--zstd", "-xf", os.path.abspath(src)],
            cwd=dest, capture_output=True, text=True
        )
        if result.returncode != 0:
            raise RuntimeError(f"Failed to extract tar.zst: {result.stderr}")
        if verbose:
            print(f"  extracted {src} to {dest}")
    elif fmt == "zst":
        try:
            import zstandard as zstd
            out_path = os.path.join(dest, os.path.basename(src).replace(".zst", ""))
            os.makedirs(dest, exist_ok=True)
            with open(src, "rb") as f_in:
                dctx = zstd.ZstdDecompressor()
                with open(out_path, "wb") as f_out:
                    dctx.copy_stream(f_in, f_out)
            if verbose:
                print(f"  extracting {os.path.basename(out_path)}")
        except ImportError:
            raise RuntimeError("zst support requires the 'zstandard' package: pip install zstandard")
    elif fmt == "rar":
        try:
            import rarfile
            with rarfile.RarFile(src) as rf:
                for member in rf.infolist():
                    if verbose:
                        print(f"  extracting {member.filename}")
                    rf.extract(member, dest)
        except ImportError:
            raise RuntimeError("RAR support requires the 'rarfile' package: pip install rarfile")
    elif fmt == "deb":
        result = subprocess.run(["ar", "x", os.path.abspath(src)], cwd=dest, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Failed to extract deb: {result.stderr}")
        if verbose:
            print(f"  extracted deb contents to {dest}")
    elif fmt == "rpm":
        abs_src = os.path.abspath(src)
        result = subprocess.run(
            f"rpm2cpio '{abs_src}' | cpio -idm",
            shell=True, cwd=dest, capture_output=True, text=True
        )
        if result.returncode != 0:
            raise RuntimeError(f"Failed to extract rpm: {result.stderr}")
        if verbose:
            print(f"  extracted rpm contents to {dest}")