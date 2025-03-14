document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll('.button');
    const title = document.querySelector('h1');

    // Анимация появления заголовка
    title.style.opacity = 0;
    setTimeout(() => {
        title.style.transition = "opacity 1s";
        title.style.opacity = 1;
    }, 1000);

    // Анимация для кнопок при загрузке
    buttons.forEach((button, index) => {
        button.style.transform = 'translateY(20px)';
        button.style.opacity = '0';
        setTimeout(() => {
            button.style.transition = "transform 0.5s, opacity 0.5s";
            button.style.transform = 'translateY(0)';
            button.style.opacity = '1';
        }, 1000 + index * 300); // Задержка для каждого элемента
    });

    // Эффект "прыжка" на кнопках при клике
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            button.style.transition = "transform 0.2s";
            button.style.transform = 'scale(1.1)';
            setTimeout(() => {
                button.style.transform = 'scale(1)';
            }, 200);
        });
    });

    // Пример анимации фона при клике на заголовок
    title.addEventListener('click', () => {
        document.body.classList.toggle('nightmare');
    });
});

// CSS для эффекта фона "ночного кошмара"
const style = document.createElement('style');
style.innerHTML = `
    .nightmare {
        animation: nightmareEffect 3s infinite alternate;
    }

    @keyframes nightmareEffect {
        0% { background: linear-gradient(180deg, #1a1a1a, #333); }
        100% { background: linear-gradient(180deg, #444, #222); }
    }
`;