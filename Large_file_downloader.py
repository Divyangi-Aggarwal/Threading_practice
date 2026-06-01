import threading
from tracemalloc import start
from wsgiref import headers
import requests
from urllib.parse import urlparse
import os

def download_file(url, start, end, thread):
    print(f"Starting download from {url}")
    headers = {
        "Range": f"bytes={start}-{end}"
    }
    path = urlparse(url).path
    extension = os.path.splitext(path)[1]
    response = requests.get(url, headers=headers, stream=True)
    print(
        f"Thread {thread}:",
        response.status_code
    )
    with open(f"chunk_{thread}{extension}", 'wb') as f:
        f.write(response.content)

def join_files(no_of_threads):
    with open("largefile.pdf", 'wb') as output_file:
        for i in range(no_of_threads):
            with open(f"chunk_{i}.pdf", 'rb') as chunk_file:
                output_file.write(chunk_file.read())

def thread_creation(url, no_of_threads):
    threads = []
    response = requests.head(url)
    print(response.headers)
    file_size = int(
        response.headers["Content-Length"]
    )
    chunk_size = file_size // no_of_threads
    print(f"File size: {file_size} bytes, Chunk size: {chunk_size} bytes")
    for thread in range(no_of_threads):
        start = thread * chunk_size
        end_chunk = (thread + 1) * chunk_size - 1
        t = threading.Thread(target=download_file, args=(url, start, end_chunk, thread))
        threads.append(t)
    return threads



def main():
    url = "http://localhost:8000/large_dummy.pdf"
    no_of_threads = 4
    threads = thread_creation(url, no_of_threads)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    join_files(no_of_threads)

if __name__ == "__main__":
    main()


    