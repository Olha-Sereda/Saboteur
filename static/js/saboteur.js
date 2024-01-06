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

    let selectedCardId = null;
    function selectCard(cardId) {
        selectedCardId = cardId;
        console.log(`Selected Card ${cardId}`);
        document.getElementById("handCardID" + cardId).className="CardHighlight";
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
                console.log('Success:', data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });

            //викликати функцію оновлення руки і онвлення поля якщо повернулося значення True
            // Скидання вибору
            selectedCardId = null;
        }
    }

