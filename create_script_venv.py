#!/usr/bin/env python3

import encodings
import os
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
SCRIPTS_DIR: Final[Path] = CONF_DIR / SCRIPTS_DIR_NAME
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
        self.__create_scripts_path_config_file()

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
    def __include_dir_to_venv_pythonpath(cls, include_dir: Path) -> None:
        relative_dir: Final[Path] = cls.__dir_relative_to_root(include_dir)
        include_file_name = cls.__generate_pythonpath_include_file_name(relative_dir)

        include_file: Final[Path] = VENV_DIR / include_file_name
        file_content: Final[str] = str(relative_dir.relative_to(VENV_DIR))
        cls.__create_pythonpath_include_file(include_file, file_content)

    @staticmethod
    def __create_scripts_path_config_file() -> None:
        path_config_file_dotless_extension: Final[str] = 'pth'
        scripts_path_config_file_name: Final[str] = '.'.join([SCRIPTS_DIR_NAME, path_config_file_dotless_extension])
        file_mode: Final[int] = 0o770
        encoding: Final[str] = encodings.utf_8.getregentry().name

        _print_header('Create scripts path config file')
        print('VEnv dir:', VENV_DIR)

        scripts_path_config_file: Path = VENV_DIR / scripts_path_config_file_name
        scripts_path_config_file.touch(mode=file_mode, exist_ok=True)
        print('Scripts path config file:', scripts_path_config_file)

        scripts_path_config: str = os.path.relpath(path=SCRIPTS_DIR, start=VENV_DIR)
        scripts_path_config_file.write_text(data=scripts_path_config, encoding=encoding)

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


venv_builder = EnvBuilderInstallReqs(clear=True,
                                     with_pip=True,
                                     upgrade_deps=True)

venv_builder.create(env_dir=VENV_DIR)
