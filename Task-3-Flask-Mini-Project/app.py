from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        name = request.form["name"]
        department = request.form["department"]

        with open("students.txt", "a") as file:
            file.write(f"Name: {name}, Department: {department}\n")

        message = "Student details saved successfully!"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
