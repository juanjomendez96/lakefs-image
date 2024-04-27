from lakefs.client import Client
from dotenv import load_dotenv
import os
import lakefs
from lakefs_spec import LakeFSFileSystem

load_dotenv("configs/.env")


class LakeFSClass:
    def __init__(self) -> None:
        self.client = None
        self.file_sys = None

    def connect_lakefs(self):
        self.clt = Client(
            host=os.getenv("LAKEFS_HOST"),
            username=os.getenv("LAKEFS_INSTALLATION_ACCESS_KEY_ID"),
            password=os.getenv("LAKEFS_INSTALLATION_SECRET_ACCESS_KEY"),
        )

        self.fs = LakeFSFileSystem()

    def print_repositories(self):
        for repo in lakefs.repositories():
            print(repo)

    def create_branch(self, repository, branch, source_branch):
        try:
            branch1 = (
                lakefs.repository(repository)
                .branch(branch)
                .create(source_reference_id=source_branch)
            )

            print("experiment1 ref:", branch1.get_commit().id)

        except:
            print(
                f"Unable to create branch {branch} from {source_branch} in repository {repository}"
            )

    def print_branches(self, repository):
        for branch in lakefs.repository(repository).branches():
            print(branch)

    def print_directory(self, lakefs_dir):
        print(self.fs.ls(lakefs_dir))

    def upload_file(self, local_path, lakefs_path):
        try:
            self.fs.put_file(local_path, lakefs_path)
            print(f"File {local_path} uploaded")

        except:
            print(f"Unable to upload the file {local_path}")

    def upload_directory(self, local_dir, lakfefs_dir):
        try:
            self.fs.put(local_dir, lakfefs_dir, recursive=True)
            print(f"File {local_dir} uploaded")

        except:
            print(f"Unable to upload the file {local_dir}")

    def delete_file(self, lakefs_file):
        try:
            self.fs.rm_file(lakefs_file)
            print(f"File {lakefs_file} removed")

        except:
            print(f"Unable to remove file {lakefs_file}")

    def delete_folder(self, lakefs_folder):
        try:
            self.fs.rm(lakefs_folder, recursive=True)

        except:
            print(f"Unable to remove folder {lakefs_folder}")
