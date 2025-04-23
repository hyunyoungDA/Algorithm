const fs = require('fs');
const input = Number(fs.readFileSync("/dev/stdin").toString().trim());


const fibo = (num) =>{
    if (num === 0){
        return 0;
    } if (num === 1){
        return 1;
    } 
    return fibo(num - 1) + fibo(num - 2);
} 

const result = fibo(input);
console.log(result);