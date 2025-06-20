// Onclick of the button
document.querySelector('input[type="submit"]').onclick = function () {  
    const jumble = document.getElementById("jumbleSolve1").value.trim();
    eel.unScramble(jumble)(function(result){                      
    // Update the div with a random number returned by python
    document.querySelector(".random_number").innerText = result;
  });
  return false;
};