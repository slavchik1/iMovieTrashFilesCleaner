from pathlib import Path


def get_folder_size(folder_path):
    return sum(f.stat().st_size for f in Path(folder_path).rglob('*') if f.is_file())


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0 B"

    size_name = ("B", "KB", "MB", "GB", "TB", "PB")
    i = int((len(str(size_bytes)) - 1) // 3)
    p = 1024 ** i
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"
