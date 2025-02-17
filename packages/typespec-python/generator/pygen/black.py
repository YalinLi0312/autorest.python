# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from pathlib import Path
import os
from typing import Any, Dict
import black
from black.report import NothingChanged

from . import Plugin
from .utils import parse_args

_LOGGER = logging.getLogger("blib2to3")

_BLACK_MODE = black.Mode()  # pyright: ignore [reportPrivateImportUsage]
_BLACK_MODE.line_length = 120


class BlackScriptPlugin(Plugin):  # pylint: disable=abstract-method
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        output_folder = self.options.get("output_folder", str(self.output_folder))
        if output_folder.startswith("file:"):
            output_folder = output_folder[5:]
        if os.name == "nt" and output_folder.startswith("///"):
            output_folder = output_folder[3:]
        self.output_folder = Path(output_folder)

    def process(self) -> bool:
        # apply format_file on every .py file in the output folder
        list(
            map(
                self.format_file,
                [
                    Path(f)
                    for f in self.list_file()
                    if all(
                        item not in f
                        for item in (
                            "__pycache__",
                            "node_modules",
                            ".tox",
                            ".mypy_cache",
                        )
                    )
                    and Path(f).suffix == ".py"
                ],
            )
        )
        return True

    def format_file(self, file: Path) -> None:
        try:
            file_content = self.read_file(file)
            file_content = black.format_file_contents(file_content, fast=True, mode=_BLACK_MODE)
        except NothingChanged:
            pass
        except:  # pylint: disable=bare-except
            _LOGGER.error("Error: failed to format %s", file)
            raise
        else:
            self.write_file(file, file_content)


if __name__ == "__main__":
    # CADL pipeline will call this
    args, unknown_args = parse_args(need_cadl_file=False)
    BlackScriptPlugin(output_folder=args.output_folder, **unknown_args).process()
