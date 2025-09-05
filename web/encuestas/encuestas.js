/**
 * Sistema de Encuestas DuocPoint
 * Interfaz completa para gestión y participación en encuestas
 */

class EncuestasApp {
    constructor() {
        this.apiBaseUrl = '/api';
        this.currentUser = null;
        this.currentView = 'encuestas';
        this.encuestas = [];
        this.filtros = {};
        this.charts = {};
        
        this.init();
    }
    
    async init() {
        await this.checkAuth();
        this.setupEventListeners();
        this.loadEncuestas();
        this.setupChartDefaults();
    }
    
    // === AUTENTICACIÓN ===
    async checkAuth() {
        const token = localStorage.getItem('authToken');
        if (!token) {
            this.redirectToLogin();
            return;
        }
        
        try {
            const response = await fetch(`${this.apiBaseUrl}/me`, {
                headers: { 'Authorization': `Bearer ${token}` }
            });
            
            if (response.ok) {
                this.currentUser = await response.json();
                this.updateUIForUser();
            } else {
                this.redirectToLogin();
            }
        } catch (error) {
            console.error('Error verificando autenticación:', error);
            this.redirectToLogin();
        }
    }
    
    redirectToLogin() {
        window.location.href = '/api/auth/login';
    }
    
    updateUIForUser() {
        const canCreate = ['moderator', 'director_carrera', 'admin_global'].includes(this.currentUser.role);
        
        document.getElementById('btnCrearEncuesta').style.display = canCreate ? 'flex' : 'none';
        document.getElementById('btnMisEncuestas').style.display = canCreate ? 'flex' : 'none';
        document.getElementById('btnDashboard').style.display = canCreate ? 'flex' : 'none';
    }
    
    // === EVENT LISTENERS ===
    setupEventListeners() {
        // Navegación
        document.getElementById('btnCrearEncuesta').addEventListener('click', () => this.mostrarModalCrear());
        document.getElementById('btnMisEncuestas').addEventListener('click', () => this.cargarMisEncuestas());
        document.getElementById('btnDashboard').addEventListener('click', () => this.mostrarDashboard());
        
        // Filtros
        document.getElementById('btnFiltrar').addEventListener('click', () => this.aplicarFiltros());
        document.getElementById('btnLimpiarFiltros').addEventListener('click', () => this.limpiarFiltros());
        
        // Modales
        document.querySelectorAll('.modal-close').forEach(btn => {
            btn.addEventListener('click', (e) => this.cerrarModal(e.target.closest('.modal')));
        });
        
        // Formulario crear encuesta
        document.getElementById('formCrearEncuesta').addEventListener('submit', (e) => this.crearEncuesta(e));
        document.getElementById('btnAgregarOpcion').addEventListener('click', () => this.agregarOpcion());
        
        // Acciones de encuesta
        document.getElementById('btnVotar').addEventListener('click', () => this.votarEncuesta());
        document.getElementById('btnExportar').addEventListener('click', () => this.exportarEncuesta());
        document.getElementById('btnCerrarEncuesta').addEventListener('click', () => this.cerrarEncuesta());
        
        // Cerrar modales al hacer clic fuera
        window.addEventListener('click', (e) => {
            if (e.target.classList.contains('modal')) {
                this.cerrarModal(e.target);
            }
        });
        
        // Búsqueda en tiempo real
        let searchTimeout;
        document.getElementById('busqueda').addEventListener('input', (e) => {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                this.filtros.busqueda = e.target.value;
                this.aplicarFiltros();
            }, 500);
        });
    }
    
    // === CARGA DE DATOS ===
    async loadEncuestas(filtros = {}) {
        this.mostrarLoading(true);
        
        try {
            const params = new URLSearchParams(filtros);
            const response = await this.fetchWithAuth(`${this.apiBaseUrl}/polls/?${params}`);
            
            if (response.ok) {
                const data = await response.json();
                this.encuestas = data.results || data;
                this.renderEncuestas();
            } else {
                this.showToast('Error cargando encuestas', 'error');
            }
        } catch (error) {
            console.error('Error cargando encuestas:', error);
            this.showToast('Error de conexión', 'error');
        } finally {
            this.mostrarLoading(false);
        }
    }
    
    async cargarMisEncuestas() {
        this.currentView = 'mis-encuestas';
        this.mostrarSeccion('encuestasSection');
        
        try {
            const response = await this.fetchWithAuth(`${this.apiBaseUrl}/polls/mis-encuestas/`);
            if (response.ok) {
                const data = await response.json();
                this.encuestas = data.results || data;
                this.renderEncuestas();
            }
        } catch (error) {
            console.error('Error cargando mis encuestas:', error);
            this.showToast('Error cargando mis encuestas', 'error');
        }
    }
    
    async mostrarDashboard() {
        this.currentView = 'dashboard';
        this.mostrarSeccion('dashboardSection');
        
        try {
            const response = await this.fetchWithAuth(`${this.apiBaseUrl}/polls/dashboard/`);
            if (response.ok) {
                const data = await response.json();
                this.renderDashboard(data);
            }
        } catch (error) {
            console.error('Error cargando dashboard:', error);
            this.showToast('Error cargando dashboard', 'error');
        }
    }
    
    // === RENDERIZADO ===
    renderEncuestas() {
        const container = document.getElementById('encuestasList');
        const noResults = document.getElementById('noResults');
        
        if (this.encuestas.length === 0) {
            container.innerHTML = '';
            noResults.style.display = 'block';
            return;
        }
        
        noResults.style.display = 'none';
        
        container.innerHTML = this.encuestas.map(encuesta => `
            <div class="encuesta-card" onclick="encuestasApp.verEncuesta(${encuesta.id})">
                <div class="encuesta-header">
                    <h3 class="encuesta-titulo">${encuesta.titulo}</h3>
                    <span class="encuesta-estado estado-${encuesta.estado}">
                        ${this.getEstadoLabel(encuesta.estado)}
                    </span>
                </div>
                
                <p class="encuesta-descripcion">${encuesta.descripcion || 'Sin descripción'}</p>
                
                <div class="encuesta-meta">
                    <span>Por: ${encuesta.creador_nombre}</span>
                    <span>${this.formatFecha(encuesta.created_at)}</span>
                </div>
                
                <div class="encuesta-stats">
                    <div class="stat-item">
                        <i class="bi bi-people"></i>
                        <span>${encuesta.total_votos} votos</span>
                    </div>
                    ${encuesta.cierra_at ? `
                        <div class="stat-item">
                            <i class="bi bi-calendar"></i>
                            <span>Cierra: ${this.formatFecha(encuesta.cierra_at)}</span>
                        </div>
                    ` : ''}
                </div>
                
                <div class="encuesta-actions">
                    ${encuesta.puede_votar ? 
                        '<span class="puede-votar"><i class="bi bi-check-circle"></i> Puedes votar</span>' :
                        '<span class="no-puede-votar"><i class="bi bi-x-circle"></i> No puedes votar</span>'
                    }
                    <i class="bi bi-arrow-right"></i>
                </div>
            </div>
        `).join('');
    }
    
    renderDashboard(data) {
        // Estadísticas principales
        document.getElementById('totalEncuestas').textContent = data.estadisticas.total_encuestas;
        document.getElementById('encuestasActivas').textContent = data.estadisticas.encuestas_activas;
        document.getElementById('misEncuestasCount').textContent = data.estadisticas.mis_encuestas;
        document.getElementById('actividadReciente').textContent = data.estadisticas.actividad_reciente;
        
        // Gráfico de top encuestas
        this.renderTopEncuestasChart(data.top_encuestas);
    }
    
    renderTopEncuestasChart(topEncuestas) {
        const ctx = document.getElementById('topEncuestasChart');
        if (!ctx) return;
        
        if (this.charts.topEncuestas) {
            this.charts.topEncuestas.destroy();
        }
        
        this.charts.topEncuestas = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: topEncuestas.map(e => e.titulo.substring(0, 30) + '...'),
                datasets: [{
                    label: 'Participantes',
                    data: topEncuestas.map(e => e.participantes),
                    backgroundColor: 'rgba(255, 215, 0, 0.8)',
                    borderColor: '#ffd700',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: { color: '#ffd700' },
                        grid: { color: 'rgba(255, 215, 0, 0.1)' }
                    },
                    x: {
                        ticks: { color: '#ffd700' },
                        grid: { display: false }
                    }
                }
            }
        });
    }
    
    // === MODAL CREAR ENCUESTA ===
    mostrarModalCrear() {
        const modal = document.getElementById('modalCrearEncuesta');
        this.limpiarFormularioCrear();
        this.agregarOpcion(); // Agregar 2 opciones por defecto
        this.agregarOpcion();
        modal.style.display = 'block';
    }
    
    limpiarFormularioCrear() {
        document.getElementById('formCrearEncuesta').reset();
        document.getElementById('opcionesList').innerHTML = '';
        
        // Establecer fecha/hora por defecto
        const ahora = new Date();
        ahora.setMinutes(ahora.getMinutes() - ahora.getTimezoneOffset());
        document.getElementById('inputInicia').value = ahora.toISOString().slice(0, 16);
        
        const enUnaHora = new Date(ahora.getTime() + 60 * 60 * 1000);
        document.getElementById('inputCierra').value = enUnaHora.toISOString().slice(0, 16);
    }
    
    agregarOpcion() {
        const container = document.getElementById('opcionesList');
        const index = container.children.length;
        
        const opcionDiv = document.createElement('div');
        opcionDiv.className = 'opcion-item';
        opcionDiv.innerHTML = `
            <input type="text" placeholder="Texto de la opción" required>
            <input type="text" placeholder="Descripción (opcional)">
            <input type="color" value="#ffd700" title="Color">
            <button type="button" class="btn btn-danger" onclick="this.parentElement.remove()">
                <i class="bi bi-trash"></i>
            </button>
        `;
        
        container.appendChild(opcionDiv);
    }
    
    async crearEncuesta(e) {
        e.preventDefault();
        
        const formData = new FormData(e.target);
        const opciones = this.recopilarOpciones();
        
        if (opciones.length < 2) {
            this.showToast('Se requieren al menos 2 opciones', 'error');
            return;
        }
        
        const data = {
            titulo: document.getElementById('inputTitulo').value,
            descripcion: document.getElementById('inputDescripcion').value,
            multi: document.getElementById('inputMulti').checked,
            anonima: document.getElementById('inputAnonima').checked,
            requiere_justificacion: document.getElementById('inputRequiereJustificacion').checked,
            mostrar_resultados: document.getElementById('inputMostrarResultados').value,
            inicia_at: document.getElementById('inputInicia').value,
            cierra_at: document.getElementById('inputCierra').value || null,
            carreras: this.parseCarreras(document.getElementById('inputCarreras').value),
            opciones: opciones
        };
        
        try {
            const response = await this.fetchWithAuth(`${this.apiBaseUrl}/polls/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            
            if (response.ok) {
                this.showToast('Encuesta creada exitosamente', 'success');
                this.cerrarModal(document.getElementById('modalCrearEncuesta'));
                this.loadEncuestas();
            } else {
                const error = await response.json();
                this.showToast(`Error: ${JSON.stringify(error)}`, 'error');
            }
        } catch (error) {
            console.error('Error creando encuesta:', error);
            this.showToast('Error de conexión', 'error');
        }
    }
    
    recopilarOpciones() {
        const opciones = [];
        const items = document.querySelectorAll('#opcionesList .opcion-item');
        
        items.forEach((item, index) => {
            const inputs = item.querySelectorAll('input');
            const texto = inputs[0].value.trim();
            
            if (texto) {
                opciones.push({
                    texto: texto,
                    descripcion: inputs[1].value.trim(),
                    orden: index,
                    color: inputs[2].value
                });
            }
        });
        
        return opciones;
    }
    
    parseCarreras(carrerasStr) {
        if (!carrerasStr.trim()) return [];
        return carrerasStr.split(',').map(c => c.trim()).filter(c => c.length > 0);
    }
    
    // === VER ENCUESTA ===
    async verEncuesta(id) {
        try {
            const response = await this.fetchWithAuth(`${this.apiBaseUrl}/polls/${id}/`);
            if (response.ok) {
                const encuesta = await response.json();
                this.mostrarModalVerEncuesta(encuesta);
            }
        } catch (error) {
            console.error('Error cargando encuesta:', error);
            this.showToast('Error cargando encuesta', 'error');
        }
    }
    
    mostrarModalVerEncuesta(encuesta) {
        const modal = document.getElementById('modalVerEncuesta');
        document.getElementById('modalTitulo').textContent = encuesta.titulo;
        
        // Detalles de la encuesta
        const detalleHTML = `
            <div class="encuesta-info">
                <p><strong>Descripción:</strong> ${encuesta.descripcion || 'Sin descripción'}</p>
                <p><strong>Creador:</strong> ${encuesta.creador_nombre}</p>
                <p><strong>Estado:</strong> <span class="estado-${encuesta.estado}">${this.getEstadoLabel(encuesta.estado)}</span></p>
                <p><strong>Total votos:</strong> ${encuesta.total_votos}</p>
                ${encuesta.cierra_at ? `<p><strong>Cierra:</strong> ${this.formatFecha(encuesta.cierra_at)}</p>` : ''}
                <p><strong>Tipo:</strong> ${encuesta.multi ? 'Múltiple selección' : 'Selección única'}</p>
            </div>
        `;
        document.getElementById('encuestaDetalle').innerHTML = detalleHTML;
        
        // Mostrar opciones para votar o resultados
        if (encuesta.puede_votar) {
            this.mostrarOpcionesVotacion(encuesta);
        } else if (encuesta.puede_ver_resultados) {
            this.mostrarResultados(encuesta);
        } else {
            document.getElementById('opcionesVotacion').innerHTML = '<p>No puedes ver los resultados de esta encuesta aún.</p>';
            document.getElementById('resultadosGrafico').style.display = 'none';
        }
        
        // Mostrar analytics si están disponibles
        if (encuesta.analytics) {
            this.mostrarAnalytics(encuesta.analytics);
        }
        
        // Configurar botones del modal
        this.configurarBotonesModal(encuesta);
        
        modal.style.display = 'block';
        this.currentEncuesta = encuesta;
    }
    
    mostrarOpcionesVotacion(encuesta) {
        const container = document.getElementById('opcionesVotacion');
        const inputType = encuesta.multi ? 'checkbox' : 'radio';
        
        container.innerHTML = `
            <h4>Selecciona tu respuesta:</h4>
            ${encuesta.opciones.map(opcion => `
                <div class="opcion-voto">
                    <input type="${inputType}" name="voto" value="${opcion.id}" id="opcion_${opcion.id}">
                    <label for="opcion_${opcion.id}">
                        <strong>${opcion.texto}</strong>
                        ${opcion.descripcion ? `<br><small>${opcion.descripcion}</small>` : ''}
                    </label>
                </div>
            `).join('')}
            
            ${encuesta.requiere_justificacion ? `
                <div class="form-group">
                    <label for="justificacion">Justificación:</label>
                    <textarea id="justificacion" rows="3" placeholder="Explica tu elección..."></textarea>
                </div>
            ` : ''}
        `;
        
        document.getElementById('resultadosGrafico').style.display = 'none';
        document.getElementById('btnVotar').style.display = 'flex';
    }
    
    mostrarResultados(encuesta) {
        const container = document.getElementById('opcionesVotacion');
        
        container.innerHTML = `
            <h4>Resultados:</h4>
            ${encuesta.opciones.map(opcion => `
                <div class="resultado-opcion">
                    <div class="resultado-header">
                        <span class="resultado-texto">${opcion.texto}</span>
                        <span class="resultado-stats">${opcion.votos} votos (${opcion.porcentaje}%)</span>
                    </div>
                    <div class="resultado-barra">
                        <div class="resultado-progreso" style="width: ${opcion.porcentaje}%"></div>
                    </div>
                </div>
            `).join('')}
        `;
        
        // Mostrar gráfico
        this.mostrarGraficoResultados(encuesta);
        document.getElementById('btnVotar').style.display = 'none';
    }
    
    mostrarGraficoResultados(encuesta) {
        const container = document.getElementById('resultadosGrafico');
        container.style.display = 'block';
        
        const ctx = document.getElementById('resultadosChart');
        if (this.charts.resultados) {
            this.charts.resultados.destroy();
        }
        
        const colores = encuesta.opciones.map(o => o.color || '#ffd700');
        
        this.charts.resultados = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: encuesta.opciones.map(o => o.texto),
                datasets: [{
                    data: encuesta.opciones.map(o => o.votos),
                    backgroundColor: colores,
                    borderColor: colores.map(c => c + '80'),
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: { color: '#ffd700' }
                    }
                }
            }
        });
    }
    
    mostrarAnalytics(analytics) {
        const container = document.getElementById('analyticsDetalle');
        
        container.innerHTML = `
            <h4>Análisis Detallado</h4>
            <div class="analytics-grid">
                <div class="analytics-card">
                    <h4>Por Sede</h4>
                    <ul class="analytics-list">
                        ${Object.entries(analytics.distribucion_sedes).map(([sede, count]) => `
                            <li><span>${sede}</span><span>${count}</span></li>
                        `).join('')}
                    </ul>
                </div>
                
                <div class="analytics-card">
                    <h4>Por Carrera</h4>
                    <ul class="analytics-list">
                        ${Object.entries(analytics.distribucion_carreras).map(([carrera, count]) => `
                            <li><span>${carrera}</span><span>${count}</span></li>
                        `).join('')}
                    </ul>
                </div>
            </div>
            <p><small>Última actualización: ${this.formatFecha(analytics.ultima_actualizacion)}</small></p>
        `;
    }
    
    configurarBotonesModal(encuesta) {
        const btnExportar = document.getElementById('btnExportar');
        const btnCerrar = document.getElementById('btnCerrarEncuesta');
        
        const puedeGestionar = encuesta.creador_nombre === this.currentUser.name || 
                              ['moderator', 'director_carrera', 'admin_global'].includes(this.currentUser.role);
        
        btnExportar.style.display = encuesta.puede_ver_resultados ? 'flex' : 'none';
        btnCerrar.style.display = (puedeGestionar && encuesta.estado === 'activa') ? 'flex' : 'none';
    }
    
    // === ACCIONES DE ENCUESTA ===
    async votarEncuesta() {
        const opciones = [];
        const inputs = document.querySelectorAll('input[name="voto"]:checked');
        
        if (inputs.length === 0) {
            this.showToast('Selecciona al menos una opción', 'error');
            return;
        }
        
        inputs.forEach(input => opciones.push(parseInt(input.value)));
        
        const data = {
            opciones: opciones,
            justificacion: document.getElementById('justificacion')?.value || ''
        };
        
        try {
            const response = await this.fetchWithAuth(
                `${this.apiBaseUrl}/polls/${this.currentEncuesta.id}/votar/`,
                {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                }
            );
            
            if (response.ok) {
                this.showToast('Voto registrado exitosamente', 'success');
                this.cerrarModal(document.getElementById('modalVerEncuesta'));
                this.loadEncuestas();
            } else {
                const error = await response.json();
                this.showToast(`Error: ${JSON.stringify(error)}`, 'error');
            }
        } catch (error) {
            console.error('Error votando:', error);
            this.showToast('Error de conexión', 'error');
        }
    }
    
    async exportarEncuesta() {
        try {
            const response = await this.fetchWithAuth(
                `${this.apiBaseUrl}/polls/${this.currentEncuesta.id}/export/`,
                {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        formato: 'csv',
                        incluir_metadatos: true,
                        incluir_justificaciones: true
                    })
                }
            );
            
            if (response.ok) {
                const blob = await response.blob();
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `encuesta_${this.currentEncuesta.id}_resultados.csv`;
                a.click();
                window.URL.revokeObjectURL(url);
                this.showToast('Archivo descargado', 'success');
            }
        } catch (error) {
            console.error('Error exportando:', error);
            this.showToast('Error exportando', 'error');
        }
    }
    
    async cerrarEncuesta() {
        if (!confirm('¿Estás seguro de que quieres cerrar esta encuesta?')) return;
        
        try {
            const response = await this.fetchWithAuth(
                `${this.apiBaseUrl}/polls/${this.currentEncuesta.id}/cerrar/`,
                { method: 'POST' }
            );
            
            if (response.ok) {
                this.showToast('Encuesta cerrada exitosamente', 'success');
                this.cerrarModal(document.getElementById('modalVerEncuesta'));
                this.loadEncuestas();
            }
        } catch (error) {
            console.error('Error cerrando encuesta:', error);
            this.showToast('Error cerrando encuesta', 'error');
        }
    }
    
    // === FILTROS ===
    aplicarFiltros() {
        this.filtros = {
            estado: document.getElementById('filtroEstado').value,
            fecha_desde: document.getElementById('filtroFecha').value,
            busqueda: document.getElementById('busqueda').value
        };
        
        // Limpiar filtros vacíos
        Object.keys(this.filtros).forEach(key => {
            if (!this.filtros[key]) delete this.filtros[key];
        });
        
        this.loadEncuestas(this.filtros);
    }
    
    limpiarFiltros() {
        document.getElementById('filtroEstado').value = '';
        document.getElementById('filtroFecha').value = '';
        document.getElementById('busqueda').value = '';
        this.filtros = {};
        this.loadEncuestas();
    }
    
    // === UTILIDADES ===
    async fetchWithAuth(url, options = {}) {
        const token = localStorage.getItem('authToken');
        return fetch(url, {
            ...options,
            headers: {
                ...options.headers,
                'Authorization': `Bearer ${token}`
            }
        });
    }
    
    mostrarSeccion(seccionId) {
        document.querySelectorAll('.main-content > section').forEach(section => {
            section.style.display = 'none';
        });
        document.getElementById(seccionId).style.display = 'block';
    }
    
    mostrarLoading(show) {
        document.getElementById('loading').style.display = show ? 'block' : 'none';
    }
    
    cerrarModal(modal) {
        modal.style.display = 'none';
        
        // Limpiar gráficos
        Object.values(this.charts).forEach(chart => {
            if (chart && typeof chart.destroy === 'function') {
                chart.destroy();
            }
        });
        this.charts = {};
    }
    
    showToast(message, type = 'info') {
        const toast = document.getElementById('toast');
        const messageEl = document.getElementById('toastMessage');
        
        messageEl.textContent = message;
        toast.className = `toast ${type}`;
        toast.classList.add('show');
        
        setTimeout(() => {
            toast.classList.remove('show');
        }, 3000);
    }
    
    setupChartDefaults() {
        Chart.defaults.color = '#ffd700';
        Chart.defaults.borderColor = 'rgba(255, 215, 0, 0.2)';
        Chart.defaults.backgroundColor = 'rgba(255, 215, 0, 0.1)';
    }
    
    getEstadoLabel(estado) {
        const labels = {
            'activa': 'Activa',
            'cerrada': 'Cerrada',
            'borrador': 'Borrador',
            'archivada': 'Archivada'
        };
        return labels[estado] || estado;
    }
    
    formatFecha(fechaStr) {
        const fecha = new Date(fechaStr);
        return fecha.toLocaleDateString('es-CL', {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
    }
}

// Inicializar aplicación cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    window.encuestasApp = new EncuestasApp();
});

// Registrar Service Worker para PWA
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/service-worker.js');
}
