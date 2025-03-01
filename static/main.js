document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const spinner = document.getElementById("spinner");
    const button = document.querySelector(".button");
  
    form.onsubmit = function () {
      const inputs = document.querySelectorAll("input, select");
      let valid = true;
  
      inputs.forEach((input) => {
        if (input.value === "" || input.value === null) {
          valid = false;
        }
      });
  
      if (!valid) {
        alert("⚠️ Please enter all the fields properly!");
        return false; // Stop Form Submission
      }
  
      spinner.style.display = "block";
      button.disabled = true;
      button.innerHTML = "Predicting...⏳";
  
      setTimeout(() => {
        spinner.style.display = "none";
        button.disabled = false;
        button.innerHTML = "🚀 PREDICT NOW";
      }, 3000);
    };
  });
  


