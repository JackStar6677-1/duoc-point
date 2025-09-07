// JavaScript para Reportes de Infraestructura

let reportes = [];
let reportesFiltrados = [];
let sedes = [];

// Inicialización
document.addEventListener('DOMContentLoaded', function() {
    cargarSedes();
    cargarReportes();
    configurarEventos();
});

// Configurar eventos
function configurarEventos() {
    document.getElementById('btnNuevoReporte').addEventListener('click', mostrarNuevoReporte);
    document.getElementById('sedeSelect').addEventListener('change', filtrarReportes);
    document.getElementById('estadoSelect').addEventListener('change', filtrarReportes);
    document.getElementById('categoriaSelect').addEventListener('change', filtrarReportes);
}

// Cargar sedes
async function cargarSedes() {
    try {
        const response = await fetch('/api/campuses/sedes');
        if (!response.ok) {
            throw new Error('Error al cargar sedes');
        }
        
        const data = await response.json();
        sedes = data.results || data;
        
        // Llenar selectores de sedes
        const sedeSelect = document.getElementById('sedeSelect');
        const sedeReporte = document.getElementById('sedeReporte');
        
        sedes.forEach(sede => {
            const option1 = new Option(sede.nombre, sede.slug);
            const option2 = new Option(sede.nombre, sede.id);
            sedeSelect.add(option1);
            sedeReporte.add(option2);
        });
    } catch (error) {
        console.error('Error al cargar sedes:', error);
    }
}

// Cargar reportes
async function cargarReportes() {
    try {
        const token = localStorage.getItem('token');
        if (!token) {
            mostrarError('Debes iniciar sesión para ver los reportes');
            return;
        }

        const response = await fetch('/api/reports/reportes', {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error('Error al cargar reportes');
        }

        const data = await response.json();
        reportes = data.results || data;
        reportesFiltrados = [...reportes];
        mostrarReportes();
    } catch (error) {
        console.error('Error:', error);
        mostrarError('Error al cargar los reportes');
    }
}

// Filtrar reportes
function filtrarReportes() {
    const sede = document.getElementById('sedeSelect').value;
    const estado = document.getElementById('estadoSelect').value;
    const categoria = document.getElementById('categoriaSelect').value;

    reportesFiltrados = reportes.filter(reporte => {
        const cumpleSede = !sede || reporte.sede === sede;
        const cumpleEstado = !estado || reporte.estado === estado;
        const cumpleCategoria = !categoria || reporte.categoria === categoria;
        return cumpleSede && cumpleEstado && cumpleCategoria;
    });

    mostrarReportes();
}

// Mostrar reportes
function mostrarReportes() {
    const container = document.getElementById('listaReportes');
    
    if (reportesFiltrados.length === 0) {
        container.innerHTML = `
            <div class="col-12">
                <div class="empty-state">
                    <i class="bi bi-exclamation-triangle"></i>
                    <h3>No hay reportes</h3>
                    <p>No se encontraron reportes para los filtros seleccionados.</p>
                </div>
            </div>
        `;
        return;
    }

    container.innerHTML = reportesFiltrados.map(reporte => `
        <div class="col-md-6 col-lg-4">
            <div class="reporte-card">
                <div class="reporte-card-header">
                    <h5 class="reporte-titulo">${reporte.categoria}</h5>
                    <span class="reporte-estado ${reporte.estado}">
                        ${reporte.estado.charAt(0).toUpperCase() + reporte.estado.slice(1)}
                    </span>
                </div>
                <div class="reporte-card-body">
                    <div class="reporte-meta">
                        <span class="reporte-categoria">${reporte.categoria}</span>
                        <span>${new Date(reporte.creado_at).toLocaleDateString()}</span>
                    </div>
                    <p class="reporte-descripcion">
                        ${reporte.descripcion.length > 100 ? 
                            reporte.descripcion.substring(0, 100) + '...' : 
                            reporte.descripcion}
                    </p>
                    <div class="reporte-actions">
                        <button class="btn btn-ver-reporte" onclick="verReporte(${reporte.id})">
                            <i class="bi bi-eye"></i> Ver Detalles
                        </button>
                    </div>
                </div>
            </div>
        </div>
    `).join('');
}

// Mostrar modal de nuevo reporte
function mostrarNuevoReporte() {
    const modal = new bootstrap.Modal(document.getElementById('nuevoReporteModal'));
    modal.show();
    
    // Obtener ubicación actual si es posible
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function(position) {
                document.getElementById('latitudReporte').value = position.coords.latitude;
                document.getElementById('longitudReporte').value = position.coords.longitude;
            },
            function(error) {
                console.log('No se pudo obtener la ubicación:', error);
            }
        );
    }
}

// Enviar nuevo reporte
async function enviarReporte() {
    try {
        const token = localStorage.getItem('token');
        if (!token) {
            mostrarError('Debes iniciar sesión para enviar reportes');
            return;
        }

        const formData = new FormData();
        formData.append('sede', document.getElementById('sedeReporte').value);
        formData.append('categoria', document.getElementById('categoriaReporte').value);
        formData.append('descripcion', document.getElementById('descripcionReporte').value);
        formData.append('lat', document.getElementById('latitudReporte').value || 0);
        formData.append('lng', document.getElementById('longitudReporte').value || 0);

        const imagen = document.getElementById('imagenReporte').files[0];
        if (imagen) {
            formData.append('media', imagen);
        }

        const response = await fetch('/api/reports/reportes', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`
            },
            body: formData
        });

        if (!response.ok) {
            throw new Error('Error al enviar el reporte');
        }

        // Cerrar modal y recargar reportes
        const modal = bootstrap.Modal.getInstance(document.getElementById('nuevoReporteModal'));
        modal.hide();
        
        // Limpiar formulario
        document.getElementById('formNuevoReporte').reset();
        
        // Recargar reportes
        await cargarReportes();
        
        // Mostrar mensaje de éxito
        mostrarExito('Reporte enviado exitosamente');
    } catch (error) {
        console.error('Error:', error);
        mostrarError('Error al enviar el reporte');
    }
}

// Ver reporte completo
async function verReporte(id) {
    try {
        const token = localStorage.getItem('token');
        const response = await fetch(`/api/reports/reportes/${id}`, {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error('Error al cargar el reporte');
        }

        const reporte = await response.json();
        
        // Mostrar en modal
        document.getElementById('modalTituloReporte').textContent = reporte.categoria;
        document.getElementById('modalContenidoReporte').innerHTML = `
            <div class="mb-3">
                <span class="reporte-estado ${reporte.estado}">
                    ${reporte.estado.charAt(0).toUpperCase() + reporte.estado.slice(1)}
                </span>
                <span class="reporte-categoria ms-2">${reporte.categoria}</span>
            </div>
            <div class="mb-3">
                <h6>Descripción:</h6>
                <p>${reporte.descripcion}</p>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <h6>Información:</h6>
                    <p><strong>Sede:</strong> ${reporte.sede_nombre || 'No especificada'}</p>
                    <p><strong>Fecha:</strong> ${new Date(reporte.creado_at).toLocaleString()}</p>
                    <p><strong>Prioridad:</strong> ${reporte.prioridad}</p>
                </div>
                <div class="col-md-6">
                    <h6>Ubicación:</h6>
                    <p><strong>Latitud:</strong> ${reporte.lat}</p>
                    <p><strong>Longitud:</strong> ${reporte.lng}</p>
                </div>
            </div>
            ${reporte.media && reporte.media.length > 0 ? `
                <div class="mt-3">
                    <h6>Imágenes:</h6>
                    ${reporte.media.map(media => `
                        <img src="${media.url}" alt="Imagen del reporte" class="reporte-imagen">
                    `).join('')}
                </div>
            ` : ''}
        `;

        const modal = new bootstrap.Modal(document.getElementById('verReporteModal'));
        modal.show();
    } catch (error) {
        console.error('Error:', error);
        mostrarError('Error al cargar el reporte');
    }
}

// Mostrar error
function mostrarError(mensaje) {
    const container = document.getElementById('listaReportes');
    container.innerHTML = `
        <div class="col-12">
            <div class="alert alert-danger" role="alert">
                <i class="bi bi-exclamation-triangle"></i>
                ${mensaje}
            </div>
        </div>
    `;
}

// Mostrar éxito
function mostrarExito(mensaje) {
    // Crear toast de éxito
    const toast = document.createElement('div');
    toast.className = 'toast align-items-center text-white bg-success border-0';
    toast.setAttribute('role', 'alert');
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                <i class="bi bi-check-circle"></i> ${mensaje}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
        </div>
    `;
    
    document.body.appendChild(toast);
    const bsToast = new bootstrap.Toast(toast);
    bsToast.show();
    
    // Remover del DOM después de que se oculte
    toast.addEventListener('hidden.bs.toast', () => {
        document.body.removeChild(toast);
    });
}
