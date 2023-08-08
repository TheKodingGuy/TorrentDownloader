from torrentp import TorrentDownloader
import tkinter as tk
from tkinter import filedialog


def torrent_downloader(stf):

    select_torrent = stf

    root = tk.Tk()
    root.withdraw()

    storage_dir = filedialog.askdirectory()

    torrent_file = TorrentDownloader(select_torrent, storage_dir)
    torrent_file.start_download()
