// Onclick of the button
// document.querySelector('input[type="submit"]').onclick = function () {  
//     const jumble = document.getElementById("jumbleSolve1").value.trim();
//     eel.unScramble(jumble)(function(result){                      
//     // Update the div with a random number returned by python
//     document.querySelector(".random_number").innerText = result;
//   });
//   return false;
// };

function setupUnscramble(btnId, inputId, resultId){
    document.getElementById(btnId).onclick = function(){
        const jumble = document.getElementById(inputId).value.trim();
        eel.unScramble(jumble)(function(result){
            document.getElementById(resultId).innerText = result;
        });
    };
}

setupUnscramble("btn1", "jumble1", "result1");
setupUnscramble("btn2", "jumble2", "result2");
setupUnscramble("btn3", "jumble3", "result3");
setupUnscramble("btn4", "jumble4", "result4");
