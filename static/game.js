// document.addEventListener("DOMContentLoaded", function () {
//     const player = document.getElementById("player");
//     const enemy = document.getElementById("enemy");
    
//     let playerPosition = 50; // Player's initial position (Left=0, Right=100)
//     let lastMove = 1; // Track last move (0 = Left, 1 = Right)
    
//     document.addEventListener("keydown", function (event) {
//         if (event.key === "ArrowLeft" && playerPosition > 0) {
//             playerPosition -= 50;
//             lastMove = 0;
//         } else if (event.key === "ArrowRight" && playerPosition < 100) {
//             playerPosition += 50;
//             lastMove = 1;
//         }
        
//         player.style.left = playerPosition + "px";
        
//         // Send move data to AI backend
//         fetch("/predict", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json",
//             },
//             body: JSON.stringify({ last_move: lastMove }),
//         })
//         .then(response => response.json())
//         .then(data => {
//             let aiPrediction = data.prediction;
//             let enemyPosition = aiPrediction === 0 ? 50 : 150;
//             enemy.style.left = enemyPosition + "px";
//         });
//     });
// });
