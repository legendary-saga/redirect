import uvicorn
import argparse
from pydantic import BaseModel
from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()

class Config(BaseModel):
    target_url: str
    port: int

parser = argparse.ArgumentParser(description="Run a proxy FastAPI server.")
parser.add_argument("--target", type=str, help="Target URL to redirect requests to")
parser.add_argument("--port", type=int, help="Port to run the server on")

args = parser.parse_args()
target_url = input("Enter the target URL: ") if not args.target else args.target
port = input("Enter the port number: ") if not args.port else args.port

config = Config(target_url=target_url, port=port)

@app.get("/{full_path:path}")
async def read_item(full_path: str):
    return RedirectResponse(url=f"{args.target}/{full_path}")

def run():
	uvicorn.run(app, host="0.0.0.0", port=config.port)
	print('redirect now available on http://0.0.0.0:8888 or http://localhost:8888')
  
if __name__ == "__main__":
    run()