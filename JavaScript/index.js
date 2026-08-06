// ways to print in java script

// console api
// console.log("Hello Zain", 4 + 5);
// console.warn("Ye warning hai")
// console.error("Ye error hai")
// alert("No zain");
// click.innerHTML = "Hello Zain";
// document.write("This is document.");

// Javascript variables

// Variable is a container used to store values, data

var number1 = 25;
var number2 = 20;
var number3 = 2.24;
// console.log(number3)
// console.log(number1 + number2);

// Data types in JavaScript

var x = "This is a string";
var z = 'Ye string hai';

//Objects
var marks = {
    ravi: 34,
    zain: 14,
    waliullah: 75
}

// console.log(x, z, marks, number2);

// Booleans

var a = true, b = false;
// console.log(a,b)

var t = undefined;
var u = undefined;
var pak;
// console.log("u = ", u)
// console.log(t)
// console.log("Ye wo variable hai jisko value nhi di hai",pak);

var x = null

// console.log(x)

// Array
// var arr = [32, 52, 62, 'zain'];

/*
There are two types of data types in JavaScript
1. Primitive data types: undefined, null, number, string, boolean, symbol
2. Reference data types: Arrays and objects
*/

// Arithmetic Operators

var val1 = 30, val2 = 40;

// console.log( "a = ", val1, "b = ", val2)
// console.log("a + b = ", val1+val2)
// console.log("a - b = ", val1-val2)
// console.log("a * b = ", val1*val2)
// console.log("a / b = ", val1/val2)

// Assigment Operator

var a = val1, b = val2;
// a +=2;
// b -=2;
// a *=2;
// a /=2;
// console.log(a,b);

// Comparision Operator

// console.log(a==b)
// console.log(a<=b)
// console.log(b>=a)

// Logical Operator

// &&  And operator

// console.log(true && true)
// console.log(true && false)
// console.log(false && false)
// || or operator 
// console.log(true || true)
// console.log(true || false)
// console.log(false || false)

// Logical Not
// console.log(!true);
// console.log(!false);

// Function

// var x = 3, y = 9;
// function avg(a,b){
//     c = (a+b)/2;
//     return c;
// }
// c1 = avg(x,y)
// c2 = avg(20,40)
// console.log(c1,c2)

// Conditions

var age = 149;

// If - else statement

// if(age>20){
//     console.log('Verifies')
// }
// else{
//     console.log('Not Verified')
// }

// If-else Ladder

// if(age<18){
//     console.log('Tum bache ho')
// }
// else if(age>18 && age<50){
//     console.log('Tum bache nhi ho')
// }
// else if(age>=50 && age<=100){
//     console.log('Tum budhe ho')
// }
// else{
//     console.log('Tum immortal ho')
// }

// Loops

let arr = [23, 52, 21, 54];

// For Loop

// for(var i=0; i<arr.length;i++){
//     console.log(arr[i]);
// }

// arr.forEach(function(btn1){
//     console.log(btn1);
// })

// While Loop 

let j = 0;
// while(j<arr.length){
//     console.log(arr[j]);
//     j++;
// }

// Do While Loop

// do{
//     if(arr[j]==21){
//         j++;
//         continue;
            // break;
//     }
//     console.log(arr[j]);
//     j++;
// }while(j<arr.length);

// Array Methods

let myarr=['zain', 'wali', 23,24.5,true,'jamshaid'];
// myarr.pop();
// console.log(myarr.length);
// myarr.push('harry')
// myarr.shift();
// console.log(myarr.unshift('Hamza'))
// myarr.toString()
// myarr.forEach(btn1 => {
//     console.log(btn1);
// });
// d = [2,5,2,5,1,5,0,9,2554,9283,1235,52];
// d.sort();
// d.forEach(btn1 => {
//     console.log(btn1)
// });

// String Method

let strn='Ma zain ho zain';
// console.log(strn.length);
// console.log(strn.indexOf("zain"))
// console.log(strn.lastIndexOf("zain"))
// console.log(strn.slice(3,7))
// console.log(strn.replace("zain","wali","zian","jamshaid"))

// Dates

let mydate = new Date();
// console.log(mydate)
// console.log(mydate.getTime())
// console.log(mydate.getFullYear())
// console.log(mydate.getDay())
// console.log(mydate.getHours())
// console.log(mydate.getMinutes())

// DOM Manipulation
// DOM stand for Document Object Model

// document.getbtnById('click').style.border='2px solid blue';
// document.getbtnById('click').style.background='red'
// let ele = document.getbtnById('click');
// console.log(ele);
// let eleclass = document.getbtnsByClassName("container")
// console.log(eleclass)
// eleclass[0].style.background='red';
// eleclass[0].classList.remove("design");
// console.log(eleclass[0].className);
// eleclass[0].innerHTML
// eleclass[1].classList.add('design')
// console.log(eleclass[1].innerHTML)
// let eletag=document.getbtnsByTagName('h1')
// eletag[0].classList.add('design')
// eletag[0].classList.remove('design')
// let eleid = document.getbtnById('Java')
// eleid.classList.add('design');
// let btn1 = document.querySelector('button')
// btn1.classList.add('design')
// let p = document.querySelector('.container')
// p.classList.remove('design');
// h1 = document.querySelector('#Java')
// h1.classList.add('design')
// let ele = document.querySelectorAll('.container')
// ele[1].classList.toggle('design')
// document.querySelectorAll('*').classList.toggle('dark')
// let allbtns = document.querySelectorAll("*");

// allbtns.forEach(function(btn1) {
//     btn1.classList.toggle("dark");
// });
// bt = document.querySelector('button')
// bt.style.background='red';
// eleclass[0].style.background='red';

// console.log(p)
// p.classList.add('design')
// console.log(p.classList.contains('design')) 

// let p = document.querySelectorAll('.container')
// let ele = document.createbtn('p')
// ele.innerHTML="Ma zain ho"
// p[0].appendChild(ele)
// btn1 = document.createbtn('button')
// btn1.innerHTML='click';
// btn1.style.background='red'
// p[0].appendChild(btn1)
//  bo = document.createbtn('b')
//  bo.innerHTML="Ma bold ho"
//  p[0].replaceChild(bo, btn1)
//  p[0].replaceChild(btn1,ele)
//  p[0].removeChild(btn1)
//  p[0].removeChild(bo)

//  Events

// btn1 = document.querySelector('p')
// function red(){
//     btn1.style.background='red'
// }
// function blue(){
//     btn1.style.background='blue'
// }
// function green(){
//     btn1.style.background='green'
// }
// x = document.querySelectorAll('.container')
// x[0].style.background='green'
function handleclick() {

    if (document.body.style.background != "black") {
        document.body.style.background = "black";
    } else {
        document.body.style.background = "";
    }

}
butn.addEventListener('click', function(){
    sel = document.querySelector('.box')
    box1 =document.createElement('div')
    box1.innerHTML="Box"
    box1.classList.add('tab')
    sel.appendChild(box1)
});
// const btn12 = document.querySelector("button");

// btn12.addEventListener("click", function () {
//     console.log("Click", event, event.target);
//     btn12.style.background='purple'
// });

// btn12.addEventListener("mouseenter", function () {
//     console.log("Mouse andar");
//     btn12.style.background='green'

// });

// btn12.addEventListener("mouseleave", function () {
//     console.log("Mouse bahar");
//     btn12.style.background='blue'

// });
// btn12.addEventListener("dblclick", function () {
//     btn12.style.background='black'

// });
// btn12.addEventListener("onmouseover", function () {
//     btn12.style.background='white'

// });
// window.onload = console.log("Window loaded")
// butn.addEventListener('click', function(){
//     console.log('click howa')
// })
// par1.addEventListener('mouseover', function(event){
//     event.target.style.background='red'
// })
// par1.addEventListener('mouseover', function(){
//     tooltip.style.display='block';
// })
// par1.addEventListener('mouseout', function(event){
//     event.target.style.background='green'
// })
// par1.addEventListener('mouseup', function(event){
//     event.target.style.background=''
// })
// par1.addEventListener('mousedown', function(event){
//     event.target.style.background='red'
// })
// prev =Java.innerHTML;
// Java.addEventListener('mouseup', function(){
// Java.innerHTML=prev;
// })
// Java.addEventListener('mousedown', function(){
// Java.innerHTML="<b> Its hold</b>";
// })

// Arrow Functions

// function sum(a,b){
//     return = a+b;
// }
// sum=(a,b)=>{
//     return = a+b;
// }
// logkro = () =>{
//     console.log("Set timout is used");
// }
//  SetTimout and setinterval

// setTimeout(logkro, 5000);
// fin=setInterval(logkro, 2000);
// Used clearInterval(fin)/clearTimeout(fin) to cancel interval/timeout

// Local Storage

// localStorage.setItem('Name','waliullah')
// localStorage
// Storage { zain: "waliullah", length: 1 }
// localStorage.removeItem('Name')
// localStorage.removeItem('N')
// localStorage.setItem('CGPA', 3.46)


// Json

// obj =  { Name: 'Zain', length: 1, a: {Name: "Waliullah"} };
// jso =JSON.stringify(obj);
// console.log(jso);
// console.log(typeof jso);
// obj = JSON.parse(`{ "Name": "Zain", "length": 1, "a":{"Name": "Waliullah"} }`)
// localStorage.removeItem("zain");
// console.log(parsed);
// JSON.stringify() = Object ➜ JSON.
// JSON.parse() = JSON ➜ Object.

// Backticks

// let name =`Zain
// khan`

// console.log(`My name is ${name}`)