/**
 * Street View Personalizado DuocPoint
 * Sistema de visualización 360° con Three.js
 */

class StreetViewApp {
    constructor() {
        this.scene = null;
        this.camera = null;
        this.renderer = null;
        this.sphere = null;
        this.texture = null;
        this.controls = {
            rotationX: 0,
            rotationY: 0,
            zoom: 1
        };
        this.isDragging = false;
        this.lastMouseX = 0;
        this.lastMouseY = 0;
        this.currentPoint = null;
        this.points = [];
        
        this.init();
    }
    
    async init() {
        this.setupEventListeners();
        await this.loadPoints();
        this.initThreeJS();
        this.render();
    }
    
    // === THREE.JS SETUP ===
    initThreeJS() {
        const canvas = document.getElementById('streetview-canvas');
        const container = document.getElementById('streetview-container');
        
        // Scene
        this.scene = new THREE.Scene();
        
        // Camera
        this.camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000);
        this.camera.position.set(0, 0, 0);
        
        // Renderer
        this.renderer = new THREE.WebGLRenderer({ 
            canvas: canvas, 
            antialias: true,
            alpha: true
        });
        this.renderer.setSize(container.clientWidth, container.clientHeight);
        this.renderer.setPixelRatio(window.devicePixelRatio);
        
        // Crear esfera para la imagen 360°
        this.createSphere();
        
        // Cargar primera imagen si hay puntos
        if (this.points.length > 0) {
            this.loadPointImage(this.points[0]);
        }
        
        this.hideLoading();
    }
    
    createSphere() {
        const geometry = new THREE.SphereGeometry(500, 60, 40);
        geometry.scale(-1, 1, 1); // Invertir para ver desde adentro
        
        const material = new THREE.MeshBasicMaterial({
            map: this.texture,
            side: THREE.DoubleSide
        });
        
        this.sphere = new THREE.Mesh(geometry, material);
        this.scene.add(this.sphere);
    }
    
    async loadPointImage(point) {
        if (!point.imagen_360_url) {
            this.showError('No hay imagen 360° disponible para este punto');
            return;
        }
        
        this.showLoading();
        
        try {
            const loader = new THREE.TextureLoader();
            this.texture = await new Promise((resolve, reject) => {
                loader.load(
                    point.imagen_360_url,
                    resolve,
                    undefined,
                    reject
                );
            });
            
            if (this.sphere) {
                this.sphere.material.map = this.texture;
                this.sphere.material.needsUpdate = true;
            }
            
            this.currentPoint = point;
            this.updatePointInfo(point);
            this.hideLoading();
            
        } catch (error) {
            console.error('Error cargando imagen:', error);
            this.showError('Error cargando imagen 360°');
        }
    }
    
    // === RENDER LOOP ===
    render() {
        requestAnimationFrame(() => this.render());
        
        if (this.sphere) {
            this.sphere.rotation.y = this.controls.rotationX;
            this.sphere.rotation.x = this.controls.rotationY;
        }
        
        if (this.camera) {
            this.camera.zoom = this.controls.zoom;
            this.camera.updateProjectionMatrix();
        }
        
        if (this.renderer && this.scene && this.camera) {
            this.renderer.render(this.scene, this.camera);
        }
    }
    
    // === EVENT LISTENERS ===
    setupEventListeners() {
        const canvas = document.getElementById('streetview-canvas');
        
        // Mouse events
        canvas.addEventListener('mousedown', (e) => this.onMouseDown(e));
        canvas.addEventListener('mousemove', (e) => this.onMouseMove(e));
        canvas.addEventListener('mouseup', () => this.onMouseUp());
        canvas.addEventListener('wheel', (e) => this.onWheel(e));
        
        // Touch events para móviles
        canvas.addEventListener('touchstart', (e) => this.onTouchStart(e));
        canvas.addEventListener('touchmove', (e) => this.onTouchMove(e));
        canvas.addEventListener('touchend', () => this.onTouchEnd());
        
        // Botones de control
        document.getElementById('btnRotateLeft')?.addEventListener('click', () => this.rotateLeft());
        document.getElementById('btnRotateRight')?.addEventListener('click', () => this.rotateRight());
        document.getElementById('btnLookUp')?.addEventListener('click', () => this.lookUp());
        document.getElementById('btnLookDown')?.addEventListener('click', () => this.lookDown());
        document.getElementById('btnZoomIn')?.addEventListener('click', () => this.zoomIn());
        document.getElementById('btnZoomOut')?.addEventListener('click', () => this.zoomOut());
        
        // Botones de navegación
        document.getElementById('btnFullscreen')?.addEventListener('click', () => this.toggleFullscreen());
        document.getElementById('btnInfo')?.addEventListener('click', () => this.showInfo());
        document.getElementById('btnBack')?.addEventListener('click', () => this.goBack());
        document.getElementById('btnRetry')?.addEventListener('click', () => this.retry());
        
        // Modal
        document.querySelectorAll('.modal-close').forEach(btn => {
            btn.addEventListener('click', () => this.closeModal());
        });
        
        // Resize
        window.addEventListener('resize', () => this.onResize());
    }
    
    // === MOUSE CONTROLS ===
    onMouseDown(e) {
        this.isDragging = true;
        this.lastMouseX = e.clientX;
        this.lastMouseY = e.clientY;
    }
    
    onMouseMove(e) {
        if (!this.isDragging) return;
        
        const deltaX = e.clientX - this.lastMouseX;
        const deltaY = e.clientY - this.lastMouseY;
        
        this.controls.rotationX += deltaX * 0.01;
        this.controls.rotationY += deltaY * 0.01;
        
        // Limitar rotación vertical
        this.controls.rotationY = Math.max(-Math.PI/2, Math.min(Math.PI/2, this.controls.rotationY));
        
        this.lastMouseX = e.clientX;
        this.lastMouseY = e.clientY;
    }
    
    onMouseUp() {
        this.isDragging = false;
    }
    
    onWheel(e) {
        e.preventDefault();
        const delta = e.deltaY > 0 ? 0.9 : 1.1;
        this.controls.zoom *= delta;
        this.controls.zoom = Math.max(0.5, Math.min(3, this.controls.zoom));
    }
    
    // === TOUCH CONTROLS ===
    onTouchStart(e) {
        e.preventDefault();
        if (e.touches.length === 1) {
            this.isDragging = true;
            this.lastMouseX = e.touches[0].clientX;
            this.lastMouseY = e.touches[0].clientY;
        }
    }
    
    onTouchMove(e) {
        e.preventDefault();
        if (e.touches.length === 1 && this.isDragging) {
            const deltaX = e.touches[0].clientX - this.lastMouseX;
            const deltaY = e.touches[0].clientY - this.lastMouseY;
            
            this.controls.rotationX += deltaX * 0.01;
            this.controls.rotationY += deltaY * 0.01;
            
            this.controls.rotationY = Math.max(-Math.PI/2, Math.min(Math.PI/2, this.controls.rotationY));
            
            this.lastMouseX = e.touches[0].clientX;
            this.lastMouseY = e.touches[0].clientY;
        }
    }
    
    onTouchEnd() {
        this.isDragging = false;
    }
    
    // === CONTROL BUTTONS ===
    rotateLeft() {
        this.controls.rotationX -= 0.1;
    }
    
    rotateRight() {
        this.controls.rotationX += 0.1;
    }
    
    lookUp() {
        this.controls.rotationY -= 0.1;
        this.controls.rotationY = Math.max(-Math.PI/2, this.controls.rotationY);
    }
    
    lookDown() {
        this.controls.rotationY += 0.1;
        this.controls.rotationY = Math.min(Math.PI/2, this.controls.rotationY);
    }
    
    zoomIn() {
        this.controls.zoom *= 1.1;
        this.controls.zoom = Math.min(3, this.controls.zoom);
    }
    
    zoomOut() {
        this.controls.zoom *= 0.9;
        this.controls.zoom = Math.max(0.5, this.controls.zoom);
    }
    
    // === NAVIGATION ===
    toggleFullscreen() {
        const container = document.getElementById('streetview-container');
        
        if (!document.fullscreenElement) {
            container.requestFullscreen().then(() => {
                container.classList.add('fullscreen');
                this.onResize();
            });
        } else {
            document.exitFullscreen().then(() => {
                container.classList.remove('fullscreen');
                this.onResize();
            });
        }
    }
    
    showInfo() {
        document.getElementById('modalInfo').style.display = 'block';
    }
    
    goBack() {
        window.history.back();
    }
    
    retry() {
        if (this.currentPoint) {
            this.loadPointImage(this.currentPoint);
        }
    }
    
    closeModal() {
        document.querySelectorAll('.modal').forEach(modal => {
            modal.style.display = 'none';
        });
    }
    
    // === POINTS MANAGEMENT ===
    async loadPoints() {
        try {
            // Simular carga de puntos desde la API
            // En producción, esto vendría de /api/campuses/recorridos/
            this.points = [
                {
                    id: 1,
                    titulo: "Entrada Principal",
                    descripcion: "Acceso principal al campus de Duoc UC Maipú",
                    imagen_360_url: "/images/streetview/entrada_360.jpg",
                    lat: -33.5118,
                    lng: -70.7526,
                    orden: 1
                },
                {
                    id: 2,
                    titulo: "Biblioteca",
                    descripcion: "Centro de recursos de aprendizaje y estudio",
                    imagen_360_url: "/images/streetview/biblioteca_360.jpg",
                    lat: -33.5115,
                    lng: -70.7523,
                    orden: 2
                },
                {
                    id: 3,
                    titulo: "Laboratorio de Informática",
                    descripcion: "Laboratorios equipados para clases de programación",
                    imagen_360_url: "/images/streetview/lab_info_360.jpg",
                    lat: -33.5112,
                    lng: -70.7520,
                    orden: 3
                }
            ];
            
            this.renderPointsList();
            
        } catch (error) {
            console.error('Error cargando puntos:', error);
            this.showError('Error cargando puntos de interés');
        }
    }
    
    renderPointsList() {
        const container = document.getElementById('points-list');
        if (!container) return;
        
        container.innerHTML = this.points.map(point => `
            <div class="point-item ${point === this.currentPoint ? 'active' : ''}" 
                 data-point-id="${point.id}">
                <span class="point-order">${point.orden}</span>
                <h4>${point.titulo}</h4>
                <p>${point.descripcion}</p>
            </div>
        `).join('');
        
        // Event listeners para los puntos
        container.querySelectorAll('.point-item').forEach(item => {
            item.addEventListener('click', () => {
                const pointId = parseInt(item.dataset.pointId);
                const point = this.points.find(p => p.id === pointId);
                if (point) {
                    this.loadPointImage(point);
                    this.updateActivePoint(point);
                }
            });
        });
    }
    
    updateActivePoint(point) {
        document.querySelectorAll('.point-item').forEach(item => {
            item.classList.remove('active');
        });
        
        const activeItem = document.querySelector(`[data-point-id="${point.id}"]`);
        if (activeItem) {
            activeItem.classList.add('active');
        }
    }
    
    updatePointInfo(point) {
        document.getElementById('point-title').textContent = point.titulo;
        document.getElementById('point-description').textContent = point.descripcion;
        document.getElementById('point-coords').textContent = 
            `Lat: ${point.lat.toFixed(4)}, Lng: ${point.lng.toFixed(4)}`;
    }
    
    // === UI HELPERS ===
    showLoading() {
        document.getElementById('loading').style.display = 'block';
        document.getElementById('error').style.display = 'none';
        document.getElementById('streetview-canvas').style.display = 'none';
    }
    
    hideLoading() {
        document.getElementById('loading').style.display = 'none';
        document.getElementById('streetview-canvas').style.display = 'block';
    }
    
    showError(message) {
        document.getElementById('loading').style.display = 'none';
        document.getElementById('error').style.display = 'block';
        document.getElementById('streetview-canvas').style.display = 'none';
        
        const errorText = document.querySelector('#error p');
        if (errorText) {
            errorText.textContent = message;
        }
    }
    
    // === RESIZE ===
    onResize() {
        if (!this.camera || !this.renderer) return;
        
        const container = document.getElementById('streetview-container');
        const width = container.clientWidth;
        const height = container.clientHeight;
        
        this.camera.aspect = width / height;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(width, height);
    }
}

// Inicializar cuando se carga la página
document.addEventListener('DOMContentLoaded', () => {
    new StreetViewApp();
});
