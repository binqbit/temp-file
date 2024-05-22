# Temp Files

This tool is designed to temporarily upload a file and access it on another system.

## Usage
- Upload a file
```shell
tmpf file.txt
```

- This command uploads the file. After executing this command, the curl command to download the file will be copied to your clipboard.

- Download a file
```shell
curl -o .\file.txt https://tmpfiles.org/dl/0000000/file.txt
```

Use this command to download the file to another system.
