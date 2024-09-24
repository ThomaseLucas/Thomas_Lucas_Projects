from flask import Flask, request, render_template
import json

tasks = [
    ]

app = Flask(__name__)

def save_to_file():
    with open('tasks.txt', 'w') as file:
        json.dump(tasks, file)

def load_from_file():
    global tasks
    try:
        with open('tasks.txt', 'r') as file:
            tasks = json.load(file)
    
    except FileNotFoundError:
        tasks = []

load_from_file()

@app.route('/')
def home():

    return "<h1>Welcome to a place to keep tasks organized!</h1><a href='/tasks'><button>Go To Task List</button></a>"


@app.route('/tasks')
def get_tasks():

    print("Rendering tasks.html with tasks:", tasks)
    return render_template('tasks.html', tasks=tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

    new_task = {
        "id": tasks[-1]["id"] + 1 if tasks else 1, #iterates through starting at 1 if nothing in the list
        "title": data["title"],
        "description": data["description"]
    }

    tasks.append(new_task)
    save_to_file()

    return {"message": "Task Created Successfully", "task": new_task}, 201

@app.route('/tasks/<int:task_id>', methods = ['PUT'])
def update_tasks(task_id):
    data = request.get_json()
    task = next((task for task in tasks if task["id"] == task_id), None)

    if task is None:
        return {"message": "Task not found"}, 404

    task["title"] = data.get("title", task["title"])
    task["description"] = data.get("description", task["description"])

    save_to_file()

    return {"message": "Task updated successfully", "task": task}

@app.route('/tasks/<int:task_id>/complete', methods = ['PUT'])
def mark_as_complete(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)

    if task is None:
        return {"message": "Task not found"}, 404

    task["Completed"] = True

    save_to_file()

    return {"message": "Task marked as complete", "task": task}

@app.route('/tasks/<int:task_id>/incomplete', methods = ['PUT'])
def mark_as_incomplete(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)

    if task is None:
        return {"message": "Task not found"}, 404

    task["Completed"] = False

    save_to_file()

    return {"message": "Task marked as incomplete", "task": task}
 



if __name__ == '__main__':
    app.run(debug = True)



#Imagine I know nothing (because i do) and that I am just starting out and trying to learn these things. You are my tutor. Tutors do not give the answers, nor do they give too much information at once. You are here to help me reach conclusions on my own by asking one question at a time, and based on my response you are able to asses what is most important to teach me about the topic. Do not give me multiple questions at once, give me one question and wait for my answer and base your next information or question on my answer. Always start by asking my name.