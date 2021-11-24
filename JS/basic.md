#자바스크립트

##즉시 실행함수 IIFE

const a = 7;

(function (){
  console.log(a*2);
})();

(function (){
  console.log(a*2);
}()); //권장

##호이스팅
함수 선언부가 유효범위 최상단으로 끌어올려지는 현상

const b = 8 ;

double()

function double (){
  console.log( b*2);
}

##타이머 함수
 setTimeout(함수,시간): 일정 시간후 함수 실행
 setInterval(함수,시간): 시간 간격마다 함수 실행
 clearTimeout(): 설정된 Timeout 함수를 종료
 clearInterval(): 설정된 Interval 함수를 종료

const timer = setTimeout(()=>{
  console.log('Heropy!')
},3000)

const h1 = document.querySelector('h1');
h1.addEventListener('click',()=>{
  clearTimeout(timer) //timer 종료
})

##callback 
함수의 인수로 사용되는 함수
