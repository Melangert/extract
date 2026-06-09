# Extract
An archive extraction tool for linux that supports many file types.
I built this because i didnt like having to use many different ways of extracting when extracting a different file type like tar in terminal
![extract --list](screenshot.png)
## Requirements 
-Python 
-Shell
-Any linux distro
## What it does 
```
zip    -> unzip file.zip
tar.gz -> tar -xzf file.tar.gz
rar    -> unrar x file.rar
extract file.zip
extract file.tar.gz
extract file.rar
```
## How to install
```bash
git clone https://github.com/Melangert/extract
cd extract
sudo ln -s $(pwd)/extract.sh /usr/local/bin/extract
```
if you installed from the release cd into the install directory and do the following commands
```
tar -xzf extract.tar.gz
cd extract
sudo ln -s $(pwd)/extract.sh /usr/local/bin/extract
```
## Commands
```bash
# Extract a file
extract archive.zip
# Extract to a specific directory
extract archive.tar.gz -o ~/Desktop
# Detect format without extracting
extract --detect archive.zip
# List supported formats
extract --list
# Show help
extract --help
```
## currently supported formats
-.zip
-.tar, .tar.gz, .tgz
-.tar.bz2, .tbz2
-.tar.xz, .txz
-.tar.zst, .tzst
-.gz, .bz2, .xz, .zst
-.rar (requires: pip install rarfile)
-.deb
-.rpm (requires: rpm2cpio)
```

