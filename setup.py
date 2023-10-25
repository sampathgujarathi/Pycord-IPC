import ast
import re

import setuptools
from pathlib import Path


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf8")

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('discord/ext/ipc/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(f.read().decode('utf-8')).group(1)))

setuptools.setup(
    author="Sampath",
    python_requires=">=3.8.0",
    license="MIT License",
    author_email="gujarathisampath@gmail.com",
    long_description_content_type="text/markdown",
    url="https://github.com/sampathgujarathi/pycord-ipc",
    description="A high-performance inter-process communication library designed to work with the latest version of py-cord",
    packages=[
        "discord.ext.ipc"
    ],
    project_urls={
        "Source": "https://github.com/sampathgujarathi/pycord-ipc"
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Communications",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["Pycord-IPC","ipc", "python", "py-cord"],
    long_description=long_description,
    install_requires=["websockets>=10.4","py-cord >= 2.4.1"],
    name="Pycord-IPC",
    version=version,
)