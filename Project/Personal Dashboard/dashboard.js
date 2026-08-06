// Check log
let log = true;
function checklogin(){
    let usernamestore=localStorage.getItem("name")
    let passwordstore=localStorage.getItem("password")
    if((usernamestore && passwordstore) && (log===true)){
        document.querySelector("#login-section").style.display='none';
        document.querySelector("#dashboard").style.display='block';
    }
    else{
         document.querySelector("#login-section").style.display='block';
        document.querySelector("#dashboard").style.display='none';
    }
}
checklogin();

// Login
document.getElementById("login-info").addEventListener("submit", savelogin);

function savelogin(event) {
    event.preventDefault(); 
    let usernamestore=localStorage.getItem("name")
    let passwordstore=localStorage.getItem("password")
    let usernameinput= document.querySelector("#login_name").value;
    let passwordinput=document.querySelector("#login_password").value;
   
     if((usernamestore !== usernameinput) && (passwordstore !== passwordinput) ){
        document.getElementById('wrongnamepassword').style.display='block'
                document.getElementById('wrong-name').style.display='none'
        document.getElementById('wrong-password').style.display='none'
        checklogin();
    }
    else if(usernamestore !== usernameinput ){
        document.getElementById('wrong-name').style.display='block'
        document.getElementById('wrong-password').style.display='none'
        document.getElementById('wrongnamepassword').style.display='none'
        checklogin();

    }
    else if(passwordstore !== passwordinput ){
        document.getElementById('wrong-password').style.display='block'
                document.getElementById('wrong-name').style.display='none'
        document.getElementById('wrongnamepassword').style.display='none'

        checklogin();

    }
    else if((usernamestore === usernameinput) && (passwordstore === passwordinput) ){
        document.getElementById
                document.getElementById('wrong-name').style.display='none'

        document.getElementById('wrong-password').style.display='none'

        document.getElementById('wrongnamepassword').style.display='none'

         document.querySelector("#login-section").style.display='none';
        document.querySelector("#dashboard").style.display='block';
        log =true;
    }
}

// Sign up
document.getElementById('newlog-button').addEventListener('click', showwarn)
function showwarn(){
    let usernameinput= document.querySelector("#login_name").value;
    let passwordinput=document.querySelector("#login_password").value;
    document.getElementById('save-log-warn-pop').style.display='block'
    document.getElementById('overlay').style.display='block'
    document.getElementById("showname").textContent= usernameinput
    document.getElementById("showpassword").textContent= passwordinput
}
document.getElementById('log-confirm').addEventListener('click', newlogin)
function newlogin(){
     localStorage.clear;
    let usernameinput= document.querySelector("#login_name").value;
    let passwordinput=document.querySelector("#login_password").value;
    localStorage.setItem("name",usernameinput)
    localStorage.setItem("password",passwordinput)
     document.querySelector("#login-section").style.display='none';
        document.querySelector("#dashboard").style.display='block';
         document.getElementById('save-log-warn-pop').style.display='none'
    document.getElementById('overlay').style.display='none'
}

// Logout
document.getElementById('logout-button').addEventListener('click', logout)
function logout(){
    document.querySelector("#login-section").style.display='block';
        document.querySelector("#dashboard").style.display='none';
  log = false;
}
// Year Month Progress bar
function progress() {

    let today = new Date();

    // YEAR

    let year = today.getFullYear();

    let startYear = new Date(year,0,1);

    let endYear = new Date(year,11,31);

    let passedDays = (today - startYear) / (1000*60*60*24);

    let totalDays = (endYear - startYear) / (1000*60*60*24) + 1;

    let yearPercent = (passedDays / totalDays) * 100;

    document.getElementById("year-percent").textContent =
    Math.floor(yearPercent) + "%";

    document.getElementById("year-fill").style.width =
    yearPercent + "%";



    // MONTH

    let currentMonth = today.getMonth();

    let startMonth = new Date(year,currentMonth,1);

    let endMonth = new Date(year,currentMonth+1,0);

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
function    updatetime(){
   let now = new Date();
   let date =now.toLocaleDateString("en-GB", {
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric"
   });
   let time = now.toLocaleTimeString("en-US",{
    hour: "2-digit",
    minute: "2-digit"
   })
   document.getElementById("date").textContent=date;
   document.getElementById("time").textContent=time;
   
}
updatetime();
setInterval(updatetime,1000);

// Task Add
document.getElementById("add-task").addEventListener("click", addtask);
function addtask(){
    document.getElementById("overlay").style.display='block'
    document.getElementById("task-add-pop").style.display='block'
}

// Overlay
document.getElementById('overlay').addEventListener('click', overlayfun)
function overlayfun(){
    document.getElementById('overlay').style.display='none'
    let pop = document.querySelectorAll('.popup');
    pop.forEach(element => {
        element.style.display='none'
    });
}