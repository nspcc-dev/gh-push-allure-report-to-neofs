import os
import requests
import pytest
import zipfile
import tempfile
from urllib.parse import urljoin


def download_to_tempfile(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()

    temp_file = tempfile.NamedTemporaryFile(delete=False)
    with open(temp_file.name, "wb") as f:
        f.write(response.content)
    return temp_file.name


def list_all_files(directory: str) -> list:
    all_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, directory)
            all_files.append(relative_path)

    return all_files


def compare_zip_files(zip_path_1: str, zip_path_2: str) -> bool:
    with zipfile.ZipFile(zip_path_1, "r") as zip1, zipfile.ZipFile(
        zip_path_2, "r"
    ) as zip2:
        zip1_files = zip1.namelist()
        zip2_files = zip2.namelist()

        if set(zip1_files) != set(zip2_files):
            return False

        for file_name in zip1_files:
            with zip1.open(file_name) as file1, zip2.open(file_name) as file2:
                if file1.read() != file2.read():
                    return False

    return True


def compare_regular_files(file_path_1: str, file_path_2: str) -> bool:
    with open(file_path_1, "r") as file1, open(file_path_2, "r") as file2:
        return file1.read() == file2.read()


def test_file_content(base_url, report_dir):
    if base_url is None or not base_url.endswith("/"):
        pytest.fail("base_url is not provided. Provide it using --base_url option.")
    print(f"base_url: {base_url}")

    if report_dir is None or not os.path.exists(report_dir):
        pytest.fail("report_dir is not provided. Provide it using --report_dir option.")
    print(f"report_dir: {report_dir}")

    all_files = list_all_files(report_dir)

    for file in all_files:
        print(f"file: {file}")
        full_url = urljoin(base_url, file)
        print(f"full_url: {full_url}")

        temp_file_path = download_to_tempfile(full_url)

        if zipfile.is_zipfile(temp_file_path):
            assert compare_zip_files(
                temp_file_path, os.path.join(report_dir, file)
            ), f"Contents of zip files {full_url} and {file} do not match."
        else:
            assert compare_regular_files(
                temp_file_path, os.path.join(report_dir, file)
            ), f"Contents of {full_url} and {file} do not match."

        os.remove(temp_file_path)
