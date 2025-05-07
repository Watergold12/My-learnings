let inputDirection = { x: 0, y: 0 }
let lastInputDirection = { x: 0, y: 0 }
let isPaused = false;

window.addEventListener('keydown', e => {
  if (e.key === 'Escape') {
    // Step 1: Toggle the pause state
    isPaused = !isPaused;
    // Add code here to pause or resume the game, e.g. by stopping or restarting the game loop or timer
  } else {
    // Handle arrow keys
    switch (e.key) {
      case 'ArrowUp':
        if (lastInputDirection.y !== 0) break
        inputDirection = { x: 0, y: -1 }
        break
      case 'ArrowDown':
        if (lastInputDirection.y !== 0) break
        inputDirection = { x: 0, y: 1 }
        break
      case 'ArrowLeft':
        if (lastInputDirection.x !== 0) break
        inputDirection = { x: -1, y: 0 }
        break
      case 'ArrowRight':
        if (lastInputDirection.x !== 0) break
        inputDirection = { x: 1, y: 0 }
        break
    }
  }
})

// Step 2: Check if the game is paused before returning the input direction
export function getInputDirection() {
  if (isPaused) {
    return { x: 0, y: 0 };
  } else {
    lastInputDirection = inputDirection
    return inputDirection
  }
}
