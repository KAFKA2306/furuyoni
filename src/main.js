import { pairs, cards, portraits, baseUrl } from './data.js';

const pairGrid = document.getElementById('pair-grid');
const modal = document.getElementById('modal');
const modalContent = document.getElementById('modal-content');
const closeModal = document.getElementById('close-modal');

/**
 * Render all pairs in the grid
 */
function renderPairsByGrid() {
    pairGrid.innerHTML = pairs.map(pair => `
        <div class="pair-card" data-id="${pair.id}">
            <div class="pair-portraits">
                ${pair.characters.map(char => `
                    <div class="mini-portrait">
                        <img src="${baseUrl}${portraits[char]}" alt="${char}" loading="lazy">
                    </div>
                `).join('')}
            </div>
            <div class="pair-name">${pair.name}</div>
            <div class="pair-chars">${pair.characters.join(' / ')}</div>
            <p class="pair-tagline">${pair.description.split('。')[0]}</p>
        </div>
    `).join('');

    // Add click events
    document.querySelectorAll('.pair-card').forEach(card => {
        card.addEventListener('click', () => {
            const id = parseInt(card.dataset.id);
            const pair = pairs.find(p => p.id === id);
            showModal(pair);
        });
    });
}

/**
 * Show pair details in the modal
 */
function showModal(pair) {
    const charSections = pair.characters.map(char => {
        const charCardsList = cards[char] || [];
        return `
            <div class="char-section">
                <div class="char-header">
                    <img src="${baseUrl}${portraits[char]}" alt="${char}" class="char-portrait-large">
                    <h3>${char}</h3>
                </div>
                <div class="char-card-list">
                    ${charCardsList.map(cardPath => `
                        <div class="card-item" onclick="window.open('${baseUrl}${cardPath}', '_blank')">
                            <img src="${baseUrl}${cardPath}" alt="${char} card" loading="lazy">
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }).join('');

    modalContent.innerHTML = `
        <div class="detail-container">
            <div class="detail-sidebar">
                <h2 class="detail-title">${pair.name}</h2>
                <div class="detail-info">
                    <div class="info-block">
                        <label>Description</label>
                        <p>${pair.description}</p>
                    </div>
                    <div class="info-block">
                        <label class="strength">Strength</label>
                        <p>${pair.pros}</p>
                    </div>
                    ${pair.cons ? `
                    <div class="info-block">
                        <label class="weakness">Weakness</label>
                        <p>${pair.cons}</p>
                    </div>
                    ` : ''}
                </div>
            </div>
            <div class="detail-cards">
                ${charSections}
            </div>
        </div>
    `;

    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

closeModal.addEventListener('click', () => {
    modal.classList.add('hidden');
    document.body.style.overflow = 'auto';
});

modal.querySelector('.modal-overlay').addEventListener('click', () => {
    modal.classList.add('hidden');
    document.body.style.overflow = 'auto';
});

// Add Sakura Petals Animation
function createSakuraPetals() {
    const container = document.body;
    for (let i = 0; i < 20; i++) {
        const petal = document.createElement('div');
        petal.className = 'sakura-petal';
        petal.style.left = Math.random() * 100 + 'vw';
        petal.style.animationDelay = Math.random() * 10 + 's';
        petal.style.opacity = Math.random() * 0.5 + 0.2;
        container.appendChild(petal);
    }
}

// Entrance Animation with Intersection Observer
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('reveal');
        }
    });
}, { threshold: 0.1 });

// Initialize animations after render
function initAnimations() {
    createSakuraPetals();
    document.querySelectorAll('.pair-card').forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
        observer.observe(card);
    });
}

// Initial render
renderPairsByGrid();
initAnimations();

// Add interactive hover effect for glow
document.addEventListener('mousemove', (e) => {
    document.querySelectorAll('.pair-card').forEach(card => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        card.style.setProperty('--mouse-x', `${x}px`);
        card.style.setProperty('--mouse-y', `${y}px`);
    });
});
