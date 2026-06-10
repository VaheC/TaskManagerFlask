from flask import Flask, make_response, request
from uuid import uuid4
from datetime import datetime

task_storage = {}

app = Flask('task_manager')

@app.get('/tasks')
def retrieve_task():
    return make_response(task_storage)

@app.get('/tasks/<id>')
def retrieve_task_by_id(id):
    task = task_storage.get(id)
    if not task:
        return make_response({"message": "Task not found!!!"}, 404)
    return make_response(task)

@app.post('/tasks')
def create_task():
    task = {}
    task_id = uuid4().hex
    task['id'] = task_id
    task['title'] = request.json.get('title', 'Missing')
    task['description'] = request.json.get('description', 'Missing')
    task['status'] = request.json.get('status', 'Missing')
    task['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task_storage[task_id] = task
    return make_response({'Created task id': task['id']})

@app.put('/tasks/<id>')
def update_task_by_id(id):
    task = task_storage.get(id)
    if not task:
        return make_response({'message': 'Task not found'}, 404)
    task['status'] = request.json.get('status', 'Missing')
    return make_response({'Updating status': 'Success'})

@app.delete('/tasks/<id>')
def delete_task_by_id(id):
    task = task_storage.pop(id, None)
    if not task:
        return make_response({'message': 'Task not found'}, 404)
    return make_response({f'removal of task {id}': 'Success'})
 
if __name__ == '__main__':
    app.run(debug=True)