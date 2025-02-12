let ball = new Image();
ball.src = "./static/img/redball.png";

let ballPosition = { x: 100, y: 100 };
let ballSize = { width: 30, height: 70 };

let canvas = document.getElementById("canvas");
canvas.width = 500;
canvas.height = 500;

const ctx = canvas.getContext("2d");
ctx.imageSmoothingEnabled = true;
ctx.imageSmoothingQuality = "high";

ball.onload = function() {
    drawBall();
};

function drawBall() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(ball, ballPosition.x, ballPosition.y, ballSize.width, ballSize.height);
}

document.addEventListener("keydown", function(event) {
    switch (event.key) {
        case "w":
        case "ArrowUp":
            ballPosition.y -= 10;
            break;
        case "a":
        case "ArrowLeft":
            ballPosition.x -= 10;
            break;
        case "s":
        case "ArrowDown":
            ballPosition.y += 10;
            break;
        case "d":
        case "ArrowRight":
            ballPosition.x += 10;
            break;
    }
    drawBall();
});
