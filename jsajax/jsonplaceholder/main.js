function displayJSON(json) {
  for (i of json) {
    console.log(i)
    para = document.createElement("p");
    para.innerHTML = JSON.stringify(i)
    deletebutton = document.createElement("button");
    deletebutton.onclick = 
    document.body.appendChild(para)
  }
}
fetch('https://my-json-server.typicode.com/ZeddPerm/fakeAPI/posts')

function successMessage() {
  para = document.createElement("p");
  para.innerHTML = "Success";
  document.body.appendChild(para);
}
function postJSON() {
  fetch('https://my-json-server.typicode.com/ZeddPerm/fakeAPI/posts', {
  method: 'POST',
  body: JSON.stringify({
    title: document.getElementById("title").innerHTML,
    body: document.getElementById("body").innerHTML,
    userId: parseInt(document.getElementById("userid").innerHTML),
  }),
  headers: {
    'Content-type': 'application/json; charset=UTF-8',
  },
  })
  .then((response) => response.json())
  .then((json) => successMessage());
}
