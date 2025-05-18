import asyncio
from compute_time import compute_run_time


async def fetch_db_data(user_id):
    print('fetching data from db')
    await asyncio.sleep(2)
    print('data has been fetched')
    return f'fetched data for {user_id=}'


@compute_run_time
async def main():
    coroutine_obj = fetch_db_data(1)
    coroutine_obj_2 = fetch_db_data(2)
    print(coroutine_obj)
    print(coroutine_obj_2)
    awaited_coroutine_obj_res = await coroutine_obj
    awaited_coroutine_obj_res_2 = await coroutine_obj_2
    print(awaited_coroutine_obj_res_2)
    print(awaited_coroutine_obj_res)


if __name__ == "__main__":
    asyncio.run(main())  # this says asyncio to create event-loop to run the co-routines
"""
Print statement in order 
<coroutine object fetch_db_data at 0x000001F9CEFA7F40>
<coroutine object fetch_db_data at 0x000001F9CEFFE500>
fetching data from db
data has been fetched
fetching data from db
data has been fetched
fetched data for user_id=2
fetched data for user_id=1
Execution time for `main`: 4.02 seconds  [ from @compute_run_time decorator ] 
"""