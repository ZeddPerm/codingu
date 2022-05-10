var redY = 350;
var blueY = 350;
var ballX = 450;
var ballY = 400;
var ballSpeedX = 3;
var ballSpeedY = 3;
var redScore = 0;
var blueScore = 0;
function setup() {
    createCanvas(900, 900);
}
function draw() {
    background(200);

    noStroke();

    fill(255, 0, 0);
    rect(35, redY, 25, 100);
    fill(0, 0, 255);
    rect(840, blueY, 25, 100);

    fill(0, 255, 0);
    circle(ballX, ballY, 50)

    paddleMovement();
    ballMovement();
    paddleBallCollision();
    scoreDisplay();
}
function paddleMovement() {
    if (keyIsDown(UP_ARROW) && blueY >= 0) {
        blueY -= 4
    }
    if (keyIsDown(DOWN_ARROW) && blueY <= 800) {
        blueY += 4
    }
    if (keyIsDown(87) && redY >= 0) {
        redY -= 4
    }
    if (keyIsDown(83) && redY <= 800) {
        redY += 4
    }
}
function ballMovement() {
    ballX += ballSpeedX;
    ballY += ballSpeedY;
    if (ballX >= 875) {
        ballSpeedX = -ballSpeedX
        redScore++;
    }
    if (ballX <= 25) {
        ballSpeedX = -ballSpeedX
        blueScore++;
    }
    if (ballY >= 875 || ballY <= 25) {
        ballSpeedY = -ballSpeedY
    }
}
function paddleBallCollision() {
    if ((ballX + 25) >= 840) {
        if (ballY >= blueY - 15 && ballY <= blueY + 100) {
            ballSpeedX = -3
        }
    }
    if ((ballX - 25) <= 60) {
        if (ballY >= redY - 15 && ballY <= redY + 100) {
            ballSpeedX = 3
        }
    }
}
function scoreDisplay() {
    textSize(16);
    fill("red");
    textAlign(RIGHT, TOP);
    text('Score: ', 70, 30);
    text(redScore, 80, 30);
    fill("blue");
    textAlign(LEFT, TOP);
    text('Score: ', 810, 30);
    text(blueScore, 860, 30);
}