let user={
    name: "Zain",
    rollno: 81
};
localStorage.setItem('users',JSON.stringify(user))
obj=JSON.parse(localStorage.getItem("users"));
console.log(obj.name)
console.log(obj.rollno)

data={
    name: "Waliullah",
    rollno: 88
};
localStorage.setItem('student',JSON.stringify(data))

value={
    name: "Jamshaid",
    rollno: 90
};
localStorage.setItem("student1",JSON.stringify(value))
obj=JSON.parse(localStorage.getItem("student1"));
console.log(obj.name)
console.log(obj.rollno);

student={
    name: "Kaief",
    rollno: 84
}
localStorage.setItem("student3",JSON.stringify(student));
obj=JSON.parse(localStorage.getItem("student3"))
console.log(obj.name)
console.log(obj.rollno)