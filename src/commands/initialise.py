from pathlib import Path
from .exceptions import WorkingDirNotExists


class Initialise():
    def __init__(self, working_dir: str, create_wd: bool):
        self._working_dir = Path(working_dir)
        self._create_wd = create_wd

    def run(self):
        """Runs project setup"""
        if not self._check_wd():
            self._handle_create_wd()

        self._setup_templates()

    def _handle_create_wd(self):
        """Creates the working directory for the project if specified"""
        if self._create_wd:
            self._working_dir.mkdir(parents=True)
        else:
            raise WorkingDirNotExists("Working directory does not exist")

    def _check_wd(self):
        """Checks if the working directory exists"""
        return self._working_dir.exists()

    def _setup_templates(self):
        """Makes the folders for the project"""
        path = Path(__file__).parent.parent / "init_templates"
        templates = [p for p in path.rglob("*")]

        for item in templates:
            if item.is_dir():
                (self._working_dir / item.relative_to(path)).mkdir(exist_ok=True)
            else:
                (self._working_dir / item.relative_to(path)).write_bytes((path / item).read_bytes())
