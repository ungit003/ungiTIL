// 랜덤 이미지 불러오기 := 명언이랑 거의 비슷함.
const images = [
    "0.jpg",
    "1.jpg",
    "2.jpg",
    "3.jpg",
]

const chosenImage = images[Math.floor(Math.random() * images.length)];
// 짜스에서 html을 만들어서 추가하기.
const bgImage = document.createElement("img");

bgImage.src = `pics/${chosenImage}`;

document.body.appendChild(bgImage);