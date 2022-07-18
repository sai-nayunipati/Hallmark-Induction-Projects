let tasks = [];
const user = "Sai";

function loadTasks() {
    tasks = []
    
    fetch('http://127.0.0.1:5000/tasks/all', {method: 'GET'})
    .then(res=>res.json())
    .then(data=>{
        for (let i in data) {
            tasks.push({"id": data[i][0], "content": data[i][1], "is_completed": data[i][2], "place_in_order": data[i][3], "added_by": data[i][4]});
        }
    })
    .then(()=>tasks.sort((a,b)=>a.place_in_order-b.place_in_order))
    .then(() => renderTasks());
}

function renderTasks() {
    let html = "";

    for (let i in tasks) {
        // The task is not done
        if (tasks[i].is_completed == 0)
        {
            html += `<li class="list-group-item" id='task-${i}''><input class="form-check-input me-1" type="checkbox" value="" aria-label="..." onclick="changeCompletionStatus(${i})"> ${tasks[i].content} <i>(${tasks[i].added_by}) </i><i class="fa-solid fa-arrow-up" onclick="moveTaskUp(${i})"></i> <i class="fa-solid fa-arrow-down" onclick="moveTaskDown(${i})"></i></li>`
        }
        // The task is done
        else
        {
            html += `<li class="list-group-item" id='task-${i}''><input class="form-check-input me-1" type="checkbox" value="" aria-label="..." onclick="changeCompletionStatus(${i})" checked><s> ${tasks[i].content} <i>(${tasks[i].added_by}) </i></s><i class="fa-solid fa-arrow-up" onclick="moveTaskUp(${i})"></i> <i class="fa-solid fa-arrow-down" onclick="moveTaskDown(${i})"></i></li>`
        }
    }

    document.querySelector("#task-list").innerHTML = html;

    for (let i in tasks) {
        if (tasks[i].completed)
        {
            document.querySelector(`#task-${i}`).setAttribute("style", "opacity: 0.5");
        } 
    }
}

function addTask() {
    let content = document.querySelector("#input-box").value;
    document.querySelector("#input-box").value = "";

    if (content != "") {
        newTask = {"content": content, "is_completed": 0, "place_in_order": tasks.length + 1, "added_by": user};


        fetch('http://127.0.0.1:5000/tasks/add', {
            method: 'POST',
            headers :{
                'Content-Type': 'application/json'
            },
            body : JSON.stringify(newTask)
        })
        .then(() => loadTasks());
    } 
    else {
        console.log("Cannot add an empty item.");
    }
}

function clearTasks() {
    // Clear the tasks array and submit the request to the server
    fetch('http://127.0.0.1:5000/tasks/clear', {method: 'GET'})
    .then(() => loadTasks())
}

document.addEventListener("keypress", event => {
    if (event.keyCode == 13) { // 13 is the enter key.
        addTask();
    }
})

function changeCompletionStatus(index) {
    fetch('http://127.0.0.1:5000/tasks/update/' + tasks[index].id, {
        method: 'GET',
        headers :{
            'Content-Type': 'application/json'
        }
    })
    .then(() => loadTasks());
}

function moveTaskUp(index) {
    if (index > 0) {
        fetch('http://127.0.0.1:5000/tasks/move-up/' + tasks[index].id, {method: 'GET'})
        .then(() => loadTasks())
    }
}

function moveTaskDown(index) {
    if (index <  tasks.length - 1) {
        fetch('http://127.0.0.1:5000/tasks/move-down/' + tasks[index].id, {method: 'GET'})
        .then(() => loadTasks())
    }
}

loadTasks();
