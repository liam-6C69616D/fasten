from pathlib import Path
from .exceptions import WorkingDirNotExists


class Initialise():
    def __init__(self, working_dir: str, create_wd: bool):
        self._working_dir = Path(working_dir)
        self._create_wd = create_wd

    def run(self):
        if not self._check_wd():
            self._handle_create_wd()

        self._setup_folders()
        self._setup_files()

    def _handle_create_wd(self):
        if self._create_wd:
            self._working_dir.mkdir(parents=True)
        else:
            raise WorkingDirNotExists("Working directory does not exist")

    def _check_wd(self):
        return self._working_dir.exists()

    def _setup_folders(self):
        folders = ["routes", "services", "repos"]  # TODO: extract to a config file
        for folder in folders:
            (self._working_dir / folder).mkdir(exist_ok=True)

    def _setup_files(self):
        pass
