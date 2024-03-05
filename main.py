from fastapi import FastAPI, Query
from pydantic import BaseModel
import uvicorn


app = FastAPI()

class SumResponse(BaseModel):
    success: bool
    value: int | None
    error: str | None

@app.post('/sum')
async def natural_sum(upto: int = Query(..., description="a natural number")) -> SumResponse:
    if upto < 1:
        return SumResponse(success=False, value=None, error="'upto' must be a natural number.")
    value = sum(range(1, upto+1))
    return SumResponse(success=True, value=value, error=None)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8888,
        reload=True,
        log_level="info"
    )
