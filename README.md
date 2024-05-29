# Glacier
Utilizing the AWS SDK for Python to interact with Amazon Glacier, this script includes basic functionalities such as creating a vault, listing vaults, uploading an archive, and retrieving an archive.

## Prerequisites

- Python 3.x
- Boto3 library
- AWS credentials configured (using `aws configure` or by setting environment variables)

## Installing Boto3
If you haven't installed Boto3 yet, you can install it using pip:
```bash
pip install boto3
```

## Usage

Save the script as `glacier_script.py` and run it using the command line. Here are some examples of how to use the script:

## Create a vault
```bash
python glacier_script.py create-vault my-vault
```

## List vaults
```bash
python glacier_script.py list-vaults
```

## Upload an archive
```bash
python glacier_script.py upload-archive my-vault path/to/your/file
```

## Retrieve an archive
```bash
python glacier_script.py retrieve-archive my-vault archive-id description
```

Replace `my-vault`, `path/to/your/file`, `archive-id`, and `description` with appropriate values. You can save them as environment variables, for example exporting them:

```bash
export MY_VAULT="$"
```

## Copyright

Mad Max (c) 2024

