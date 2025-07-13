document.addEventListener("DOMContentLoaded", function() {
  const questions = [
    { name: "gender", question: "What is your gender?", options: ["Male", "Female"] },
    { name: "part_time_job", question: "Have you done part-time job?", options: ["Yes", "No"] },
    { name: "absence_days", question: "How many days were you absent?", input: "number" },
    { name: "extracurricular_activities", question: "Do you do extracurricular activities?", options: ["Yes", "No"] },
    { name: "weekly_self_study_hours", question: "How many hours do you study weekly?", input: "number" },
    { name: "math_score", question: "What is your Math score?", input: "number" },
    { name: "science_score", question: "What is your Science score?", input: "number" },
    { name: "social_score", question: "What is your Social score?", input: "number" },
    { name: "nepali_score", question: "What is your Nepali score?", input: "number" },
    { name: "account_score", question: "What is your Account score?", input: "number" },
    { name: "english_score", question: "What is your English score?", input: "number" },
    { name: "eph_score", question: "What is your EPH score?", input: "number" }
  ];

  let currentQuestion = 0;
  const answers = {};

  const startBtn = document.getElementById("start-btn");
  const startScreen = document.getElementById("start-screen");
  const quizForm = document.getElementById("quiz-form");
  const questionCountEl = document.getElementById("question-count");
  const questionTextEl = document.getElementById("question-text");
  const optionsContainer = document.getElementById("options-container");
  const nextBtn = document.getElementById("next-btn");
  const doneBtn = document.getElementById("done-btn");

  startBtn.addEventListener("click", () => {
    startScreen.style.display = "none";
    quizForm.style.display = "block";
    renderQuestion();
  });

  function calculateScores() {
    const scoreKeys = ["math_score", "science_score", "social_score", "nepali_score", "account_score", "english_score", "eph_score"];
    let total = 0;
    let count = 0;
    scoreKeys.forEach(key => {
      const val = parseFloat(answers[key]);
      if (!isNaN(val)) {
        total += val;
        count++;
      }
    });
    answers["total_score"] = total.toFixed(2);
    answers["average_score"] = count > 0 ? (total / count).toFixed(2) : "0.00";
  }

  function renderQuestion() {
    const q = questions[currentQuestion];
    questionCountEl.textContent = `Question ${currentQuestion + 1} of ${questions.length}`;
    questionTextEl.textContent = q.question;
    optionsContainer.innerHTML = "";

    if (q.options) {
      q.options.forEach(option => {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "option-btn";
        btn.textContent = option;
        // If previously answered, show selected
        if (answers[q.name] && answers[q.name].toLowerCase() === option.toLowerCase()) {
          btn.classList.add("selected");
        }
        btn.addEventListener("click", () => {
          answers[q.name] = option.toLowerCase();
          highlightSelected(btn);
        });
        optionsContainer.appendChild(btn);
      });
    } else if (q.input === "number") {
      const input = document.createElement("input");
      input.type = "number";
      input.name = q.name;
      input.className = "form-control";
      input.required = true;
      input.value = answers[q.name] || "";
      input.addEventListener("input", () => {
        answers[q.name] = input.value;
        if (q.name.includes("score")) {
          calculateScores();
        }
      });
      optionsContainer.appendChild(input);
    }
  }

  function highlightSelected(selectedBtn) {
    const buttons = optionsContainer.querySelectorAll("button");
    buttons.forEach(btn => btn.classList.remove("selected"));
    selectedBtn.classList.add("selected");
  }

  nextBtn.addEventListener("click", (e) => {
    e.preventDefault();

    // Validation: for buttons, must select one option; for input, must fill it
    const q = questions[currentQuestion];
    if (q.options) {
      if (!answers[q.name]) {
        alert("Please select an option to continue.");
        return;
      }
    } else if (q.input === "number") {
      const val = answers[q.name];
      if (!val || isNaN(val) || val === "") {
        alert("Please enter a valid number.");
        return;
      }
    }

    if (currentQuestion < questions.length - 1) {
      currentQuestion++;
      renderQuestion();
    } else {
      questionCountEl.textContent = "";
      questionTextEl.innerHTML = "<h4>All questions done!</h4>";
      optionsContainer.innerHTML = "";

      // Add hidden inputs with all answers to form
      for (const key in answers) {
        const input = document.createElement("input");
        input.type = "hidden";
        input.name = key;
        input.value = answers[key];
        quizForm.appendChild(input);
      }

      nextBtn.style.display = "none";
      doneBtn.style.display = "inline-block";
    }
  });

});
