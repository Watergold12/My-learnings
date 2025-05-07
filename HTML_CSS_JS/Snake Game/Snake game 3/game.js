import { update as updateSnake, draw as drawSnake, SNAKE_SPEED, getSnakeHead, snakeIntersection } from './snake.js'
import { update as updateFood, draw as drawFood, getFoodPosition } from './food.js'
import { outsideGrid } from './grid.js'

let lastRenderTime = 0
let gameOver = false
let score = 0
const gameBoard = document.getElementById('game-board')

function main(currentTime) {
  if (gameOver) {
    if (confirm('You lost. Press ok to restart.')) {
      window.location = '/'
    }
    return
  }

  window.requestAnimationFrame(main)
  const secondsSinceLastRender = (currentTime - lastRenderTime) / 1000
  if (secondsSinceLastRender < 1 / SNAKE_SPEED) return

  lastRenderTime = currentTime

  update()
  draw()
}

window.requestAnimationFrame(main)

function update() {
  updateSnake()
  if (outsideGrid(getSnakeHead()) || snakeIntersection()) {
    gameOver = true
  }
  updateFood()
  checkDeath()

  // check if the snake head has collided with the food
  if (getSnakeHead().x === getFoodPosition().x && getSnakeHead().y === getFoodPosition().y) {
    score += 5;
scoreElement.textContent = `Score: ${score}`;
  }
}

function draw() {
  gameBoard.innerHTML = ''
  drawSnake(gameBoard)
  drawFood(gameBoard)
}

function checkDeath() {
  gameOver = outsideGrid(getSnakeHead()) || snakeIntersection()
}

// Display scoreboard
const scoreboard = document.createElement('div')
scoreboard.textContent = `Score: ${score}`
scoreboard.style.fontWeight = 'bold'
scoreboard.style.fontSize = '24px'
scoreboard.style.marginBottom = '10px'
gameBoard.insertAdjacentElement('beforebegin', scoreboard)
const scoreElement = document.querySelector('.score-value');