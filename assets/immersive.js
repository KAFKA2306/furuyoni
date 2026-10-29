// Shared usability helpers and optional sakura decoration.
(function () {
    'use strict';

    const LEGACY_PAGE_PATTERNS = [
        /\/lore(?:\.html)?$/,
        /\/resources(?:\.html)?$/,
        /\/history\//,
        /\/megami\/(?:\d{2}_[^/]+|cards)(?:\.html)?$/,
    ];

    function isLegacyPage(pathname) {
        return LEGACY_PAGE_PATTERNS.some((pattern) => pattern.test(pathname));
    }

    function addLegacyBanner() {
        const content = document.querySelector('.md-content__inner');
        if (!content || content.querySelector('.legacy-version-banner')) {
            return;
        }

        if (!isLegacyPage(window.location.pathname)) {
            return;
        }

        const banner = document.createElement('aside');
        banner.className = 'legacy-version-banner';
        banner.setAttribute('role', 'note');
        banner.innerHTML = `
            <strong>新幕アーカイブ</strong>
            <span>このページは主に旧シリーズ「新幕」の資料です。現行の再演ではカード・ルール・使用可能範囲が異なる場合があります。</span>
            <a href="${resolveSitePath('status.html')}">版の違いを見る</a>
            <a href="https://furuyoni.sekiseiro.com/re/">再演公式サイト</a>
        `;
        content.prepend(banner);
    }

    function resolveSitePath(relativePath) {
        const marker = '/furuyoni/';
        const pathname = window.location.pathname;
        const markerIndex = pathname.indexOf(marker);
        const root = markerIndex >= 0 ? pathname.slice(0, markerIndex + marker.length) : '/';
        return `${root}${relativePath}`;
    }

    function initializePageHelpers() {
        addLegacyBanner();
    }

    if (typeof window.document$ !== 'undefined' && window.document$.subscribe) {
        window.document$.subscribe(initializePageHelpers);
    } else if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializePageHelpers, { once: true });
    } else {
        initializePageHelpers();
    }

    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const smallViewport = window.matchMedia('(max-width: 768px)').matches;
    const saveData = Boolean(navigator.connection && navigator.connection.saveData);

    if (prefersReducedMotion || smallViewport || saveData || document.getElementById('sakura-canvas')) {
        return;
    }

    const canvas = document.createElement('canvas');
    canvas.id = 'sakura-canvas';
    canvas.setAttribute('aria-hidden', 'true');
    document.body.appendChild(canvas);

    const ctx = canvas.getContext('2d');
    if (!ctx) {
        canvas.remove();
        return;
    }

    let width = 0;
    let height = 0;
    let animationFrame = null;
    const petals = [];
    const totalPetals = 24;

    function resize() {
        width = window.innerWidth;
        height = window.innerHeight;
        canvas.width = width;
        canvas.height = height;
    }

    class Petal {
        constructor() {
            this.reset(true);
        }

        reset(initial) {
            this.x = Math.random() * width;
            this.y = initial ? Math.random() * height - height : -20;
            this.size = Math.random() * 4 + 4;
            this.speedY = Math.random() * 0.8 + 0.35;
            this.speedX = Math.random() * 0.4 - 0.2;
            this.rotation = Math.random() * 360;
            this.rotationSpeed = Math.random() * 1.5 - 0.75;
            this.opacity = Math.random() * 0.35 + 0.15;
        }

        update() {
            this.y += this.speedY;
            this.x += this.speedX + Math.sin(this.y / 50) * 0.35;
            this.rotation += this.rotationSpeed;

            if (this.y > height) {
                this.reset(false);
            }
        }

        draw() {
            ctx.save();
            ctx.translate(this.x, this.y);
            ctx.rotate(this.rotation * Math.PI / 180);
            ctx.globalAlpha = this.opacity;
            ctx.fillStyle = '#ffb7c5';
            ctx.beginPath();
            ctx.moveTo(0, 0);
            ctx.bezierCurveTo(this.size / 2, -this.size / 2, this.size, 0, 0, this.size);
            ctx.bezierCurveTo(-this.size, 0, -this.size / 2, -this.size / 2, 0, 0);
            ctx.fill();
            ctx.restore();
        }
    }

    function animate() {
        ctx.clearRect(0, 0, width, height);
        petals.forEach((petal) => {
            petal.update();
            petal.draw();
        });
        animationFrame = window.requestAnimationFrame(animate);
    }

    function startAnimation() {
        if (animationFrame !== null || document.hidden) {
            return;
        }
        animationFrame = window.requestAnimationFrame(animate);
    }

    function stopAnimation() {
        if (animationFrame === null) {
            return;
        }
        window.cancelAnimationFrame(animationFrame);
        animationFrame = null;
    }

    resize();
    window.addEventListener('resize', resize, { passive: true });

    for (let index = 0; index < totalPetals; index += 1) {
        petals.push(new Petal());
    }

    document.addEventListener('visibilitychange', () => {
        if (document.hidden) {
            stopAnimation();
        } else {
            startAnimation();
        }
    });

    startAnimation();
})();
