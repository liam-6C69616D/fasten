from pathlib import Path
from .exceptions import FieldException
import re


class Generate():
    def __init__(self, working_dir: Path, name: str, fields: list[str]):
        self.name = name
        self.fields = self.__parse_fields(fields)
        self.__working_dir = working_dir

    def __parse_fields(self, fields: list[str]) -> list[list[str]]:
        parsed_fields = []
        valid_regex = r'(^[a-zA-Z_][a-zA-Z0-9_]*):([a-zA-Z0-9_\[\]<>.,:\s]+)$'

        for field in fields:
            if not (match := re.match(valid_regex, field)):
                raise FieldException(f"Field {field} is not formatted correctly, refer to the guides for syntax")

            field_name, field_type = (x.strip() for x in match.groups())
            field_type = self.__normalize_type_syntax(field_type)
            parsed_fields.append([field_name, field_type])

        return parsed_fields

    def __normalize_type_syntax(self, type_str: str):
        """Convert list.str or list::str to list[str]"""
        # Replace . with [, and :: with [
        normalized = type_str.replace('::', '[').replace('.', '[')

        # Count opening brackets and add closing ones
        open_count = normalized.count('[')
        normalized += ']' * open_count

        return normalized

    def __append_to_file(self, file_path: Path, content: str) -> None:
        """Append content to an existing Python file."""
        if not file_path.exists():
            raise FileNotFoundError(f"File {file_path} does not exist.")

        existing = file_path.read_text()

        # Add spacing before appended content
        if not existing.endswith("\n\n"):
            existing += "\n\n"

        file_path.write_text(existing + content)

    def run(self):
        self._generate_types()

    def _generate_types(self):
        file_content = f"class {self.name}(BaseModel):\n"

        for field_name, field_type in self.fields:
            content = f"\t{field_name}: {field_type}\n"
            file_content += content

        self.__append_to_file(self.__working_dir / "utils/types.py", file_content)

    def _generate_repo(self):
        pass

    def _generate_service(self):
        pass

    def _generate_route(self):
        pass
