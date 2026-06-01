# Threading_practice

A small collection of example scripts demonstrating basic threading patterns in Python: creating threads, joining threads, and using threads to parallelize I/O-bound work (a simple large-file downloader).

## Contents

- [create_dummy_file.py](create_dummy_file.py): Generates a large dummy PDF (`large_dummy.pdf`) using ReportLab. Useful for testing the downloader.
- [Large_file_downloader.py](Large_file_downloader.py): Splits a remote file into byte ranges and downloads chunks in parallel using `threading`, then joins the chunks into `largefile.pdf`.
- [thread.py](thread.py): Minimal example showing how to start multiple threads for a blocking I/O simulation (simple crawler stub).

## Requirements

- Python 3.8+
- Python packages:
  - `requests` (for HTTP downloads)
  - `reportlab` (for generating the dummy PDF)

Install dependencies with pip:

```bash
pip install requests reportlab
```

## Usage

1. Generate a large dummy PDF (optional, for testing):

```bash
python create_dummy_file.py
```

This will generate `large_dummy.pdf` in the current directory. The default in the script is to generate a very large file; edit the `pages` argument in `generate_dummy_pdf()` if you want a smaller file for quick tests.

2. Serve the file locally (so the downloader can fetch it). From the directory containing `large_dummy.pdf` run:

```bash
python -m http.server 8000
```

3. Run the downloader (the script defaults to `http://localhost:8000/large_dummy.pdf` and 4 threads):

```bash
python Large_file_downloader.py
```

The downloader will create chunk files named like `chunk_0.pdf`, `chunk_1.pdf`, ... and then combine them into `largefile.pdf`.

Notes and caveats:
- The downloader uses HTTP `Range` requests. The remote server must support range requests (e.g., `python -m http.server` does support them for static files).
- The current `join_files` implementation expects `.pdf` chunks and writes `largefile.pdf` — adjust file naming in the code if you download a different file type.
- Error handling and retries are minimal; this is an educational example, not production-ready code.

## thread.py

Run `thread.py` to see a minimal threading example that spawns a thread per link and waits for all threads to finish:

```bash
python thread.py
```

## Next steps / Improvements

- Add robust error handling and download retry/backoff.
- Detect MIME type/extension automatically instead of assuming `.pdf`.
- Provide a CLI to configure target URL, number of threads, and output filename.

## License

This repository is provided as-is for learning purposes. Use freely.
