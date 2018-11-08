#!/usr/bin/env python3

import os
from pathlib import Path
import subprocess
from pkg_resources import parse_version

class Repo:
    def __init__(self, name, versions):
        self.name = name
        self.versions = versions
        self.max_version = self.max_version()

    def max_version(self):
        parsed_versions = [
            parse_version(version)
            for version in self.versions if version
            ]
        if parsed_versions:
            return max(parsed_versions)
        else:
            return "master"

here = Path(os.getcwd())

repos = [
    Repo(
        dir.name,
        subprocess.check_output(["git", "-C", str(dir), "tag"]).decode().splitlines()
    )
    for dir in here.iterdir() if dir.is_dir() and (dir / ".git").exists()
]

for repo in repos:
    print("{}: {}".format(repo.name, repo.max_version))
