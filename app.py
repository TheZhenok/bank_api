import fastapi


class FastAPIApp(fastapi.FastAPI):
    """Custom class."""
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
