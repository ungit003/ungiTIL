// timeout, Date
const clock =  document.querySelector("h2#clock");

function getClock() {
    const date = new Date();
    const hours = String(date.getHours()).padStart(2, "0");
    const minutes = String(date.getMinutes()).padStart(2, "0");
    const seconds = String(date.getSeconds()).padStart(2, "0");
    clock.innerText = `${hours}:${minutes}:${seconds}`

    // 시,분,초 추가
    // clock.innerText = `${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`
}

// 뒤의 숫자는 ms 단위
getClock()
setInterval(getClock, 1000);