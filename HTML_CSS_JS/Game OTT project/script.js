document.addEventListener("mousemove", (event) => {
        const $cards = document.querySelector(".cards");
        const $images = document.querySelectorAll(".img");
        const $backgrounds = document.querySelectorAll(".bg");
        const RANGE = 40;

        const containerRect = $cards.getBoundingClientRect();
        const centerX = containerRect.left + containerRect.width / 2;
        const centerY = containerRect.top + containerRect.height / 2;

        const calcValue = (a, b) => {
          return ((a / b) * RANGE - RANGE / 2).toFixed(1);
        };

        const yValue = calcValue(event.clientY - centerY, containerRect.height);
        const xValue = calcValue(event.clientX - centerX, containerRect.width);

        $cards.style.transform = `rotateX(${yValue}deg) rotateY(${xValue}deg)`;

        $images.forEach(($img) => {
          $img.style.transform = `translateX(${-xValue}px) translateY(${yValue}px)`;
        });

        $backgrounds.forEach(($bg) => {
          $bg.style.backgroundPosition = `${xValue * 0.45}px ${
            yValue * 0.45
          }px`;
        });
      });