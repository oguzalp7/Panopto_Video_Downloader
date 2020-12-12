# Panopto_Video_Downloader
Small project to download recorded lectures.
### Requirements
  - pip install requests
  - pip install shutil
  - pip install m3u8
## Usage
- Inspect the web page that consist a video.
- Select Network
- Refresh the page while Inspection and Network tab is open
- Find index.m3u8
- Copy index.m3u8 request url
- Paste the url to video_dwnld.py and run the code
- Checkout how many ts file is used on a video. Take the non-zero part of the ts file as an integer.
- In download_ts.py use the integer value that you've took from video_dwnld.py for second parameter on download_ts.py/download_ts
- Go back to Network tab in your web browser, select an 000xx.ts and copy request url without filename ex. "some_url/00".
- Leave the filling operation to the program.
- Pass that parameter to download_ts(url, length_of_ts) in download_ts.py and run the program, wait until it downloads every ts file.
- Then move on to the merge_ts.py, if you desire you can change the name of the output. Run the merge_ts.py as well.
- Your recorded lecture is in the same directory, happy working offline :)
