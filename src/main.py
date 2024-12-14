import uvicorn


def run_api_server():
    uvicorn.run(
        "mediassist.api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    run_api_server()
