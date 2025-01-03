from fastapi import FastAPI

app =FastAPI() 

@app.get('/javed')
async def javed() -> dict[str, str]:
    return{"messege":"hello javed"}   

@app.get('/about')        
async def javed1() -> str:
    return "hello javed1"

@app.get('/contact')
async def contact() -> str:
    return "hello contact me at 8vS6f@example.com"