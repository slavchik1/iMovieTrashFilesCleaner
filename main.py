import os
import shutil
from helper_functions import *

ELEMENTS_NOT_MOVIES = ['lock', 'Settings.plist', '__Sync__', 'CurrentVersion.flexolibrary', '__Temp', 'CurrentVersion.plist']

iMovie_folder_path = os.path.expanduser('~/Movies')
iMovie_library_name = [item for item in os.listdir(iMovie_folder_path) if item.endswith('.imovielibrary')][0]
iMovie_library_path = os.path.expanduser(f'~/Movies/{iMovie_library_name}')
iMovie_library_items = [item for item in os.listdir(iMovie_library_path) if not item.startswith('.') and item not in ELEMENTS_NOT_MOVIES]


deleted_files_size = 0


for i in iMovie_library_items:
    movie_path = f'{iMovie_library_path}/{i}'
    movie_items = os.listdir(movie_path)

    if 'Render Files' in movie_items:
        render_files_path = f'{movie_path}/Render Files'

        deleted_files_size += get_folder_size(render_files_path)
        shutil.rmtree(render_files_path)



print(f"Deleted files size: {deleted_files_size} Bytes / {convert_size(deleted_files_size)}")
