import requests


def download_video_series(video_links):
    for link in video_links:

        '''iterate through all links in video_links  
        and download them one by one'''

        # obtain filename by splitting url and getting
        # last string
        file_name = link.split('/')[-1]

        print("Downloading file:%s" % file_name)

        # create response object
        r = requests.get(link, stream=True)

        # download started
        with open(f"ts_files/{file_name}", 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        print("%s downloaded!\n" % file_name)

    print("All videos downloaded!")
    return


def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(f"ts_files/{local_filename}", 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    return local_filename


def download_ts(url, ts_len):
    url_copy = url
    for i in range(ts_len+1):
        i = str(i)
        length = len(i)
        zero_number = "0" * (3 - length)
        final_number = zero_number + i
        # print(final_number)
        url += final_number
        url += '.ts'
        download_file(url)
    url = url_copy

url = 'https://d2y36twrtb17ty.cloudfront.net/sessions/5b9ddb75-a33f-4c69-9fe9-ac44010e0f41/0474d621-81fa-4cc2-befd-ac44010e0f52-659f4a78-cb9d-462c-8341-ac4401222401.hls/534593/00'
links = []
for i in range(354):
    i = str(i)
    length = len(i)
    zero_number = "0" * (3 - length)
    final_number = zero_number + i
    #print(final_number)
    url += final_number
    url += '.ts'
    download_file(url)
    url = 'https://d2y36twrtb17ty.cloudfront.net/sessions/5b9ddb75-a33f-4c69-9fe9-ac44010e0f41/0474d621-81fa-4cc2-befd-ac44010e0f52-659f4a78-cb9d-462c-8341-ac4401222401.hls/534593/00'




