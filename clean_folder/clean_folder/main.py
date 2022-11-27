from pathlib import Path
import shutil
import sys
import file_parser as parser
from normalize import normalize


def handle_files(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_archive(filename: Path, target_folder: Path):
    # Створюємо папку для архіву
    target_folder.mkdir(exist_ok=True, parents=True)
    # Створюємо папку куди розпакуємо архів
    # Беремо суфікс у файла і удаляємо replace(filename.suffix, '')
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))

    # Створюємо папку для архіву з іменем файлу
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()),
                              str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'Це не архів {filename}!')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Помилка видалення папки {folder}')


def main(folder: Path):
    parser.scan(folder)
    for file in parser.IMAGES:
        handle_files(file, folder / 'images')
    for file in parser.AUDIO:
        handle_files(file, folder / 'audio')
    for file in parser.VIDEO:
        handle_files(file, folder / 'video')
    for file in parser.DOCUMENTS:
        handle_files(file, folder / 'documents')
    for file in parser.OTHER:
        handle_files(file, folder / 'other')
    for file in parser.ARCHIVES:
        handle_archive(file, folder / 'archives')

    # Виконуємо реверс списку для того щоб видалити всі папки
    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)


def clean_folder():
    try:
        folder = sys.argv[1]
    except IndexError:
        print('Enter valid path to the folder')
    else:
        folder_for_scan = Path(folder)
        print(f'Start in folder {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())
        print(f'Sorting in folder {folder_for_scan.resolve()} ended')


if __name__ == '__main__':
    clean_folder()