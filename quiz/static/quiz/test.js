document.addEventListener("DOMContentLoaded", function() {
    let currentQuestionIndex = 0;
    const questions = JSON.parse(document.getElementById('questions-data').textContent); // Change to match your Django template structure
    const content = document.getElementById('content');
    const btn = document.getElementById('revealBtn');

    function displayQuestion() {
        if (currentQuestionIndex < questions.length) {
            const question = questions[currentQuestionIndex].question_text; // Adjust to match your Django model structure
            const answer = questions[currentQuestionIndex].answer_text; // Adjust to match your Django model structure
            content.innerHTML = `<div class='question'>Question: ${question}</div><div class='answer' style='display: none;'>Answer: ${answer}</div>`;
            btn.textContent = "Reveal Answer";
        } else {
            content.innerHTML = "No more questions.";
            btn.style.display = "none";
        }
    }

    displayQuestion();

    btn.addEventListener("click", function() {
        const answerElement = content.querySelector('.answer');
        if (btn.textContent === "Reveal Answer") {
            answerElement.style.display = "block";
            btn.textContent = "Next Question";
        } else {
            currentQuestionIndex++;
            displayQuestion();
        }
    });
});
