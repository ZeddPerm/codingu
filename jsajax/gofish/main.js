// get a new shuffled deck
var deck = {}
var deckid = ""
fetch('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
    .then((response) => response.json())
    .then((json) => {
        deckid = json["deck_id"];
        // deal 7 cards to a player
        fetch(`https://deckofcardsapi.com/api/deck/${json["deck_id"]}/draw/?count=7`)
            .then((response) => response.json())
            .then((json) => {
                var startinghand = ""
                for (var i of json['cards']) {
                    var newcard = document.createElement("img");
                    newcard.src = i["image"];
                    document.body.appendChild(newcard)
                    startinghand = startinghand + i["code"] + ','
                }
                document.body.appendChild(document.createElement("br"));
                fetch(`https://deckofcardsapi.com/api/deck/${json["deck_id"]}/pile/player1/add/?cards=${startinghand}`)
                    .then((response) => response.json())
                    .then((json) => {
                        console.log('a', json);
                    });
            });
        // deal 7 cards to a player
        fetch(`https://deckofcardsapi.com/api/deck/${json["deck_id"]}/draw/?count=7`)
            .then((response) => response.json())
            .then((json) => {
                startinghand = ""
                for (var i of json['cards']) {
                    var newcard = document.createElement("img");
                    newcard.src = i["image"];
                    document.body.appendChild(newcard);
                    startinghand = startinghand + i["code"] + ','
                }
                fetch(`https://deckofcardsapi.com/api/deck/${json["deck_id"]}/pile/player2/add/?cards=${startinghand}`)
                    .then((response) => response.json())
                    .then((json) => {
                        console.log('a', json);
                    });
            });
    });
function player1Fish() {
    var hascard = false
    fetch(`http://deckofcardsapi.com/api/deck/${deckid}/pile/player1/list/`)
        .then((response) => response.json())
        .then((json) => {
            console.log(json)
            // check if player 1 has one of the card they are requesting
            var p1req = document.getElementById("player1req");
            for (var card of json["piles"]["player1"]["cards"]) {
                if (card["value"] == p1req.value) {
                    hascard = true;
                }
            }
            // cancel req if player 1 doesnt have card
            if (hascard == false) {
                console.log("you must have card to request it");
                return;
            }
            fetch(`http://deckofcardsapi.com/api/deck/${deckid}/pile/player2/list/`)
                .then((response) => response.json())
                .then((json) => {
                    var hascard = false
                    // check if player 2 has one of the card they are requesting
                    var p1req = document.getElementById("player1req");
                    for (var card of json["piles"]["player1"]["cards"]) {
                        if (card["value"] == p1req.value) {
                            
                        }
                    }
                });
        });
}
