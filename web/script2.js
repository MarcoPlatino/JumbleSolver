const circleChars = JSON.parse(sessionStorage.getItem("circleChars") || "[]");
console.log(circleChars);

document.getElementById(submitAmount).onclick = function(){
    selectElement = document.querySelector('#select1');
    choice = selectElement.value();
    }
