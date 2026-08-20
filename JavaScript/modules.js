 let hello = ()=>{
    console.log("Hello")
}
export default hello;
export function name(user_name){
    console.log(user_name)
}
let zain = {
    hello: (name)=>{
        console.log("Hello", name)
    },
    greeting: ()=>{
        console.log("Asslam o alikum")
    }
}
export {zain}