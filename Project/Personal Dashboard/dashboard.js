// Check log
function checklogin() {
    let log = localStorage.getItem("isLoggedIn");
    if (log === "true") {
        document.querySelector("#login-section").style.display = 'none';
        document.querySelector("#dashboard").style.display = 'block';
    }
    else if (!log) {
        document.querySelector("#login-section").style.display = 'block';
    }
}
checklogin();

// Login
document.getElementById("login-info").addEventListener("submit", savelogin);

function savelogin(event) {
    event.preventDefault();
    let usernamestore = localStorage.getItem("name")
    let passwordstore = localStorage.getItem("password")
    let usernameinput = document.querySelector("#login_name").value;
    let passwordinput = document.querySelector("#login_password").value;
    if (!usernamestore && !passwordstore) {

        document.getElementById('newlogmessage').style.display = 'block'
    }
    else if ((usernamestore !== usernameinput) && (passwordstore !== passwordinput)) {
        document.getElementById('wrongnamepassword').style.display = 'block'
        document.getElementById('wrong-name').style.display = 'none'
        document.getElementById('wrong-password').style.display = 'none'
    }
    else if (usernamestore !== usernameinput) {
        document.getElementById('wrong-name').style.display = 'block'
        document.getElementById('wrongnamepassword').style.display = 'none'
        document.getElementById('wrong-password').style.display = 'none'
    }
    else if (passwordstore !== passwordinput) {
        document.getElementById('wrong-password').style.display = 'block'
        document.getElementById('wrongnamepassword').style.display = 'none'
        document.getElementById('wrong-name').style.display = 'none'
    }

    else if ((usernamestore === usernameinput) && (passwordstore === passwordinput)) {
        document.querySelector("#login-section").style.display = 'none';
        document.querySelector("#dashboard").style.display = 'block';
        localStorage.setItem("isLoggedIn", "true");
    }
}

// Sign up
document.getElementById('newlog-button').addEventListener('click', showwarn)
function showwarn() {

    let usernamestore = localStorage.getItem("name")
    let passwordstore = localStorage.getItem("password")

    let usernameinput = document.querySelector("#login_name").value;
    let passwordinput = document.querySelector("#login_password").value;

    document.getElementById("showname").textContent = usernameinput
    document.getElementById("showpassword").textContent = passwordinput

    if (!usernameinput || !passwordinput) {
        alert("Name aur Password tu enter kro")
    }
    else if (usernamestore && passwordstore) {
        document.getElementById('warn-del-data').style.display = 'flex'
        document.getElementById("overlay").style.display = 'block'
    }
    else {
        document.getElementById('overlay').style.display = 'block'
        document.getElementById('save-log-warn-pop').style.display = 'flex'

    }
}

document.getElementById('log-confirm').addEventListener('click', newlogin)

function newlogin() {

    localStorage.clear();

    let usernameinput = document.querySelector("#login_name").value;
    let passwordinput = document.querySelector("#login_password").value;

    localStorage.setItem("name", usernameinput)
    localStorage.setItem("password", passwordinput)

    document.querySelector("#login-section").style.display = 'none';
    document.querySelector("#dashboard").style.display = 'block';
    document.getElementById('save-log-warn-pop').style.display = 'none'
    document.getElementById('overlay').style.display = 'none'

    localStorage.setItem("isLoggedIn", "true");

    location.reload()
}

document.getElementById("confirm-del-data").addEventListener('click', deldata)
function deldata() {

    let usernamestore = localStorage.getItem("name")
    let passwordstore = localStorage.getItem("password")


    let usernameinput = document.querySelector("#login_name").value;
    let passwordinput = document.querySelector("#login_password").value;

    document.getElementById('warn-del-data').style.display = 'none'
    document.getElementById('overlay').style.display = 'block'
    document.getElementById("save-log-warn-pop").style.display = 'flex'

}

// Logout
document.getElementById('logout-button').addEventListener('click', logout)

function logout() {

    localStorage.setItem("isLoggedIn", "false");
    location.reload();

}

// Year Month Progress bar
function progress() {

    let today = new Date();

    // YEAR

    let year = today.getFullYear();

    let startYear = new Date(year, 0, 1);

    let endYear = new Date(year, 11, 31);

    let passedDays = (today - startYear) / (1000 * 60 * 60 * 24);

    let totalDays = (endYear - startYear) / (1000 * 60 * 60 * 24) + 1;

    let yearPercent = (passedDays / totalDays) * 100;

    document.getElementById("year-percent").textContent =
        Math.floor(yearPercent) + "%";

    document.getElementById("year-fill").style.width =
        yearPercent + "%";



    // MONTH

    let currentMonth = today.getMonth();

    let startMonth = new Date(year, currentMonth, 1);

    let endMonth = new Date(year, currentMonth + 1, 0);

    let passedMonthDays = today.getDate();

    let totalMonthDays = endMonth.getDate();

    let monthPercent = (passedMonthDays / totalMonthDays) * 100;

    document.getElementById("month-percent").textContent =
        Math.floor(monthPercent) + "%";

    document.getElementById("month-fill").style.width =
        monthPercent + "%";

}

progress();

// Data Time 
function updatetime() {

    let now = new Date();

    let date = now.toLocaleDateString("en-GB", {
        weekday: "short",
        day: "numeric",
        month: "short",
        year: "numeric"
    });

    let time = now.toLocaleTimeString("en-US", {
        hour: "2-digit",
        minute: "2-digit"
    })

    document.getElementById("date").textContent = date;
    document.getElementById("time").textContent = time;

}
updatetime();
setInterval(updatetime, 1000);

// Task Add
document.getElementById("add-task").addEventListener("click", addtask);
function addtask() {

    document.getElementById("overlay").style.display = 'block'
    document.getElementById("task-pop").style.display = 'flex'

}

// Overlay
document.getElementById('overlay').addEventListener('click', overlayfun)
function overlayfun() {

    document.getElementById('overlay').style.display = 'none'

    let pop = document.querySelectorAll('.popup');

    pop.forEach(element => {
        element.style.display = 'none'
    });
    location.reload();
}

// Date Time
let date = new Date();
let formatted = date.toLocaleString("en-US", {
    weekday: "short",
    day: "2-digit",
    month: "short",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    hour12: true
});

// Task add
let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

document.getElementById('task-add-pop').addEventListener('submit', savetask)
function savetask() {

    let inputtaskname = document.getElementById('task-name').value
    let inputtaskdescription = document.getElementById('task-description').value
    let inputtaskdate = document.getElementById('task-date').value
    let formattedDate

    if (inputtaskdate) {
        let parts = inputtaskdate.split("-");

        formattedDate = `${parts[2]}-${parts[1]}-${parts[0]}`;
    }

    let deadline = formattedDate || new Date().toLocaleDateString("en-GB");
    let task;

    task = {
        id: Date.now(),
        title: inputtaskname,
        detail: inputtaskdescription,
        deadline: deadline,
        completed: false,
        adddate: formatted
    }

    tasks.push(task);

    localStorage.setItem("tasks", JSON.stringify(tasks))
}


// Check Task
function checktask() {
    if (tasks.length > 0) {

        let parent = document.getElementById("task-list")

        tasks.forEach(task => {
            let taskdiv = document.createElement('div')
            taskdiv.classList.add("task-card");
            taskdiv.id = task.id;
            parent.appendChild(taskdiv)

            let checkbox = document.createElement('input')
            checkbox.type = "checkbox"
            checkbox.classList.add("task-checkbox")
            checkbox.checked = task.completed
            taskdiv.appendChild(checkbox)

            let tasknamediv = document.createElement('div')
            tasknamediv.classList.add("task-name");
            tasknamediv.textContent = task.title;
            taskdiv.appendChild(tasknamediv)

            let taskdeadline = document.createElement('div')
            taskdeadline.classList.add("deadline-text")
            taskdeadline.textContent = task.deadline;
            taskdeadline.classList.add("taskdeadlinetext")
            taskdiv.appendChild(taskdeadline)

        });
    }
}
checktask()

// Task Completed

let checkbox = document.querySelectorAll(".task-checkbox")

checkbox.forEach(checkbox => {
    checkbox.addEventListener("click", () => {
            event.stopPropagation();

        let id = Number(checkbox.parentElement.id)
        let task1 = tasks.find(task => task.id === id);
        console.log(task1.completed)
        if (task1.completed) {
            task1.copmletedAt = ""
            task1.completed = false
            console.log(task1.copmletedAt)
            localStorage.setItem("tasks", JSON.stringify(tasks));

        }
        else {
            task1.copmletedAt = formatted
            task1.completed = true
            console.log(task1.copmletedAt)
            localStorage.setItem("tasks", JSON.stringify(tasks));

        }

    })
});

// // Task Details
function taskclick() {
    let cards = document.querySelectorAll(".task-card");

    cards.forEach(card => {
        card.addEventListener('click', function () {
            let task1 = tasks.find(tasks => tasks.id === Number(card.id));

            document.getElementById('overlay').style.display = "block"
            document.getElementById('task-detail-pop').style.display = "flex"

            let parent = document.getElementById('task-detail-pop')
            taskdetails = document.createElement("div")
            taskdetails.id = `task-details-${task1.id}`;
            taskdetails.classList.add("task-details-pop")
            parent.appendChild(taskdetails)



            let name = document.createElement("div")
            name.textContent = `Taks Name: ${task1.title}`
            name.contentEditable = true;
            taskdetails.appendChild(name)

            // let name_edit = document.createElement("div")
            // name_edit.style.position='relative'
            // name_edit.classList.add("edit-detail")
            // name_edit.textContent=`(Change)`
            // name.appendChild(name_edit)

//             name_edit.addEventListener("click", function() {
    
// });

            if (task1.detail) {
                let detail = document.createElement("div")
                detail.textContent = `Detail: ${task1.detail}`
                taskdetails.appendChild(detail)

            //     let detail_edit = document.createElement("div")
            // detail_edit.classList.add("edit-detail")
            // detail_edit.style.position='relative'
            // detail_edit.textContent=`(Change)`
            // detail.appendChild(detail_edit)
            }

            let adddate = document.createElement("div")
            adddate.textContent = `Add at: ${task1.adddate}`
            taskdetails.appendChild(adddate)

            // let adddate_edit = document.createElement("div")
            // adddate_edit.style.position='relative'
            // adddate_edit.classList.add("edit-detail")
            // adddate_edit.textContent=`(Change)`
            // adddate.appendChild(adddate_edit)

            let deadline = document.createElement("div")
            deadline.textContent = `Deadline: ${task1.deadline}`
            taskdetails.appendChild(deadline)

            // let deadline_edit = document.createElement("div")
            // deadline_edit.style.position='relative'
            // deadline_edit.classList.add("edit-detail")
            // deadline_edit.textContent=`(Change)`
            // deadline.appendChild(deadline_edit)

            if(task1.completed){
            let completedAt = document.createElement("div")
            completedAt.textContent = `Completed At: ${task1.copmletedAt}`
            taskdetails.appendChild(completedAt)

            // let completedAt_edit = document.createElement("div")
            // completedAt_edit.style.position='relative'
            // completedAt_edit.classList.add("edit-detail")
            // completedAt_edit.textContent=`(Change)`
            // completedAt.appendChild(completedAt_edit)
            }
        })
    });
}
taskclick();
