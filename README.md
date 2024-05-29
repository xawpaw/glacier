# Glacier
Utilizing the AWS SDK for Python, to interact with Amazon Glacier. This script includes basic functionalities like creating a vault, listing vaults, uploading an archive, and retrieving an archive.

## Usage

Save the script as glacier_script.py and run it using the command line. Here are some examples of how to use the script:

Create a vault:

```bash
python glacier_script.py create-vault my-vault
```

List vaults:

```bash
python glacier_script.py list-vaults
```

Upload an archive:

```bash
python glacier_script.py upload-archive my-vault path/to/your/file
```

Retrieve an archive:

```
bash
python glacier_script.py retrieve-archive my-vault archive-id description
```
