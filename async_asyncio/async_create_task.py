import asyncio
from compute_time import compute_run_time
from typing import Any, Dict


async def fetch_db_data(user_id):
    print(f'fetching data from db for {user_id=}')
    await asyncio.sleep(2)
    print(f'data has been fetched for {user_id=}')
    return f'fetched data for {user_id=}'


async def fetch_external_api_data(pub_key: str, **kwargs: Any) -> Dict[str, Any]:
    print(f"going to fetch external api data from using {pub_key=}")
    if kwargs.get('action') and kwargs.get('action').lower() == 'failed':
        raise Exception('task failed for testing')
    await asyncio.sleep(4)
    print(f"data has been fetched using public key {pub_key=}")
    return {"status": "success", "data": "dummy data"}


@compute_run_time
async def main():
    coroutine_obj_1 = asyncio.create_task(fetch_db_data(1))
    coroutine_obj_2 = asyncio.create_task(fetch_db_data(2))
    coroutine_obj_3 = asyncio.create_task(fetch_external_api_data('dummy', action='failed'))
    coroutine_obj_4 = asyncio.create_task(fetch_external_api_data('dummy'))
    tasks = [coroutine_obj_1, coroutine_obj_2, coroutine_obj_3, coroutine_obj_4]
    res = []

    for task in tasks:
        try:
            result = await task
            res.append(result)
        except asyncio.TimeoutError:
            print(f'task {task.get_name()=} is timed out ')
            task.cancel('FAILED')
        except Exception as e:
            print(f' task {task.get_name()=} raise the exception as {str(e)}')



    # print(coroutine_obj_1)
    # print(coroutine_obj_2)
    # awaited_coroutine_obj_res = await coroutine_obj_1
    # awaited_coroutine_obj_res_2 = await coroutine_obj_2
    # print(awaited_coroutine_obj_res_2)
    # print(awaited_coroutine_obj_res)


if __name__ == "__main__":
    asyncio.run(main())  # this says asyncio to create event-loop to run the co-routines

"""
OUTPUT: <Task pending name='Task-2' coro=<fetch_db_data() running at 
C:\\Users\Gi-Admin\PycharmProjects\\15_days_python\\async_asyncio\\async_create_task.py:5>> <Task pending name='Task-3' 
coro=<fetch_db_data() running at ""C:\\Users\Gi-Admin\PycharmProjects\\15_days_python\\async_asyncio\\async_create_task.py""
:5>> fetching data from db for user_id=1 fetching data from db for user_id=2 data has been fetched for user_id=1 data 
has been fetched for user_id=2 fetched data for user_id=2 fetched data for user_id=1 Execution time for main: 2.01 
seconds  ( now this running concurrently like when non-blocking io gets sleep for 2 second event loop started another 
task to execute and the returned both maintaining concurrency)

"""
