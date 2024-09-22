// 날씨 만들기
// step.1 내 위치 찾기.
// openweather에서 url 따오기.
// 정보 뒤져서 가져오기.

function onGeoOk(position) {
    const lat = position.coords.latitude;
    const lng = position.coords.longitude;
    // console.log("you are living in", lat, lng);
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=35.0978048&lon=128.9158656&appid=4550cd60b616922bfc82766893b061dd&units=metric`;
    // console.log(url);
    fetch(url)
        .then(response => response.json())
        .then((data) => {
            const weather = document.querySelector("#weather span:first-child");
            const city = document.querySelector("#weather span:last-child");
            city.innerText = data.name;
            weather.innerText = `${data.weather[0].main} / ${data.main.temp}'C`;
        });
}

function onGeoError() {
    alert("can't find you.")
}

navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError);
