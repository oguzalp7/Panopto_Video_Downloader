import shutil
import os
TS_DIR = 'ts_files'


cwd = os.getcwd()  # Get the current working directory (cwd)
with open('MAC_Protocols_Part2.ts', 'wb') as merged:
    for ts_file in os.listdir(f'{cwd}/{TS_DIR}'):
        with open(f'{cwd}/{TS_DIR}/{ts_file}', 'rb') as mergefile:
            shutil.copyfileobj(mergefile, merged)