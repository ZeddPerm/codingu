// setTimeout(() =>{console.log("Hello")}, 0);
// alert("World");
// console.log("World");

// // EXERCISE 1: TRANSITION CIRCLE
// document.getElementById("circle").addEventListener('transitionend', setOpacity)
// function animation() {
//     document.getElementById("circle").style.width = "400px";
//     document.getElementById("circle").style.height = "400px";
// }
// function setOpacity() {
//     document.getElementById("text").style.opacity = 1;
// }

// // EXERCISE 2: SHOW NAME ONE LETTER AT A TIME
// var username = prompt("ENTER YOUR NAME");
// for (let letter of username) {
//     const container = document.getElementById('container');
//     container.insertAdjacentHTML('beforeend', '<span class="letter">' + letter + '</span>');
// }
// for (let letterElem of document.getElementsByClassName('letter')) {
//     letterElem.addEventListener('transitionend', setOpacity);
// }
// function setOpacity() {
//     console.log('asiojdhnasuyildy')
//     if (this.nextElementSibling) { this.nextElementSibling.style.opacity = 1; }
// }
// setTimeout(document.getElementsByClassName('letter')[0].style.opacity = 1, 1000);
// window.onload = () => {console.log('asidaisjd');document.getElementsByClassName('letter')[0].style.opacity = 1}

// XML REQUESTS
const xhr = new XMLHttpRequest();
//replace 'my-notes' with any valid string as username in the URL
xhr.open('GET', 'https://jsonplaceholder.typicode.com/todos/1');
xhr.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
    console.log(this.responseText);
    }
}
xhr.send();
