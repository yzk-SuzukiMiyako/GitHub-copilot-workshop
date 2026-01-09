// FizzBuzz: 1～20 を出力
for(let i=1;i<=20;i++){
  let out = '';
  if(i%3===0) out+='Fizz';
  if(i%5===0) out+='Buzz';
  console.log(out||i);
}
