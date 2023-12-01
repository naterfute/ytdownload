from assets.downloader import Downloader
urls = ['https://www.youtube.com/watch?v=l_rbFhbcbT8']

Youtube = Downloader(host='host', host_password='''Host_password''', download_path='~/Downloads')
Youtube.download(urls=urls)


