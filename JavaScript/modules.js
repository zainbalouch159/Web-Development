//  let hello = ()=>{
//     console.log("Hello")
// }
// export default hello;
// export function name(user_name){
//     console.log(user_name)
// }
// let zain = {
//     hello: (name)=>{
//         console.log("Hello", name)
//     },
//     greeting: ()=>{
//         console.log("Asslam o alikum")
//     }
// }
// export {zain}

// Rest 

// function show(a,b,c,...other){
//     console.log(a,b,c)
//     console.log(other[0])
//     console.log(arguments)
// }
// show(2,3,5,9,8)

// // Spread

// let name = ["Zain", "Waliullah", "Jamshaid"];
// function show(name1,name2,name3){
//     console.log(name1,name2,name3)
// }
// show(... name);
// show(name);
// show(name[1])

// // In Object
//  let student = {
//     name: "Zain",
//     rollno: 81,
//     section: "q"
//  };
//  let {rollno,...baqia}= student // Destruring & rest
//  console.log(baqia,rollno);

// //  Spread in Object
//  let newstudent= {
//     ...student,
//     rollno: 90
//  }
//  console.log(newstudent)

// Optional chaining / Nullish — ?., ??

//  let student = {
//     name: "Zain",
//     rollno: 81,
//     section: "q"
//  };
//  console.log(student?.name?.city?.village)

//  let arr = [3,2,5]
//  arr = null
//  console.log(arr?.[3])

// Optional Chaining

// let data = ""
// console.log(data||"empty")
// console.log(data??"empty") // to check ?? & 0

// Scopte chain 

//  let name1 = "zain";
//  function outer(){
//     function inner(){
//         console.log(name1);
//     }
//  inner()

//  }
//  outer()

function returnFunc() {
const x = () => {
let a = 1
console.log(a)
const y = () => {
// let a = 2
console.log(a)
const z = () => {
// let a 3
console.log(a)
}
z()
}
a = 999
y()
}
x()
}
let a =returnFunc
a()
// returnFunc()