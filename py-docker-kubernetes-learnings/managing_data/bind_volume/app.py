from flask import Flask

app = Flask(__name__)


@app.get("/api/v1/demo_bind_vol")
def get_all_fruits():
    with open("./userchanges/file_on_host.txt") as f:
        contents = f.readlines()
    return {"message":contents}, 200