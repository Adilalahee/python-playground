function reversestring(mystring){
    const splitstring=mystring.split("");
    const arraystring=splitstring.reverse()
    const stringjoin=arraystring.join("")
    console.log(stringjoin)
    return stringjoin
}
const n=reversestring("hello")
console.log(n)

// function rotateelements(myarray){

// }