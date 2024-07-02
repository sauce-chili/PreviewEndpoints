from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import Protocol


@dataclass
class ParamFTP:
    host: str
    username: str
    password: str


class ServerFTP(Protocol):
    def file_exist(self, path_ftp_file: Path):
        ...

    def download_file(self, path_ftp_file: Path, path_local_file: Path):
        ...

    def upload_file(self, path_local_file: Path, path_ftp_file: Path):
        ...

    def update_file(self, path_to_ftp_server: Path, source: BytesIO):
        ...

    def remove_file(self, path_to_ftp_server: Path):
        ...

    def get_url_to_file(self, ftp_file_path: Path):
        ...


class AsyncServerFTP(Protocol):
    async def file_exist(self, path_ftp_file: Path):
        ...

    async def download_file(self, path_ftp_file: Path, path_local_file: Path):
        ...

    async def upload_file(self, path_local_file: Path, path_ftp_file: Path):
        ...

    async def update_file(self, path_to_ftp_server: Path, source: BytesIO):
        ...

    async def remove_file(self, path_to_ftp_server: Path):
        ...

    async def get_url_to_file(self, ftp_file_path: Path):
        ...
