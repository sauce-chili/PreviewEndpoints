from dataclasses import dataclass
from pathlib import Path

from domain.repository import PhotoRepository


@dataclass(frozen=True)
class FtpDatabaseParam:
    image_buffer_folder_path: Path
    image_buffer_folder_remote_path: Path


class FTPPhotoRepository(PhotoRepository):
    ...
