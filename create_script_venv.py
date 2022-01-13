#!/usr/bin/env python3

import encodings
import os
import subprocess
import venv
from pathlib import Path
from types import SimpleNamespace
from typing import Final

ROOT_DIR: Final[Path] = Path().absolute()
ROOT_DIR.resolve(strict=True)

CONF_DIR_NAME: Final[str] = 'conf'
CONF_DIR: Final[Path] = ROOT_DIR / CONF_DIR_NAME
CONF_DIR.resolve(strict=True)

SCRIPT_DIR_NAME: Final[str] = 'script'
SCRIPT_DIR: Final[Path] = CONF_DIR / SCRIPT_DIR_NAME
SCRIPT_DIR.resolve(strict=True)

SRC_DIR_NAME: Final[str] = 'src'
SRC_DIR: Final[Path] = SCRIPT_DIR / SRC_DIR_NAME
SRC_DIR.resolve(strict=True)

REQS_FILE_NAME: Final[str] = 'requirements.txt'
REQS_FILE: Final[Path] = SCRIPT_DIR / REQS_FILE_NAME
REQS_FILE.resolve(strict=True)

VENV_DIR_NAME: Final[str] = 'venv'
VENV_DIR: Final[Path] = SCRIPT_DIR / VENV_DIR_NAME


class EnvBuilderInstallReqs(venv.EnvBuilder):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def upgrade_dependencies(self, context: SimpleNamespace) -> None:
        print(f'Upgrade dependecies : pip, setuptools')
        print('-------------------------------------')

        super().upgrade_dependencies(context=context)

        self.__install_reqs(context=context)

    def post_setup(self, context: SimpleNamespace) -> None:
        self.__create_src_path_config_file()

    @staticmethod
    def __create_src_path_config_file() -> None:
        path_config_file_dotless_extension: Final[str] = 'pth'
        src_path_config_file_name: Final[str] = '.'.join([CONF_DIR_NAME, SCRIPT_DIR_NAME, SRC_DIR_NAME, path_config_file_dotless_extension])
        file_mode: Final[int] = 0o770
        encoding: Final[str] = encodings.utf_8.getregentry().name

        print(f'Create src path config file')
        print('----------------------------')
        print('VEnv dir:', VENV_DIR)

        src_path_config_file: Path = VENV_DIR / src_path_config_file_name
        src_path_config_file.touch(mode=file_mode, exist_ok=True)
        print('Src path config file:', src_path_config_file)

        src_path_config: str = os.path.relpath(path=SRC_DIR, start=VENV_DIR)
        src_path_config_file.write_text(data=src_path_config, encoding=encoding)

        print()

    @classmethod
    def __install_reqs(cls, context: SimpleNamespace) -> None:
        pip_cmd_args: list[str] = cls.__assemble_pip_cmd_args(context=context)

        print()
        print('Install requirements.txt using pip')
        print('----------------------------------')

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


venv_builder = EnvBuilderInstallReqs(system_site_packages=False,
                                     clear=True,
                                     with_pip=True,
                                     upgrade_deps=True)

venv_builder.create(env_dir=VENV_DIR)
