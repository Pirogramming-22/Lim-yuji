let attempts = 9;
let correctNumbers = generateRandomNumbers();
let gameEnded = false;

const resultDiv = document.getElementById('results');
const gameResultImg = document.getElementById('game-result-img');

let resultHistory = [];

function resetGame() {
    attempts = 9;
    document.getElementById('attempts').textContent = attempts;
    correctNumbers = generateRandomNumbers();

    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = ''; 

    document.getElementById('results').textContent = '';
    document.getElementById('game-result-img').style.display = 'none';
    document.getElementById('success-message').style.display = 'none';
    
    resultHistory = [];

    gameEnded = false;
    document.querySelector('.submit-button').disabled = false;
}

function generateRandomNumbers() {
    let numbers = [];
    while (numbers.length < 3) {
        const num = Math.floor(Math.random() * 10);
        if (!numbers.includes(num)) {
            numbers.push(num);
        }
    }
    return numbers;
}

function check_numbers() {
    if (gameEnded) return;

    const number1 = document.getElementById('number1').value;
    const number2 = document.getElementById('number2').value;
    const number3 = document.getElementById('number3').value;

    if (number1 === "" || number2 === "" || number3 === "") {
        document.getElementById('number1').value = '';
        document.getElementById('number2').value = '';
        document.getElementById('number3').value = '';
        document.querySelector('.submit-button').disabled = true;
        return;
    }
    document.querySelector('.submit-button').disabled = false;

    const userNumbers = [parseInt(number1), parseInt(number2), parseInt(number3)];

    let strikeCount = 0;
    let ballCount = 0;

    const checkNumber = new Set();

    userNumbers.forEach((num, index) => {
        if (num === correctNumbers[index]) {
            strikeCount++;
            checkNumber.add(index);
       }
    });

    userNumbers.forEach((num, index) => { 
        if (num !== correctNumbers[index] && correctNumbers.includes(num)) {
            const targetNumber = correctNumbers.indexOf(num);
            if (!checkNumber.has(targetNumber)) {
                ballCount++;
                checkNumber.add(targetNumber);
            }
        }
    });

    let result = `${userNumbers.join('')} : `; 
    if (strikeCount === 0 && ballCount === 0) {
        result += `<span class="num-result out">O</span>`;
    } else {
        result += `<span class="num-result strike">${strikeCount} S</span><span class="num-result ball">${ballCount} B</span>`;
        }
    resultHistory.unshift(result);
    const resultBox = `<div style="margin-bottom: 20px;">${userNumbers.join('')} : ${result}</div>`;
    resultDiv.innerHTML += resultBox;

    document.getElementById('results').innerHTML = resultHistory.join('<br>');
    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = '';
    attempts--;
    document.getElementById('attempts').textContent = attempts;

    if (strikeCount === 3) {
        document.getElementById('game-result-img').src = 'success.png';
        document.getElementById('game-result-img').style.display = 'block';
        document.querySelector('.submit-button').disabled = true;
        gameEnded = true;
    } else if (attempts === 0) {
        document.getElementById('game-result-img').src = 'fail.png';
        document.getElementById('game-result-img').style.display = 'block';
        document.querySelector('.submit-button').disabled = true;
        gameEnded = true; 
    } 
}
