from run_stream import run_streaming
from app import app


if __name__ == "__main__":

    app.run(debug=True)
    run_streaming()
