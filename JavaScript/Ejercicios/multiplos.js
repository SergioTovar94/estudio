/**
 * Problema 1: Múltiplos de 3 o 5
 * Si enumeramos todos los números naturales menores de 10 que son múltiplos de 3 o 5, obtenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23.
 * Encuentre la suma de todos los múltiplos de 3 o 5 debajo del valor del parámetro proporcionado number.
*/
function multiplesOf3Or5(number) {
  let x = 0;
  for (let i = 0; i<(number);i++){
    if(i%3==0 || i%5 ==0){
      x+=i;
    }
  }
  return x;
}

console.log(multiplesOf3Or5(1000));