from fastapi import APIRouter, Depends
from fastapi_limiter.depends import RateLimiter

from api.core.models.example_output import MessageOutput
from api.core.logic.example import run_prime_factor_calculation

router = APIRouter()

@router.get("/hello", response_model=MessageOutput, tags=["example get"])
def hello_endpoint():
    """
    Respond to requests on the hello endpoint
    """
    task = run_prime_factor_calculation.delay()
    n, largest_prime_factor, elapsed_time = task.wait(timeout=None, interval=0.5)

    return {
        "message1": "Hello, world!",
        "message2": f"The largest prime factor of {n} is {largest_prime_factor}. Calculation took {elapsed_time:0.3f} seconds.",
        "n": n,
        "largest_prime_factor": largest_prime_factor,
        "elapsed_time": elapsed_time,
    }

@router.get("/limited", dependencies=[
                                        Depends(RateLimiter(times=1, seconds=5)),
                                        Depends(RateLimiter(times=2, seconds=15)),
                                    ], response_model=MessageOutput, tags=["example limited get"])
async def limited():
    """
    Respond to requests on the hello endpoint
    """
    task = run_prime_factor_calculation.delay()
    n, largest_prime_factor, elapsed_time = task.wait(timeout=None, interval=0.5)

    return {
        "message1": "Hello, world!",
        "message2": f"The largest prime factor of {n} is {largest_prime_factor}. Calculation took {elapsed_time:0.3f} seconds.",
        "n": n,
        "largest_prime_factor": largest_prime_factor,
        "elapsed_time": elapsed_time,
    }

@router.get("/limited/{get_string}", dependencies=[
                                        Depends(RateLimiter(times=1, seconds=5)),
                                        Depends(RateLimiter(times=2, seconds=15)),
                                    ], response_model=MessageOutput, tags=["example limited get"])
async def limited(get_string: str):
    """
    Respond to requests on the hello endpoint
    """
    task = run_prime_factor_calculation.delay()
    n, largest_prime_factor, elapsed_time = task.wait(timeout=None, interval=0.5)

    return {
        "message1": f"Hello, {get_string}!",
        "message2": f"The largest prime factor of {n} is {largest_prime_factor}. Calculation took {elapsed_time:0.3f} seconds.",
        "n": n,
        "largest_prime_factor": largest_prime_factor,
        "elapsed_time": elapsed_time,
    }