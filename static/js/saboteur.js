     function getBoard() {
         fetch('/board')
         .then(response => response.text())
         .then(data => {
                 document.getElementById("BoardSection").innerHTML = data;
             })
         .catch((error) => {
             console.error('Error:', error);
            });
     }

     function getCardsInHands() {
         fetch('/cards_in_hands')
         .then(response => response.text())
         .then(data => {
                 document.getElementById("CardsInHandSection").innerHTML = data;
             })
         .catch((error) => {
             console.error('Error:', error);
            });
     }

     function showPlayers() {
         fetch('/players')
         .then(response => response.text())
         .then(data => {
                 document.getElementById("PlayersSection").innerHTML = data;
             })
         .catch((error) => {
             console.error('Error:', error);
            });
     }

     function endTurn() {
         fetch('/end_turn')
         .then(response => response.text())
         .then(data => {
                document.getElementById("NextTurnBtn").disabled = true;
                //show_overlay();
                getBoard();
                getCardsInHands()
                showPlayers();
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
        console.log(`Selected Card ${cardId}`);
        document.getElementById("handCardID" + cardId).classList.add("CardHighlight");
    }

    function selectField(event) {
        if (selectedCardId !== null) {
            const fieldId = event.target.id;
            console.log(`Selected Field ${fieldId}`);

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
            })
            .catch((error) => {
                console.error('Error:', error);
            });
            getBoard();
            getCardsInHands();
            showPlayers();
            //викликати функцію оновлення руки і онвлення поля якщо повернулося значення True
            // Скидання вибору
            selectedCardId = null;
        }
    }
    function selectPlayer(event) {
        if (selectedCardId !== null) {
            const fieldId = event.target.id;
            console.log(`Selected Field ${fieldId}`);

            // Отримайте координати рядка і стовпця з fieldId, наприклад, field11
            const selectedPlayer = fieldId.slice(6).split('');

            document.getElementById(fieldId).className="PlayerHighlight";

            // Відправте POST-запит з даними
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
                console.log('Success:', data);
                if (data.response == true)
                    document.getElementById("NextTurnBtn").disabled = false;
            })
            .catch((error) => {
                console.error('Error:', error);
            });

            getCardsInHands()
            showPlayers();

            selectedCardId = null;
        }
    }

    function show_overlay(){
        var overlay = document.createElement("div")
        overlay.innerHTML = " <button type='button' onClick='removeOverlay()' >Next turn!</button>"
        overlay.id = "OverlayId"
        overlay.classList.add("Overlay")
        window.scrollTo(0, 0);
        document.body.append(overlay)
        document.body.classList.add("ScrollBlock")
    }

    function  removeOverlay(){
        document.body.classList.remove("ScrollBlock")
        document.getElementById("OverlayId").remove()
    }

     function endGameRound() {
         window.location.href = '/end_game_round';
     }

     function startNewGame() {
         window.location.href = '/end_game';
     }
     function restartGame() {
         window.location.href = '/restart_game';
     }

     function returnToGame() {
         window.location.href = '/return_to_game';
     }