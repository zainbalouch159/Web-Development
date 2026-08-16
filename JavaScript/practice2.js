// class parent{
//     constructor(){
//         console.log("parent class constructor");
//     }
//     showname(){
//         console.log("parent class");
//     }
// } 
// class child extends parent{
//     constructor(){
//         super();
//         console.log("child class constructor");
//     }
//     childname(){
//         super.showname(); 
//         console.log("child class");
//     }
// }
// let obj = new child();

// Call back

function sum(a,b){
    console.log(a+b);
}
function add(a,b,plus){
    plus(a,b);
}
add(10,20,sum);
//  Async Wait
