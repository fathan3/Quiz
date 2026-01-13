let currentIndex = 0;
let answers = [];

// DOM elements
const container = document.getElementById('flashcard-container');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');
const guestNameInput = document.getElementById('guest_name');

const modal = document.getElementById("score-modal");
const closeModal = document.getElementById("close-modal");
const scoreText = document.getElementById("score-text");

// Inisialisasi jawaban
quizCards.forEach(card => answers.push({id: card.id, selected: ''}));

function renderCard(index){
    const card = quizCards[index];

    container.classList.remove('fade-in');
    container.classList.add('fade-out');

    setTimeout(() => {
        container.innerHTML = `
            <p><strong>Question ${index + 1}:</strong> ${card.question}</p>
            <div>
                <label><input type="radio" name="q${card.id}" value="A" ${answers[index].selected==='A'?'checked':''}> ${card.option_a}</label><br>
                <label><input type="radio" name="q${card.id}" value="B" ${answers[index].selected==='B'?'checked':''}> ${card.option_b}</label><br>
                <label><input type="radio" name="q${card.id}" value="C" ${answers[index].selected==='C'?'checked':''}> ${card.option_c}</label><br>
                <label><input type="radio" name="q${card.id}" value="D" ${answers[index].selected==='D'?'checked':''}> ${card.option_d}</label><br>
            </div>
        `;
        container.classList.remove('fade-out');
        container.classList.add('fade-in');
    }, 200);

    prevBtn.disabled = index === 0;
    nextBtn.textContent = index === quizCards.length - 1 ? "Submit" : "Next";
}

// Update jawaban saat memilih
container.addEventListener('change', function(e){
    if(e.target.name.startsWith('q')){
        answers[currentIndex].selected = e.target.value;
    }
});

// Tombol Previous
prevBtn.onclick = () => {
    if(currentIndex > 0){
        currentIndex--;
        renderCard(currentIndex);
    }
};

// Tombol Next / Submit
nextBtn.onclick = () => {
    // Validasi jawaban sebelum lanjut
    if(!answers[currentIndex].selected){
        alert("Please select an answer before proceeding!");
        return;
    }

    if(currentIndex < quizCards.length - 1){
        currentIndex++;
        renderCard(currentIndex);
    } else {
        // Validasi semua jawaban sebelum submit
        const unanswered = answers.find(a => a.selected === '');
        if(unanswered){
            alert("You must answer all questions before submitting!");
            return;
        }
        submitQuiz();
    }
};

// Submit quiz ke backend
function submitQuiz(){
    const guest_name = guestNameInput.value || 'Guest';
    fetch('/submit_quiz', {   
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({answers: answers, guest_name: guest_name})
    })
    .then(res => res.json())
    .then(data => {
        scoreText.textContent = `${guest_name}, Your Score: ${data.score} / ${quizCards.length}`;
        modal.style.display = "block";
    });
}

// Modal close
closeModal.onclick = () => { modal.style.display = "none"; };
window.onclick = (event) => { if(event.target === modal) modal.style.display = "none"; };

// Render card pertama
renderCard(currentIndex);
