const startButton = document.querySelector('.start'); 
const stopButton = document.querySelector('.stop');
const resetButton = document.querySelector('.reset');
const deleteButton = document.querySelector('.delete');
const timeDisplay = document.querySelector('.time');
const lapList = document.querySelector('.lap-list');

let timerInterval;
let isRunning = false;
let milliseconds = 0;
let seconds = 0;
let laps = [];

const circle1 = document.querySelector('.check');  
const circleElements = [];  

circle1.classList.add('ri-checkbox-blank-circle-line');  
circle1.addEventListener('click', () => {
    const isChecked = circle1.classList.contains('ri-checkbox-circle-line');
    
    circleElements.forEach(circle => {
        if (!isChecked) {
            circle.classList.add('ri-checkbox-circle-line');
            circle.classList.remove('ri-checkbox-blank-circle-line');
        } else {
            circle.classList.remove('ri-checkbox-circle-line');
            circle.classList.add('ri-checkbox-blank-circle-line');
        }
    });

    updateCircle1State();
});

startButton.addEventListener('click', () => {
    if (!isRunning) {
        timerInterval = setInterval(updateTime, 10); 
        isRunning = true;
        startButton.disabled = true; 
        stopButton.disabled = false; 
    }
});

stopButton.addEventListener('click', () => {
    clearInterval(timerInterval);
    isRunning = false;
    startButton.disabled = false;
    stopButton.disabled = true;

    const lapTime = formatTime(seconds, milliseconds);
    const lapItem = document.createElement('li');
    lapItem.classList.add('lap-item');
    lapItem.style.justifyContent = 'space-between';

    const circle2 = document.createElement('span');
    circle2.classList.add('circle', 'ri-checkbox-blank-circle-line'); 
    circleElements.push(circle2);
    circle2.style.cursor = 'pointer';

    circle2.addEventListener('click', () => {
        circle2.classList.toggle('ri-checkbox-circle-line');  
        circle2.classList.toggle('ri-checkbox-blank-circle-line');  
        updateCircle1State();  
    });

    const lapTimeSpan = document.createElement('span');
    lapTimeSpan.classList.add('lap-time');
    lapTimeSpan.textContent = lapTime;

    lapItem.appendChild(circle2);  
    lapItem.appendChild(lapTimeSpan);
    lapList.appendChild(lapItem);
    laps.push(lapTime);

    updateCircle1State();  
});

function updateCircle1State() {
    const allChecked = circleElements.every(circle => circle.classList.contains('ri-checkbox-circle-line'));
    if (allChecked) {
        circle1.classList.add('ri-checkbox-circle-line');
        circle1.classList.remove('ri-checkbox-blank-circle-line');
    } else {
        circle1.classList.remove('ri-checkbox-circle-line');
        circle1.classList.add('ri-checkbox-blank-circle-line');
    }
}

function updateTime() {
    milliseconds++;
    if (milliseconds >= 100) {
        milliseconds = 0;
        seconds++;
    }
    timeDisplay.textContent = formatTime(seconds, milliseconds);
}

function formatTime(seconds, milliseconds) {
    return `${padZero(seconds)}:${padZero(milliseconds)}`;
}

function padZero(number) {
    return number < 10 ? `0${number}` : number;
}

function resetTimer() {
    clearInterval(timerInterval);
    isRunning = false;
    milliseconds = 0;
    seconds = 0;
    timeDisplay.textContent = formatTime(seconds, milliseconds);
}

function deleteLap() {
    const checkedCircles = document.querySelectorAll('.ri-checkbox-circle-line');  
    checkedCircles.forEach(circle => {
        const lapItem = circle.closest('li');  
        if (lapItem) {
            lapItem.remove();  
        }
    });

    updateCircle1State();  
}

circle1.style.cursor = 'pointer';
resetButton.addEventListener('click', resetTimer); 
deleteButton.addEventListener('click', deleteLap); 

