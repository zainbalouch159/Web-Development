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
