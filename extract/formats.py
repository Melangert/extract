def detect_format(path: str) -> str | None:
    with open(path, "rb") as f:
        header = f.read(16)

    if header[:2] == b"PK":
        return "zip"

    if header[:2] == b"\x1f\x8b" and (path.endswith("tar.gz") or path.endswith(".tgz")):
        return "tar.gz"
    
    if header[:2] == b"\x1f\x8b":
        return "gz"
    
    if header[:3] == b"BZh" and (path.endswith(".tar.bz2") or path.endswith(".tbz2")):
        return "tar.bz2"

    if header[:6] == b"\xfd7zXZ\x00" and (path.endswith(".tar.xz") or path.endswith(".txz")):
        return "tar.xz" 

    if header[:3] == b"BZh":
        return "bz2"

    if header[:6] == b"\xfd7zXZ\x00":
        return "xz"

    if path.endswith(".tar"):
        return "tar"
    
    return None


def list_supported_extensions() -> list:
    return [".zip", ".tar", ".tar.gz", ".tgz", ".tar.bz2", ".tbz2", 
            ".tar.xz", ".txz", ".gz", ".bz2", ".xz"]