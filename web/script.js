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

const input1 = document.getElementById("jumble1");
const buttonsContainer1 = document.getElementById("char-buttons1");

input1.addEventListener("input", () => {
    // Clear existing buttons
    buttonsContainer1.innerHTML = "";

    // Split text into characters
    const chars = input1.value.split("");

    // Create button for each character
    chars.forEach((char, index) => {
        const btn = document.createElement("button");
        btn.className = "char-btn";
        btn.textContent = char;
        btn.onclick = () => alert(`You clicked character ${index + 1}: '${char}'`);
        buttonsContainer1.appendChild(btn);
    });
});