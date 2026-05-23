
# extract

Universal archive extraction tool for Linux.

![extract --list](screenshot.png)

## Installation

```bash
git clone https://github.com/yourname/extract
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

## Supported formats

- .zip, .jar, .apk
- .tar, .tar.gz, .tgz
- .tar.bz2, .tbz2
- .tar.xz, .txz
- .gz, .bz2, .xz

## Credits

Built with guidance from Claude (Anthropic) as a learning project. 
All code written by me
