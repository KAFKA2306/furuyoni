import { pairs, cards, portraits, baseUrl } from './data.js';
import { storySteps } from './story.js';

const grid = document.getElementById('pair-grid');
const timeline = document.getElementById('story-timeline');
const modal = document.getElementById('modal');
const modalContent = document.getElementById('modal-content');

function renderPairs() {
    grid.innerHTML = pairs.map(p => `
        <div class="pair-card" data-id="${p.id}">
            <div class="pair-portraits">
                ${p.characters.map(c => `<div class="mini-portrait"><img src="${baseUrl}${portraits[c]}" alt="${c}" loading="lazy"></div>`).join('')}
            </div>
            <h3 class="pair-name">${p.name}</h3>
            <div class="pair-chars">${p.characters.join(' / ')}</div>
            <p class="pair-tagline">${p.description.split('。')[0]}</p>
        </div>
    `).join('');
    grid.querySelectorAll('.pair-card').forEach(c => c.onclick = () => showModal(pairs.find(p => p.id === +c.dataset.id)));
}

function renderStory() {
    timeline.innerHTML = storySteps.map((s, i) => `
        <div class="story-step">
            <div class="step-number">${i + 1}</div>
            <div class="step-content">
                <div class="step-subtitle">${s.subtitle}</div>
                <h3>${s.title}</h3>
                <p>${s.description}</p>
                <ul>${s.lessons.map(l => `<li>${l}</li>`).join('')}</ul>
                <button class="btn-focus" data-id="${s.focusPair}">Focus Pair Detail</button>
            </div>
        </div>
    `).join('');
    timeline.querySelectorAll('.btn-focus').forEach(b => b.onclick = e => {
        e.stopPropagation();
        showModal(pairs.find(p => p.id === +b.dataset.id));
    });
}

function showModal(p) {
    modalContent.innerHTML = `
        <div class="detail-container">
            <aside class="detail-sidebar">
                <h2 class="detail-title">${p.name}</h2>
                <div class="detail-info">
                    <div class="info-block"><label>Description</label><p>${p.description}</p></div>
                    <div class="info-block"><label class="strength">Strength</label><p>${p.pros}</p></div>
                    ${p.cons ? `<div class="info-block"><label class="weakness">Weakness</label><p>${p.cons}</p></div>` : ''}
                </div>
            </aside>
            <div class="detail-cards">
                ${p.characters.map(c => `
                    <section class="char-section">
                        <div class="char-header">
                            <img src="${baseUrl}${portraits[c]}" alt="${c}" class="char-portrait-large">
                            <h3>${c}</h3>
                        </div>
                        <div class="char-card-list">
                            ${(cards[c] || []).map(path => `<div class="card-item" onclick="window.open('${baseUrl}${path}','_blank')"><img src="${baseUrl}${path}" alt="${c}" loading="lazy"></div>`).join('')}
                        </div>
                    </section>
                `).join('')}
            </div>
        </div>
    `;
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
}

document.querySelectorAll('.nav-btn').forEach(b => b.onclick = () => {
    const view = b.dataset.view;
    document.querySelectorAll('.nav-btn').forEach(n => n.classList.toggle('active', n === b));
    document.querySelectorAll('.view').forEach(v => v.classList.toggle('hidden', v.id !== `${view}-view`));
    if (view === 'story') renderStory();
});

document.getElementById('close-modal').onclick = closeModal;
modal.querySelector('.modal-overlay').onclick = closeModal;

renderPairs();

// Sakura Effect
function createSakura() {
    const petal = document.createElement('div');
    petal.classList.add('petal');
    const size = Math.random() * 15 + 8;
    const left = Math.random() * 100;
    const delay = Math.random() * 20;
    const duration = Math.random() * 10 + 15;

    petal.style.width = `${size}px`;
    petal.style.height = `${size}px`;
    petal.style.left = `${left}vw`;
    petal.style.animationDelay = `-${delay}s`; // Start mid-animation
    petal.style.animationDuration = `${duration}s`;

    // Randomly vary opacity/color slightly if desired, but CSS handles base style
    document.body.appendChild(petal);
}

// Create 50 petals for a dense but subtle effect
for (let i = 0; i < 50; i++) {
    createSakura();
}
