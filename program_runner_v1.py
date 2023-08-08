from file_finder_v1 import filefinder
from torrent_downloader_v1 import torrent_downloader

start_runner = input(
    "\nStart downloading torrent files?\n\n[ Yes: Y | No: N ]\n\nYour responce:")
if start_runner.strip().lower() == 'y':
    dirs = filefinder()

print(dirs)

for t in dirs:
    print(t)

for tf in dirs:
    torrent_downloader(tf)
else:
    print("Program Ended")
