function checkValidation() {
    username = document.getElementById("validationServerUsername");
    password = document.getElementById("validationServerPassword");
    ufeedback = document.getElementById("validationServerUsernameFeedback");
    pfeedback = document.getElementById("validationServerPasswordFeedback");
    console.log(username.value.length)
    if (username.value.length <= 3) {
        console.log('ai')
        ufeedback.classList.add("invalid-feedback");
        username.classList.add("is-invalid")
        ufeedback.innerHTML = 'Please choose a username.'
        return false;
    }
    else {
        console.log('aiasdsaasd')
        ufeedback.classList.remove("invalid-feedback");
        ufeedback.classList.add("valid-feedback");
        username.classList.remove("is-invalid")
        username.classList.add("is-valid")
        ufeedback.innerHTML = '';
    }
    if (password.value.length <= 3) {
        console.log('ai')
        pfeedback.classList.add("invalid-feedback");
        password.classList.add("is-invalid")
        pfeedback.innerHTML = 'Please choose a password.'
        return false;
    }
    else {
        pfeedback.classList.add("invalid-feedback");
        pfeedback.classList.remove("invalid-feedback");
        pfeedback.classList.add("valid-feedback");
        password.classList.remove("is-invalid")
        password.classList.add("is-valid")
        ufeedback.innerHTML = ''
    }
    return true;
}
function checkAccount(json) {
    console.log(json)
}
function login() {
    username = document.getElementById("validationServerUsername");
    password = document.getElementById("validationServerPassword");
    if (checkValidation()) {
        console.log(username.value)
        console.log(password.value)
        fetch('https://reqres.in/api/login', {
            method: 'POST',
            body: JSON.stringify({
                email: username.value,
                password: password.value
            }),
            headers: {
                'Content-type': 'application/json; charset=UTF-8',
            },
        })
            .then((response) => response.json())
            .then((json) => checkAccount(json));
    }
}
function register() {
    username = document.getElementById("validationServerUsername");
    password = document.getElementById("validationServerPassword");
    if (checkValidation()) {
        console.log(username.value)
        console.log(password.value)
        fetch('https://reqres.in/api/register', {
            method: 'POST',
            body: JSON.stringify({
                email: username.value,
                password: password.value
            }),
            headers: {
                'Content-type': 'application/json; charset=UTF-8',
            },
        })
            .then((response) => response.json())
            .then((json) => checkAccount(json));
    }
}