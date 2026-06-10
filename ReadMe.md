1. download the "task_manager.py" file
2. create a virtual environment, activate it, and install flask in it
3. open a terminal in the directory where the "task_manager.py" file is saved
4. run the code using the following command: "python task_manager.py"
5. open another terminal and run the following command to access the tasks:

    curl -X GET http://127.0.0.1:5000/tasks

    or open a web browser and go to the following URL: http://127.0.0.1:5000/tasks

6. to create a task run the following commands:

    Windows:

    curl -X POST -H "Content-Type: application/json" -d "{\"title\":\"Clean files\",\"description\":\"Clean files left from the previous execution\",\"status\":\"todo\"}" http://127.0.0.1:5000/tasks

    Linux or Mac:

    curl -X POST -H "Content-Type: application/json" -d '{"title":"Clean files","description":"Clean files left from the previous execution","status":"todo"}' http://127.0.0.1:5000/tasks

7. to get a specific task run the following command:

    curl -X GET http://127.0.0.1:5000/tasks/"task id here"

    For example: 

    curl -X GET http://127.0.0.1:5000/tasks/25087f8b6b1c4303916f516503ce549b

    or visit the following URL: http://127.0.0.1:5000/tasks/25087f8b6b1c4303916f516503ce549b

8. to update the status of a task run the following commands:

    Windows: 

    curl -X PUT -H "Content-Type: application/json" -d "{\"status\":\"status state here\"}" http://127.0.0.1:5000/tasks/"task id here"

    Linux or Mac:

    curl -X PUT -H "Content-Type: application/json" -d '{"status":"status state here"}' http://127.0.0.1:5000/tasks/"task id here"

    For example: 

    curl -X PUT -H "Content-Type: application/json" -d "{\"status\":\"in_progress\"}" http://127.0.0.1:5000/tasks/25087f8b6b1c4303916f516503ce549b

9. to delete a task run the following command:

    curl -X DELETE http://127.0.0.1:5000/tasks/"task id here"

    For example:

    curl -X DELETE http://127.0.0.1:5000/tasks/01733f7de35a4b74826c401aa7ff0e77