# coding: utf-8
import logging
import os
import shutil
from pathlib import Path

from Cython.Build import cythonize
from setuptools import find_packages, setup, Extension
from setuptools.command.build_ext import build_ext as build_ext_orig
from setuptools.command.build_py import build_py as build_py_orig

assert "__call__" in dir(cythonize)
NAME = "command_line_tools"
VERSION = "1.0.0"

extensions = [
    Extension('command_line_tools.*', ['command_line_tools/**/*.py']),
]


class build_py(build_py_orig):
    def build_packages(self):
        """
        Because build_packages doesn't do anything, no .py files will be collected.
        dist will include only cythonized extensions.
        """
        pass


class build_ext(build_ext_orig):
    """
    python modules need a __init__.py and a __main__.py 
    even if they are empty
    """

    def run(self):
        build_ext_orig.run(self)
        build_dir = Path(self.build_lib)
        root_dir = Path(__file__).parent
        target_dir = build_dir if not self.inplace else root_dir
        logging.debug(f"build_dir = {build_dir}")
        logging.debug(f"root_dir = {root_dir}")
        logging.debug(f"target_dir = {target_dir}")
        logging.warning(f'moving command_line_tools/__init__.py from {root_dir} to {target_dir}')
        try:
            self.copy_file(Path('command_line_tools/__init__.py'), root_dir, target_dir)
        except:
            logging.warning(f'could not move command_line_tools/__init__.py from {root_dir} to {target_dir}')

        logging.warning(f'moving command_line_tools/__main__.py from {root_dir} to {target_dir}')
        try:
            self.copy_file(Path('command_line_tools/__main__.py'), root_dir, target_dir)
        except:
            logging.warning(f'could not move command_line_tools/__main__.py from {root_dir} to {target_dir}')

    def copy_file(self, path, source_dir, destination_dir):
        if not (source_dir / path).exists():
            return
        dest = str(destination_dir / path)
        dest_dir, _ = os.path.split(dest)
        os.makedirs(dest_dir, exist_ok=True)
        shutil.copyfile(str(source_dir / path), str(destination_dir / path))


setup(
    name=NAME,
    version=VERSION,
    description="Command Line Tools",
    author_email="apiteam@default.io",
    url="",
    keywords=["datascience", "python"],
    packages=find_packages(),
    package_data={'': []},
    include_package_data=True,
    entry_points={'console_scripts': ['command_line_tools=command_line_tools.__main__:main']},
    long_description="""
    Supplemental material (code examples, exercises, etc.) 
    is available at https://github.com/joelgrus/data-science-from-scratch.
    """,
    ext_modules=cythonize(extensions, compiler_directives={'language_level': 3}),
    cmdclass={'build_py': build_py, 'build_ext': build_ext},
)
