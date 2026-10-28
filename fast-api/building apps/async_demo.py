import time
from timeit import default_timer as timer
import asyncio


async def run_task(name, seconds):
    print(f"{name} started at {timer()}")
    await asyncio.sleep(seconds)
    print(f"{name} completed at: {timer()}")



async def main():
    start = timer()
    await asyncio.gather(
        run_task('Task 1', 2),
        run_task("Task 2", 1),
        run_task("Task 3", 3)
    )
    
    finish = timer()
    print(f"Time taken to run the task: {(finish-start):.4f}")


asyncio.run(main())