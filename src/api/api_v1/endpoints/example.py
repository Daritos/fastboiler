from fastapi import APIRouter


from api.core.logic.example import run_prime_factor_calculation

router = APIRouter()

@router.get("/hello", tags=["example get"])
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
