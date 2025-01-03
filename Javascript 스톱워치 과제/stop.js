// 요소 선택
const startButton = document.querySelector('.start'); 
const stopButton = document.querySelector('.stop'); // 단일 버튼만 사용
const resetButton = document.querySelector('.reset');
const checkButton = document.querySelector('.check');
const deleteButton = document.querySelector('.delete');
const timeDisplay = document.querySelector('.time');
const lapList = document.querySelector('.lap-list');

let timerInterval;
let isRunning = false;
let milliseconds = 0;
let seconds = 0;
let laps = [];

// 타이머 시작/정지
startButton.addEventListener('click', () => {
    if (!isRunning) {
        timerInterval = setInterval(updateTime, 10); // 10ms마다 타이머 업데이트
        isRunning = true;
        startButton.disabled = true; // start 버튼 비활성화
        stopButton.disabled = false; // stop 버튼 활성화
    }
});

// 타이머 정지
stopButton.addEventListener('click', () => {
    clearInterval(timerInterval);
    isRunning = false;
    startButton.disabled = false; // start 버튼 활성화
    stopButton.disabled = true; // stop 버튼 비활성화

    const lapTime = formatTime(seconds, milliseconds);
    const lapItem = document.createElement('li');
    lapItem.textContent = lapTime;
    lapList.appendChild(lapItem);
    laps.push(lapTime);
});


// 타이머 업데이트
function updateTime() {
    milliseconds++;
    if (milliseconds >= 100) {  // 100ms가 지나면 1초가 됨
        milliseconds = 0;
        seconds++;
    }
    timeDisplay.textContent = formatTime(seconds, milliseconds);
}

// 시간을 "mm:ss" 형식으로 표시
function formatTime(seconds, milliseconds) {
    return `${padZero(seconds)}:${padZero(milliseconds)}`;
}

// 1자리 숫자를 두 자리로 포맷 (ex: 5 -> 05)
function padZero(number) {
    return number < 10 ? `0${number}` : number;
}

// 타이머 리셋
function resetTimer() {
    clearInterval(timerInterval);
    isRunning = false;
    milliseconds = 0;
    seconds = 0;
    timeDisplay.textContent = formatTime(seconds, milliseconds);
}

// 구간 기록 삭제
function deleteLap() {
    lapList.innerHTML = ''; // 구간 기록 리스트 초기화
    laps = []; // 배열 초기화
}

// 이벤트 리스너 설정
resetButton.addEventListener('click', resetTimer); // 리셋 버튼 기능
checkButton.addEventListener('click', addLap); // 구간 기록 버튼 기능
deleteButton.addEventListener('click', deleteLap); // 구간 기록 삭제 버튼 기능
