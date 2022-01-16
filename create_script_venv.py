#!/usr/bin/env python3

import encodings
import os.path
import subprocess
import venv

from pathlib import Path
from types import SimpleNamespace
from typing import Final

PROJECT_NAME: Final[str] = 'inf6200-h2022-benoit-dubreuil'

ROOT_DIR: Final[Path] = Path().absolute().resolve(strict=True)

CONF_DIR_NAME: Final[str] = 'conf'
CONF_DIR: Final[Path] = ROOT_DIR / CONF_DIR_NAME
CONF_DIR.resolve(strict=True)

SCRIPTS_DIR_NAME: Final[str] = 'scripts'
SCRIPTS_DIR: Final[Path] = ROOT_DIR / SCRIPTS_DIR_NAME
SCRIPTS_DIR.resolve(strict=True)

REQS_FILE_NAME: Final[str] = 'requirements.txt'
REQS_FILE: Final[Path] = ROOT_DIR / REQS_FILE_NAME
REQS_FILE.resolve(strict=True)

VENV_DIR_NAME: Final[str] = 'venv'
VENV_DIR: Final[Path] = CONF_DIR / VENV_DIR_NAME


def _print_header(message: str) -> None:
    print(message)
    print('-' * len(message))


class EnvBuilderInstallReqs(venv.EnvBuilder):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def upgrade_dependencies(self, context: SimpleNamespace) -> None:
        _print_header('Upgrade dependecies : pip, setuptools')

        super().upgrade_dependencies(context=context)
        self.__install_reqs(context=context)

    def post_setup(self, context: SimpleNamespace) -> None:
        self.__setup_venv_pythonpath_files()

    @staticmethod
    def __dir_relative_to_root(project_subdir: Path) -> Path:
        absolute_dir: Final[Path] = project_subdir.resolve(strict=True)
        assert absolute_dir.is_dir()

        relative_dir: Path

        if project_subdir.is_relative_to(ROOT_DIR):
            relative_dir = absolute_dir.relative_to(ROOT_DIR)
        elif project_subdir.is_absolute():
            raise ValueError(f"The supplied directory must be a subdirectory within the hierarchy of the project's root directory { {project_subdir, ROOT_DIR}= }")
        else:
            relative_dir = absolute_dir

        return relative_dir

    @staticmethod
    def __create_pythonpath_include_file(include_file: Path, file_content: str) -> None:
        include_file_mode: Final[int] = 0o660
        include_file_encoding: Final[str] = encodings.utf_8.getregentry().name

        include_file.parent.mkdir(exist_ok=True)
        include_file.touch(mode=include_file_mode)
        include_file.write_text(data=file_content, encoding=include_file_encoding)

    @classmethod
    def __generate_pythonpath_include_file_name(cls, include_dir: Path) -> str:
        assert include_dir.is_dir()

        include_file_extension: Final[str] = 'pth'

        relative_dir: Final[Path] = cls.__dir_relative_to_root(include_dir)

        include_path: Final[str] = str(relative_dir.as_posix())
        include_file_name: str = include_path.replace('/', '.')
        include_file_name = '.'.join([include_file_name, include_file_extension])

        return include_file_name

    @classmethod
    def __include_dir_to_venv_pythonpath(cls, include_dir: Path) -> str:
        relative_dir: Final[Path] = cls.__dir_relative_to_root(include_dir)
        include_file_name = cls.__generate_pythonpath_include_file_name(relative_dir)

        include_file: Final[Path] = VENV_DIR / include_file_name

        venv_subdir_level: Final[int] = len(VENV_DIR.relative_to(ROOT_DIR).parents)
        venv_to_root_path: Final[str] = os.path.join(os.path.curdir, *(venv_subdir_level * (os.path.pardir,)))
        venv_to_scripts_path: Final[str] = os.path.join(venv_to_root_path, relative_dir)

        cls.__create_pythonpath_include_file(include_file, venv_to_scripts_path)

        return include_file_name

    @classmethod
    def __setup_venv_pythonpath_files(cls) -> None:
        _print_header('Create the virtual environment PYTHONPATH files')
        print(f'{VENV_DIR_NAME}={VENV_DIR}')

        include_dir_name: str = cls.__include_dir_to_venv_pythonpath(SCRIPTS_DIR)
        print(f'{SCRIPTS_DIR_NAME}={include_dir_name}')

        print()

    @classmethod
    def __install_reqs(cls, context: SimpleNamespace) -> None:
        pip_cmd_args: list[str] = cls.__assemble_pip_cmd_args(context=context)

        print()
        _print_header('Install requirements.txt using pip')

        subprocess.check_call(pip_cmd_args)

    @staticmethod
    def __assemble_pip_cmd_args(context: SimpleNamespace) -> list[str]:
        module_option: Final[str] = '-m'
        pip_arg: Final[str] = 'pip'
        pip_install_arg: Final[str] = 'install'
        pip_install_reqs_option: Final[str] = '-r'

        venv_python = str(context.env_exe)

        pip_cmd_args: list[str] = [venv_python,
                                   module_option,
                                   pip_arg,
                                   pip_install_arg,
                                   pip_install_reqs_option,
                                   REQS_FILE]

        return pip_cmd_args


venv_builder = EnvBuilderInstallReqs(clear=True,  # TODO : Remove clear arg
                                     with_pip=True,
                                     upgrade_deps=True)

venv_builder.create(env_dir=VENV_DIR)
