

     function getBoard() {
         fetch('/board', {
            method: 'GET',
            headers: {
                    'pragma': 'no-cache',
                    'cache-control': 'no-cache',
                }
         })
         .then(response => response.text())
         .then(data => {
                 document.getElementById("BoardSection").innerHTML = data;
             })
         .catch((error) => {
             console.error('Error:', error);
            });
     }

     function getCardsInHands() {
         fetch('/cards_in_hands', {
            method: 'GET',
            headers: {
                    'pragma': 'no-cache',
                    'cache-control': 'no-cache',
                }
         })
         .then(response => response.text())
         .then(data => {
                 //console.log('Cards:', data);
                 document.getElementById("CardsInHandSection").innerHTML = data;
             })
         .catch((error) => {
             console.error('Error:', error);
            });
     }

     function showPlayers() {
         fetch('/players', {
            method: 'GET',
            headers: {
                    'pragma': 'no-cache',
                    'cache-control': 'no-cache',
                }
         })
         .then(response => response.text())
         .then(data => {
                 //console.log('Players:', data);
                 document.getElementById("PlayersSection").innerHTML = data;
             })
         .catch((error) => {
             console.error('Error:', error);
            });
     }

     function updateChat() {
         fetch('/system_chat')
         .then(response => response.text())
         .then(data => {
                 document.getElementById("SystemChat").innerHTML = data;
             })
         .catch((error) => {
             console.error('Error:', error);
            });
     }

     function endTurn() {
         fetch('/end_turn')
         .then(response => response.text())
         .then(data => {
                selectedCardId = null;
                document.getElementById("NextTurnBtn").disabled = true;
                show_overlay();
                getBoard();
                getCardsInHands();
                showPlayers();
                updateChat();
             })
         .catch((error) => {
             console.error('Error:', error);
            });
     }


     function missTurn() {
         const data = { cardId: selectedCardId };
         fetch('/miss_turn', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
         })
         .then(response => response.json())
         .then(data => {
                if (data.response == true)
                    document.getElementById("NextTurnBtn").disabled = false;
                getCardsInHands();
             })
         .catch((error) => {
             console.error('Error:', error);
            });
     }

     function rotateCard(cardId, current_playerId) {
         const data = { cardId: cardId, playerId: current_playerId };
            fetch('/rotate_card', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            })

         .then(response => response.text())
         .then(data => {
                getCardsInHands();
             })
         .catch((error) => {
             console.error('Error:', error);
            });
     }

    let selectedCardId = null;
    function selectCard(cardId) {
        document.getElementById("handCardID" + selectedCardId)?.classList.remove("CardHighlight");
        selectedCardId = cardId;
        //console.log(`Selected Card ${cardId}`);
        document.getElementById("handCardID" + cardId).classList.add("CardHighlight");
    }

    function selectField(event) {
        if (selectedCardId !== null) {
            const fieldId = event.target.id;
            //console.log(`Selected Field ${fieldId}`);

            // Отримайте координати рядка і стовпця з fieldId, наприклад, field11
            const coordinates = fieldId.slice(9).split('');
            const row = coordinates[0];
            const column = coordinates[1];

            document.getElementById(fieldId).className="CardHighlight";

            // Відправте POST-запит з даними
            const data = { cardId: selectedCardId, row, column };
            fetch('/verify_move', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            })
            .then(response => response.json())
            .then(data => {
                if (data.response == true)
                    document.getElementById("NextTurnBtn").disabled = false;

                //refresh game data
                getBoard();
                getCardsInHands();
                showPlayers();
            })
            .catch((error) => {
                console.error('Error:', error);
                //refresh game data even there was error during move
                getBoard();
                getCardsInHands();
                showPlayers();
            });
            // Скидання вибору
            selectedCardId = null;
        }
    }
    function selectPlayer(event) {
        if (selectedCardId !== null) {
            const fieldId = event.target.id;

            //Get col and row coordinated from fieldId
            const selectedPlayer = fieldId.slice(6).split('');

            document.getElementById(fieldId).className="PlayerHighlight";

            const data = { PlayerID: selectedPlayer[0], CardID: selectedCardId};
            fetch('/verify_block_move', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            })
            .then(response => response.json())
            .then(data => {
                //console.log('Success:', data);
                if (data.response == true)
                    document.getElementById("NextTurnBtn").disabled = false;
                //refresh game data
                getCardsInHands();
                showPlayers();
            })
            .catch((error) => {
                console.error('Error:', error);
                //refresh game data even there was error during move
                getCardsInHands();
                showPlayers();
            });
            selectedCardId = null;
        }
    }

    function show_overlay(){
        var overlay = document.createElement("div");
        overlay.innerHTML = " <button class='centered-button' type='button' onClick='removeOverlay()' >Next turn!</button>";
        overlay.id = "OverlayId";
        overlay.classList.add("Overlay");
        window.scrollTo(0, 0);
        document.body.append(overlay);
        document.body.classList.add("ScrollBlock");
    }

    function  removeOverlay(){
        document.body.classList.remove("ScrollBlock");
        document.getElementById("OverlayId").remove();
    }

     function endGameRound() {
        var result = window.confirm("Are you sure to end current game round?");
        if (result) {
                window.location.href = '/end_game_round';
            }
     }

     function startNewGame() {
         window.location.href = '/end_game';
     }

     function restartGame() {
         window.location.href = '/restart_game';
     }

//initial input check
var timeoutId;

function delayedValidation() {
    clearTimeout(timeoutId);

    timeoutId = setTimeout(function() {
      validateAndAdjustInput();
    }, 300); // delay 0.3 sec. it user continue to enter characters
             // then it postpone validation to 0.3 sec again and again
  }
function validateAndAdjustInput() {
    var inputValue = document.getElementById('players_number').value;
    var numericValue = parseFloat(inputValue);

    if (isNaN(numericValue)) {
        document.getElementById('players_number').value = 3;
    } else if (numericValue < 3){
        document.getElementById('players_number').value = 3;
    }
     else if (numericValue > 10) {
        document.getElementById('players_number').value = 10;
    }
}