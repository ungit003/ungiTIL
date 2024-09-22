const quotes = [
    {
        quote: "The best way to predict the future is to invent it.",
        author: "Alan Kay"
    },
    {
        quote: "Science is not only compatible with spirituality; it is a profound source of spirituality.",
        author: "Carl Sagan"
    },
    {
        quote: "Simplicity is the ultimate sophistication.",
        author: "Leonardo da Vinci"
    },
    {
        quote: "Failure is simply the opportunity to begin again, this time more intelligently.",
        author: "Henry Ford"
    },
    {
        quote: "In the middle of difficulty lies opportunity.",
        author: "Albert Einstein"
    },
    {
        quote: "You can't connect the dots looking forward; you can only connect them looking backwards.",
        author: "Steve Jobs"
    },
    {
        quote: "If you can't explain it simply, you don't understand it well enough.",
        author: "Albert Einstein"
    },
    {
        quote: "Innovation distinguishes between a leader and a follower.",
        author: "Steve Jobs"
    },
    {
        quote: "Success is the sum of small efforts, repeated day in and day out.",
        author: "Robert Collier"
    },
    {
        quote: "What we fear doing most is usually what we most need to do.",
        author: "Tim Ferriss"
    }
];

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");

// new technic : Math
// Math.random() * a : 0~a사이의 숫자 랜덤으로 추출(소수 달렸음)
// Math.round, ceil, floor : 소수 없애는 여러가지 방법
const randomQuotes = quotes[Math.floor(Math.random() * quotes.length)];

quote.innerText = randomQuotes.quote;
author.innerText = randomQuotes.author;