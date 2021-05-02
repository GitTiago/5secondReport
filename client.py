import asyncio

import sys
import psutil
import requests

CLIENT_ID = "CLIENT_1"


async def send_running_programs(host: str):
    process_iterator = psutil.process_iter(["name"])
    process_name_iterator = (process.info["name"] for process in process_iterator)
    process_names_list = list(process_name_iterator)
    response = requests.post(f"{host}/programs/{CLIENT_ID}", json=process_names_list)
    response.raise_for_status()


async def report_programs_running(host: str):
    while True:
        asyncio.ensure_future(send_running_programs(host))
        await asyncio.sleep(5)


if __name__ == '__main__':
    args = sys.argv[1:]
    host_param = args[0]
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(report_programs_running(host_param))
    finally:
        loop.close()
