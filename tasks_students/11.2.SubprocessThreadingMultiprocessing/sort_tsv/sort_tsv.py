import subprocess
from pathlib import Path
import typing as tp


def python_sort(file_in: Path, file_out: Path) -> None:
    """
    Sort tsv file using python built-in sort
    :param file_in: tsv file to read from
    :param file_out: tsv file to write to
    """
    with open(file_in, 'r') as f_in, open(file_out, 'w') as f_out:
        lines: tp.Any = f_in.readlines()
        sorted_lines: tp.Any = sorted(lines, key=lambda x: (int(x.split('\t')[1]), x.split('\t')[0]))
        f_out.writelines(sorted_lines)


def util_sort(file_in: Path, file_out: Path) -> None:
    """
    Sort tsv file using sort util
    :param file_in: tsv file to read from
    :param file_out: tsv file to write to
    """
    subprocess.run(['sort', '-t', '\t', '-k', '2n', '-k', '1', '-o', str(file_out), str(file_in)], check=True)
