from fastapi.testclient import TestClient
from datetime import datetime
from http import HTTPStatus

import os

TEST_CLIENT_ID = "TEST_CLIENT"
EXPECTED_DATE_FORMAT = "%m/%d/%Y, %H:%M:%S"


def test_post_programs_success(client: TestClient):
    test_beginning_timestamp = datetime.now()
    file_path = f"{TEST_CLIENT_ID}_running_programs.txt"
    assert not os.path.exists(file_path)

    try:
        test_programs = ["a.exe", "b.exe", "4.exe"]

        response = client.post(f"/programs/{TEST_CLIENT_ID}", json=test_programs)
        assert response.status_code == HTTPStatus.CREATED
        assert os.path.exists(file_path)

        with open(file_path, mode='r') as programs_file:
            n_lines = 0
            for line in programs_file:
                n_lines += 1
                end_date_index = line.index(']')
                date_string = line[1:end_date_index]
                # By attempting to create a date, we check the formatting
                line_time = datetime.strptime(date_string,
                                              EXPECTED_DATE_FORMAT)
                assert test_beginning_timestamp.replace(microsecond=0) <= line_time
                assert line_time <= datetime.now().replace(microsecond=0)
                assert line[end_date_index+1:].strip() == ",".join(test_programs)
            assert n_lines == 1
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
