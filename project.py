from flask import Flask,jsonify,request
app = Flask(__name__)
tasks=[
    {
        "id":1,
        "Contact":"3828493829",
        "name":"AJ",
        "done":False
    },
    {
        "id":2,
        "Contact":"2937483746",
        "name":"Michael",
        "done": False
    }
]
@app.route("/")
def hello_world():
    return "hello_world"

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    task={
        "id":tasks[-1]["id"] + 1,
        "name":request.json["name"],
        "Contact":request.json.get("Contact",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

if (__name__ == "__main__"):
    app.run(debug=True)