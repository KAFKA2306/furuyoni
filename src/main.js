import { pairs, cards, portraits, baseUrl } from './data.js';
import { storySteps } from './story.js';

const els = {
    pairGrid: document.getElementById('pair-grid'),
    storyTimeline: document.getElementById('story-timeline'),
    modal: document.getElementById('modal'),
    modalContent: document.getElementById('modal-content'),
    closeModal: document.getElementById('close-modal'),
    navBtns: document.querySelectorAll('.nav-btn'),
    views: document.querySelectorAll('.view')
};

const observers = {
    reveal: new IntersectionObserver(entries => {
        entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('reveal'); });
    }, { threshold: 0.1 })
};

const render = {
    pairs() {
        els.pairGrid.innerHTML = pairs.map(p => `
            <article class="pair-card" data-id="${p.id}">
                <div class="pair-portraits">
                    ${p.characters.map(c => `
                        <div class="mini-portrait">
                            <img src="${baseUrl}${portraits[c]}" alt="${c}" loading="lazy">
                        </div>
                    `).join('')}
                </div>
                <h3 class="pair-name">${p.name}</h3>
                <div class="pair-chars">${p.characters.join(' / ')}</div>
                <p class="pair-tagline">${p.description.split('。')[0]}</p>
            </article>
        `).join('');

        document.querySelectorAll('.pair-card').forEach((c, i) => {
            c.addEventListener('click', () => actions.showModal(pairs.find(p => p.id === +c.dataset.id)));
            c.style.animationDelay = `${i * 0.1}s`;
            observers.reveal.observe(c);
        });
    },

    story() {
        els.storyTimeline.innerHTML = storySteps.map((s, i) => `
            <div class="story-step" data-step="${s.id}">
                <div class="step-number">${i + 1}</div>
                <div class="step-content">
                    <div class="step-subtitle">${s.subtitle}</div>
                    <h3>${s.title}</h3>
                    <p class="step-description">${s.description}</p>
                    <ul class="lesson-list">
                        ${s.lessons.map(l => `<li>${l}</li>`).join('')}
                    </ul>
                    <button class="btn-focus" data-pair-id="${s.focusPair}">Focus Pair Detail</button>
                </div>
            </div>
        `).join('');

        document.querySelectorAll('.btn-focus').forEach(b => {
            b.addEventListener('click', e => {
                e.stopPropagation();
                actions.showModal(pairs.find(p => p.id === +b.dataset.pairId));
            });
        });

        document.querySelectorAll('.story-step').forEach(s => observers.reveal.observe(s));
    }
};

const actions = {
    switchView(btn) {
        const target = btn.dataset.view;
        const current = document.querySelector('.view:not(.hidden)');
        if (current.id === `${target}-view`) return;

        current.classList.add('fade-out');
        setTimeout(() => {
            els.navBtns.forEach(b => b.classList.toggle('active', b === btn));
            els.views.forEach(v => {
                v.classList.toggle('hidden', v.id !== `${target}-view`);
                v.classList.remove('fade-out');
            });
            if (target === 'story') render.story();
            else {
                render.pairs();
                actions.createSakura();
            }
        }, 300);
    },

    showModal(p) {
        els.modalContent.innerHTML = `
            <div class="detail-container">
                <aside class="detail-sidebar">
                    <h2 class="detail-title">${p.name}</h2>
                    <div class="detail-info">
                        <div class="info-block">
                            <label>Description</label>
                            <p>${p.description}</p>
                        </div>
                        <div class="info-block">
                            <label class="strength">Strength</label>
                            <p>${p.pros}</p>
                        </div>
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
                                ${(cards[c] || []).map(path => `
                                    <div class="card-item" onclick="window.open('${baseUrl}${path}', '_blank')">
                                        <img src="${baseUrl}${path}" alt="${c} card" loading="lazy">
                                    </div>
                                `).join('')}
                            </div>
                        </section>
                    `).join('')}
                </div>
            </div>
        `;
        els.modal.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
    },

    closeModal() {
        els.modal.classList.add('hidden');
        document.body.style.overflow = 'auto';
    },

    createSakura() {
        document.querySelectorAll('.sakura-petal').forEach(p => p.remove());
        for (let i = 0; i < 30; i++) {
            const p = document.createElement('div');
            const size = Math.random() * 10 + 5;
            p.className = 'sakura-petal';
            p.style.left = Math.random() * 100 + 'vw';
            p.style.width = `${size}px`;
            p.style.height = `${size * 0.7}px`;
            p.style.animationDuration = Math.random() * 5 + 5 + 's';
            p.style.animationDelay = Math.random() * 10 + 's';
            p.style.opacity = Math.random() * 0.5 + 0.2;
            document.body.appendChild(p);
        }
    }
};

els.navBtns.forEach(b => b.addEventListener('click', () => actions.switchView(b)));
els.closeModal.addEventListener('click', actions.closeModal);
els.modal.querySelector('.modal-overlay').addEventListener('click', actions.closeModal);

document.addEventListener('mousemove', e => {
    document.querySelectorAll('.pair-card').forEach(c => {
        const r = c.getBoundingClientRect();
        c.style.setProperty('--mouse-x', `${e.clientX - r.left}px`);
        c.style.setProperty('--mouse-y', `${e.clientY - r.top}px`);
    });
});

render.pairs();
actions.createSakura();
