function newDeck() {
    fetch('https://deckofcardsapi.com/api/deck/new/')
        .then((response) => response.json())
        .then((json) => {displayDeckInfo(json)});
}
function displayDeckInfo(json) {
    deckid = document.getElementById("deckid");
    shuffled = document.getElementById("shuffled");
    remaining = document.getElementById("remaining");
    deckid.innerHTML = json["deck_id"]
    shuffled.innerHTML = json["shuffled"]
    remaining.innerHTML = json["remaining"]
    document.getElementById("drawdeckbtn").style.display = "inline"
}
function drawCard() {
    cardscontainer = document.getElementById("cardscontainer")
    deckid = document.getElementById("deckid");
    shuffled = document.getElementById("shuffled");
    remaining = document.getElementById("remaining");
    drawcount = document.getElementById("drawnumber")
    fetch(`https://deckofcardsapi.com/api/deck/${deckid.innerHTML}/draw/?count=${drawcount.value}`)
        .then((response) => response.json())
        .then((json) => {
            remaining.innerHTML = json["remaining"];
            for (let card of json["cards"]) {
                var newcard = document.createElement("img");
                newcard.src = card["image"];
                cardscontainer.appendChild(newcard)
            }
        });
}