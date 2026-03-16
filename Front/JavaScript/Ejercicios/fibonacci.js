/**
 * Problema 2: Números de Fibonacci pares
 * Cada nuevo término de la secuencia de Fibonacci se genera sumando los dos términos anteriores. Al comenzar con 1 y 2, los primeros 10 términos serán:
 * 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
 * Considerando los términos de la secuencia de Fibonacci cuyos valores no exceden n, encuentre la suma de los términos de valor par.
 */

function fiboEvenSum(n) {
  let i = 1;
  let j = 0;
  let r = 0;
  let result = 0;
  while (r<n){

    j=r;
    r+=i;
    i=j;
    if (r%2==0){
      result+=r;
      }
  }
  console.log(result)
  return result;
}

fiboEvenSum(10)