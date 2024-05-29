import boto3
import sys

glacier = boto3.client('glacier')

def create_vault(vault_name):
    response = glacier.create_vault(vaultName=vault_name)
    print(f"Vault {vault_name} created successfully.")
    return response

def list_vaults():
    response = glacier.list_vaults()
    vaults = response['VaultList']
    for vault in vaults:
        print(f"Vault Name: {vault['VaultName']}, Creation Date: {vault['CreationDate']}")
    return vaults

def upload_archive(vault_name, file_path):
    with open(file_path, 'rb') as file:
        response = glacier.upload_archive(
            vaultName=vault_name,
            body=file
        )
    print(f"Archive uploaded to {vault_name} successfully. Archive ID: {response['archiveId']}")
    return response

def initiate_archive_retrieval(vault_name, archive_id, description=""):
    response = glacier.initiate_job(
        vaultName=vault_name,
        jobParameters={
            'Type': 'archive-retrieval',
            'ArchiveId': archive_id,
            'Description': description
        }
    )
    print(f"Archive retrieval initiated. Job ID: {response['jobId']}")
    return response

def main():
    if len(sys.argv) < 2:
        print("Usage: script.py <command> [<args>]")
        print("Commands: create-vault, list-vaults, upload-archive, retrieve-archive")
        return

    command = sys.argv[1]

    if command == "create-vault":
        if len(sys.argv) != 3:
            print("Usage: script.py create-vault <vault_name>")
            return
        vault_name = sys.argv[2]
        create_vault(vault_name)

    elif command == "list-vaults":
        list_vaults()

    elif command == "upload-archive":
        if len(sys.argv) != 4:
            print("Usage: script.py upload-archive <vault_name> <file_path>")
            return
        vault_name = sys.argv[2]
        file_path = sys.argv[3]
        upload_archive(vault_name, file_path)

    elif command == "retrieve-archive":
        if len(sys.argv) != 5:
            print("Usage: script.py retrieve-archive <vault_name> <archive_id> <description>")
            return
        vault_name = sys.argv[2]
        archive_id = sys.argv[3]
        description = sys.argv[4]
        initiate_archive_retrieval(vault_name, archive_id, description)

    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
