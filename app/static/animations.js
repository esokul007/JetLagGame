				// --- BEGIN: REPLACE your touch events for '.card' with the following ---
let mouseDown = false;
let activeCard = null;
let startY = 0, startX = 0; // <--- Move this OUTSIDE the forEach!

document.querySelectorAll('.card').forEach(card => {
    let moved = false;

    card.addEventListener('touchstart', e => {
        if (e.target.closest('.add-button') || e.target.closest('.rem-button') || e.target.closest(".user-dropdown")) return;
        if (e.touches.length > 1) return;
        startY = e.touches[0].clientY;
        startX = e.touches[0].clientX;
        moved = false;
        card.classList.add('curve');
    }, { passive: false });

    card.addEventListener('touchmove', e => {
        if (e.touches.length > 1) return;
        let dy = e.touches[0].clientY - startY;
        if (dy < 0) {
            e.preventDefault();
            moved = true;
            dy = Math.max(dy, -120);
            let transform = '';
            if (dy > -50) {
                transform = `translateY(${dy}px)`;
            } else {
                const rotate = Math.min(-(dy + 50) / 3, 20);
                const theta = rotate * Math.PI / 180;
                const w = card.offsetWidth;
                const compensateX = w * (1 - Math.cos(theta));
                transform = `translate(${compensateX}px, ${dy}px) rotate(${rotate}deg)`;
            }
            card.style.transform = transform;
        }
    }, { passive: false });

    card.addEventListener('touchend', e => {
        card.classList.remove('curve');
        card.style.transform = "";
        if (!moved) return;
        const select = card.querySelector('.user-dropdown');
        const user = select ? select.value : "";
        let endY = e.changedTouches[0].clientY;
        if (startY - endY > 50) {
            const cardValue = card.dataset.card;
            if (typeof cardValue === "undefined") return;
            card.classList.add('swipe-up');
            setTimeout(() => {
                card.classList.remove('swipe-up');
            }, 500);
            fetch('/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    card: cardValue,
                    action: 'swipe',
                    user: user
                })
            }).then(response => {
                if (response.ok) {
                    alert("Card sent!");
                    window.location.reload();
                }
            });
        }
    }, { passive: false });

    // Mouse events
    card.addEventListener('mousedown', e => {
        if (e.target.closest('.add-button') || e.target.closest('.rem-button')) return;
        mouseDown = true;
        startY = e.clientY;
        startX = e.clientX;
        activeCard = card;
        card.classList.add('curve');
        document.addEventListener('mousemove', mouseMoveHandler);
        document.addEventListener('mouseup', mouseUpHandler);
    });
});
function mouseMoveHandler(e) {
    if (!mouseDown || !activeCard) return;
    let dy = e.clientY - startY;
    let transform = '';
    if (dy < 0) {
        dy = Math.max(dy, -120)
        if (dy > -50) {
            transform = `translateY(${dy}px)`;
        } else {
            const rotate = Math.min(-(dy + 50) / 3, 20);
            const theta = rotate * Math.PI / 180;
            const w = activeCard.offsetWidth;
            const compensateX = w * (1 - Math.cos(theta));
            transform = `translate(${compensateX}px, ${dy}px) rotate(${rotate}deg)`;
        }
        activeCard.style.transform = transform;
    }
}

function mouseUpHandler(e) {
    if (e.target.closest('.user-dropdown')) {
        mouseDown = false;
        activeCard = null;
        document.removeEventListener('mouseup', mouseUpHandler);
        document.removeEventListener('mousemove', mouseMoveHandler);
        return;
    }
    if (!mouseDown || !activeCard) return;
    mouseDown = false;
    activeCard.classList.remove('curve');
    activeCard.style.transform = '';
    const endY = e.clientY;
    if (startY - endY > 50) {
        handleSwipe(activeCard);
    }
    activeCard = null;
    document.removeEventListener('mouseup', mouseUpHandler);
    document.removeEventListener('mousemove', mouseMoveHandler);
}

function handleSwipe(cardElem) {
    const cardValue = cardElem.dataset.card;
    if (typeof cardValue === "undefined") return;
    const select = cardElem.querySelector('.user-dropdown');
    const user = select ? select.value : "";
    cardElem.classList.add('swipe-up');
    setTimeout(() => {
        cardElem.classList.remove('swipe-up');
    }, 500);
    fetch('/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({card: cardValue, action: 'swipe', user: user})
    }).then(response => {
        if (response.ok) {
            alert("Card sent!");
            window.location.reload();
        }
    });
}
			function startQuestionTimer(sentAtString, allowedTimeSeconds) {
					const sentAt = new Date(sentAtString + "Z"); // Parse the time the question was sent (in UTC)
					const allowedTime = allowedTimeSeconds; // How many seconds the user has to answer
					const timerElem = document.getElementById('timer'); // Where the timer will be displayed

					function updateTimer() {
							const now = new Date(); // Current time
							const elapsed = (now - sentAt) / 1000; // How many seconds since the question was sent
							const remaining = Math.max(0, allowedTime - elapsed); // Time left, never less than 0
							const min = Math.floor(remaining / 60);
							const sec = Math.floor(remaining % 60);
							timerElem.textContent = `${min}:${sec.toString().padStart(2,'0')}`; // Show as MM:SS
							if (remaining > 0) setTimeout(updateTimer, 1000); // Update every second
							else timerElem.textContent = "Time's up!"; // When time runs out
					}
					updateTimer(); // Start the timer
			}
			startQuestionTimer("{{ sentAt }}", {{ allowed_time|default(300) }});

		const isCursed = {{ 'true' if cursed else 'false' }};
		function showCurseOverlay() {
			const overlay = document.getElementById('curse-overlay');
			const message = document.getElementById('curse-message');
			overlay.style.display = 'flex';
			message.style.display = ''; // show the message
			// Hide the message after 2 seconds (optional)
			setTimeout(() => {
				message.style.display = "none";
			}, 3000);
		}

  		window.addEventListener("DOMContentLoaded", function() {
    		if (isCursed) {
      			showCurseOverlay();
    		}
    	});