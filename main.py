from assets.downloader import Downloader
urls = ['https://music.youtube.com/playlist?list=OLAK5uy_m2uXUd7beuveI7DE9R3di_EWMy_moTJUg&si=le2Q2_NVvjtbbx-X']

Youtube = Downloader(host='host', host_password='''Host_password''', download_path='~/Downloads')
Youtube.download(urls=urls)


