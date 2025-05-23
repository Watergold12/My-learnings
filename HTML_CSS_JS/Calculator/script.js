const calculator = document.getElementById('calculator');
const displayCurrent = document.getElementById('current-operand');
const displayPrevious = document.getElementById('previous-operand');
const numberButtons = document.querySelectorAll('.number');
const operationButtons = document.querySelectorAll('.operation');
const equalsButton = document.getElementById('equals');
const clearButton = document.getElementById('clear');
const deleteButton = document.getElementById('delete');
const dotButton = document.getElementById('dot');

numberButtons.forEach(button => {
  button.addEventListener('click', () => {
      appendNumber(button.innerText);
      updateDisplay();
  });
});

operationButtons.forEach(button => {
  button.addEventListener('click', () => {
      chooseOperation(button.innerText);
      updateDisplay();
  });
});

clearButton.addEventListener('click', clear);
deleteButton.addEventListener('click', deleteNumber);
equalsButton.addEventListener('click', compute);
dotButton.addEventListener('click', appendDot);

let currentOperand = '';
let previousOperand = '';
let operation = null;

function clear() {
  currentOperand = '0';
  previousOperand = '';
  operation = null;
  updateDisplay();
}

function deleteNumber() {
  currentOperand = currentOperand.toString().slice(0, -1);
  if(currentOperand === '') currentOperand = '0'; // Display '0' if all numbers are deleted
  updateDisplay();
}

function compute() {
  let computation;
  const prev = parseFloat(previousOperand);
  const current = parseFloat(currentOperand);
  if (isNaN(prev) || isNaN(current)) return;
 
  switch (operation) {
      case '+':
          computation = prev + current;
          break;
      case '-':
          computation = prev - current;
          break;
      case '*':
          computation = prev * current;
          break;
      case '/':
          computation = prev / current;
          break;
      default:
          return;
  }

  currentOperand = computation;
  operation = undefined;
  previousOperand = '';
  updateDisplay(); // Refresh the display with the new state
}

function appendDot() {
  if (currentOperand.includes('.')) return; // Prevent multiple decimals
  if (currentOperand === '') currentOperand = '0'; // If empty, start with '0.'
  currentOperand += '.';
  updateDisplay();
}

function appendNumber(number) {
  if (number === '.' && currentOperand.includes('.')) return; // Prevent multiple decimals
  if (currentOperand === '0') {
    currentOperand = number.toString(); // Replace '0' with the number clicked
  } else {
    currentOperand += number.toString();
  }
}

function chooseOperation(selectedOperation) {
  if (currentOperand === '') return;
  if (previousOperand !== '') {
      compute();
  }
  operation = selectedOperation;
  previousOperand = currentOperand;
  currentOperand = '';
}

function updateDisplay() {
  displayCurrent.innerText = currentOperand !== '' ? currentOperand : '0';
  displayPrevious.innerText = previousOperand + ' ' + (operation || '');
}
