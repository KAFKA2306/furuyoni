// Sakura Petal Effect
(function () {
    const canvas = document.createElement('canvas');
    canvas.id = 'sakura-canvas';
    document.body.appendChild(canvas);

    const ctx = canvas.getContext('2d');
    let width, height;
    let petals = [];

    const TOTAL_PETALS = 40; // Number of petals

    function resize() {
        width = window.innerWidth;
        height = window.innerHeight;
        canvas.width = width;
        canvas.height = height;
    }

    class Petal {
        constructor() {
            this.x = Math.random() * width;
            this.y = Math.random() * height - height;
            this.size = Math.random() * 5 + 5;
            this.speedY = Math.random() * 1 + 0.5;
            this.speedX = Math.random() * 0.5 - 0.25;
            this.rotation = Math.random() * 360;
            this.rotationSpeed = Math.random() * 2 - 1;
            this.opacity = Math.random() * 0.5 + 0.3;
        }

        update() {
            this.y += this.speedY;
            this.x += this.speedX + Math.sin(this.y / 50) * 0.5;
            this.rotation += this.rotationSpeed;

            if (this.y > height) {
                this.y = -20;
                this.x = Math.random() * width;
            }
        }

        draw() {
            ctx.save();
            ctx.translate(this.x, this.y);
            ctx.rotate(this.rotation * Math.PI / 180);
            ctx.globalAlpha = this.opacity;
            ctx.fillStyle = '#ffb7c5';

            // Draw a simple petal shape
            ctx.beginPath();
            ctx.moveTo(0, 0);
            ctx.bezierCurveTo(this.size / 2, -this.size / 2, this.size, 0, 0, this.size);
            ctx.bezierCurveTo(-this.size, 0, -this.size / 2, -this.size / 2, 0, 0);
            ctx.fill();

            ctx.restore();
        }
    }

    function init() {
        resize();
        window.addEventListener('resize', resize);

        for (let i = 0; i < TOTAL_PETALS; i++) {
            petals.push(new Petal());
        }

        animate();
    }

    function animate() {
        ctx.clearRect(0, 0, width, height);

        petals.forEach(petal => {
            petal.update();
            petal.draw();
        });

        requestAnimationFrame(animate);
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
