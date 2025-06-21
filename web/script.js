const circleChars = [];

function setupUnscramble(btnId, inputId, resultId, charButtonsId) {
  document.getElementById(btnId).onclick = function () {
    const jumble = document.getElementById(inputId).value.trim();
    eel.unScramble(jumble)(function (possibilities) {
      const resultDiv = document.getElementById(resultId);
      const charButtonsDiv = document.getElementById(charButtonsId);
      resultDiv.innerHTML = "";
      charButtonsDiv.innerHTML = "";

      if (!possibilities || possibilities.length === 0) {
        resultDiv.innerText =
          "You must have made a mistake; there are no words with these letters...";
        return;
      }

      possibilities.forEach((word) => {
        const wordBtn = document.createElement("button");
        wordBtn.className = "reg-btn";
        wordBtn.textContent = word;
        wordBtn.type = "button";
        wordBtn.onclick = () => {
        charButtonsDiv.innerHTML = "";

          word.split("").forEach((char) => {
            const btn = document.createElement("button");
            btn.className = "char-btn";
            btn.textContent = char;
            btn.type = "button";

            btn.onclick = () => {
              btn.classList.toggle("toggled");

              if (btn.classList.contains("toggled")) {
                circleChars.push(char);
              } else {
                const index = circleChars.indexOf(char);
                if (index > -1) circleChars.splice(index, 1);
              }

              eel.solve(circleChars);
            };

            charButtonsDiv.appendChild(btn);
          });
        };
        resultDiv.appendChild(wordBtn);
      });
    });
  };
}

setupUnscramble("btn1", "jumble1", "result1", "char-buttons1");
setupUnscramble("btn2", "jumble2", "result2", "char-buttons2");
setupUnscramble("btn3", "jumble3", "result3", "char-buttons3");
setupUnscramble("btn4", "jumble4", "result4", "char-buttons4");

document.querySelector('.big-btn').onclick = function() {
    sessionStorage.setItem("circleChars", JSON.stringify(circleChars));
};