
// Prototype
// let car ={
//     name : "Honda",
//     model : 2021,
//     showname: function(){
//         console.log("You car name is", this.name)
//     },
// }

// let details = {
//     company_name: "FAZS",
//     showsalary(){
//         console.log(this.salary)
//     },
// }

// let zain = {
//     salary: 20000,
//     company_name: "USP",
// }
// zain.__proto__= details

// Classes & Objects
class car{
    constructor(){
        console.log("Construct invoked")
    }
    start(){
        console.log("Car started")
    }
    stop(){
        console.log("Car stopped")
    }
    nameshow(){
        console.log(this.name)
    }
    setname(name){
        this.name= name
    }
}
honda = new car()
honda.setname("zain")
toyota = new car()
// // // // // class parent{
// // // // //     constructor(){
// // // // //         console.log("parent class constructor");
// // // // //     }
// // // // //     showname(){
// // // // //         console.log("parent class");
// // // // //     }
// // // // // } 
// // // // // class child extends parent{
// // // // //      constructor(){
// // // // //         super();
// // // // //         console.log("child class constructor");
// // // // //     }
// // // // //     childname(){
// // // // //         super.showname(); 
// // // // //         console.log("child class");
// // // // //     }
// // // // // }
// // // // // let obj = new child();

// // // // // Call back

// // // // // function sum(a,b){
// // // // //     console.log(a+b);
// // // // // }
// // // // // function add(a,b,plus){
// // // // //     plus(a,b);
// // // // // }
// // // // // add(10,20,sum);
// // // // // Callback hell
// // // //  function getdata(id,nextdata){
// // // //     setTimeout(()=>{
// // // //     console.log("id: ", id)
// // // //     if(nextdata){
// // // //         nextdata();
// // // //     }
// // // // },2000);
// // // // }
// // // // getdata(1,()=>{
// // // //     getdata(2,()=>{
// // // //         getdata(3);
// // // //     });
// // // // })
// // // // //  Async Wait
// // // let promise = new Promise((resolve,reject)=>{
// // //     console.log("promise is pending");
// // //     resolve("promise resolved");
// // //     // reject("promise is rejected");
// // // });

// // // promise.then((res)=>{
// // //     console.log(res, "then method is called");
// // // }).catch((rej)=>{
// // //     console.log("catch method is called",rej);
// // // });

// // async function getdata(){
// //     return new Promise((resolve,reject)=>{
// //         setTimeout(()=>{
// //             console.log("data is fetched");
// //             resolve("data is resolved");
// //             // reject("data is rejected");
// //         },2000);

// async function getdata1(datano){
//     return new Promise((resolve,reject)=>{
//         console.log("Pending..")
//         setTimeout(()=>{
//             console.log('Data ', datano)
//             resolve("resolve")
//         },5000)
//         // setTimeout(()=>{
//         //     console.log("Pending")
//         //     reject("rejected")
//         // },2000)
//     })}
// // async function getdata2(){
// //     return new Promise((resolve,reject)=>{
// //         console.log("Pending....")
// //         setTimeout(()=>{
// //             resolve("resolve")
// //         },5000)
// //         // setTimeout(()=>{
// //         //     console.log("Pending")
// //         //     reject("rejected")
// //         // },2000)
// //     })}
// //     getdata1().then((res)=>{
// //         console.log("Data 1 is ", res)
// //         getdata2().then((res)=>{

// //             console.log("Data 2 is ", res)
// //         })
// //     })
    
//     // console.log("last")

//     getdata1(1)
//     .then((res)=>{
//         console.log(res)
//         return getdata1(2)
//     })
// function zain(){
//     console.log("Zain Khan")
// }
// zain= ()=>{
//     console.log("Zain Balouch")
// }
// zain= ()=>{
//     console.log("Zain Balouch3")
// }
// // zain()

// zain()

// async function data(datano) {
//     return new Promise((haal)=>{
//         console.log("Pending.. ")
//         setTimeout(()=>{
//             console.log("Data ", datano)
//             haal("Kamyab")
//         },2000)
//     })
// }
// data(1).then((res)=>{
//     console.log(res)
//     return data(2)
// }).then((sol)=>{
//     console.log(sol)
// })
// Promise Chain
// data(1).then((sol)=>{
//     console.log("Data 1 is resolved",sol)
//     return data(2)
// }).then((sol)=>{
//     console.log("Data 2 is resolved",sol)
//     return data(3)
// }).then((sol)=>[
//     console.log("Zain",sol)
// ])
// assync await>> Promise chain>> callback hell

async function data(value) {
    return new Promise ((sol)=>{
        console.log("Pending...")
        setTimeout(()=>{
            console.log("Value ", value ,"is resolved")
            sol("Solved")
        },2000)
    })
}
async function showdata(){
    await data(1)
    await data(2)
    console.log("wow")
    await data(3)
    console.log("lol")
}
showdata()

