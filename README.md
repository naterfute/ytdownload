# Page_boy

## ***IMPORTANT***

Please do Note that this Runs using a flask server, the flask server has **No way To authenticate**, That means
if you have the port open to the public, anyone can send requests. This is not something you want, as far as i'm
aware, there are no errors in my code that would allow anyone to execute any destructive code or something else malicious.
That's only as far as I know, just be careful with this.

### Prefers Playlist over individual videos

This entire branch was made for me to add music to my plex server with no hassle,
It was not made to be customizable, if you are looking for something easy to use
with little configuration needed to be done, go to the [Master Branch](https://github.com/KalebSchmidlkofer/ytdownload/tree/master)!

This branch is used to download youtube videos then send them to a server,
or to start a web-server and take url requests to download
the youtube videos onto a remote server.

## Plans for the future

### Database

whenever request is gotten append to a postgresql table with the following property's
 name | type |
| --- | --- |
| url | str |
| Queued | bool |
| downloaded | str |
| downloaded_data | relational to the download data from  download |

After finished downloaded set Queued to False on the Download
then set a relation from wherever it got saved in the downloads table to download_data
for easy access to the information from this table.
