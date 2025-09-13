/**
 * Polls Manager - StudentsPoint
 * Sistema completo de encuestas y votaciones
 */

class PollsManager {
    constructor() {
        this.polls = [];
        this.currentFilter = 'all';
        this.currentUser = null;
        this.init();
    }

    async init() {
        await this.loadUser();
        await this.loadPolls();
        this.setupEventListeners();
        this.renderPolls();
    }

    async loadUser() {
        const token = localStorage.getItem('access_token');
        if (token) {
            try {
                const response = await fetch('/api/auth/me/', {
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });
                if (response.ok) {
                    this.currentUser = await response.json();
                }
            } catch (error) {
                console.error('Error loading user:', error);
            }
        }
    }

    async loadPolls() {
        try {
            const token = localStorage.getItem('access_token');
            const headers = {};
            if (token) {
                headers['Authorization'] = `Bearer ${token}`;
            }

            const response = await fetch('/api/polls/', { headers });
            if (response.ok) {
                const data = await response.json();
                this.polls = data.results || data || [];
            } else {
                throw new Error('Error cargando encuestas');
            }
        } catch (error) {
            console.error('Error:', error);
            this.showError('Error cargando encuestas');
        }
    }

    setupEventListeners() {
        // Filtros
        document.getElementById('filterAll')?.addEventListener('click', () => this.setFilter('all'));
        document.getElementById('filterActive')?.addEventListener('click', () => this.setFilter('active'));
        document.getElementById('filterClosed')?.addEventListener('click', () => this.setFilter('closed'));
        document.getElementById('filterMyPolls')?.addEventListener('click', () => this.setFilter('my_polls'));

        // Búsqueda
        document.getElementById('searchInput')?.addEventListener('input', (e) => this.searchPolls(e.target.value));
    }

    setFilter(filter) {
        this.currentFilter = filter;
        this.updateFilterButtons();
        this.renderPolls();
    }

    updateFilterButtons() {
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        document.getElementById(`filter${this.currentFilter.charAt(0).toUpperCase() + this.currentFilter.slice(1)}`)?.classList.add('active');
    }

    searchPolls(query) {
        const filteredPolls = this.polls.filter(poll => 
            poll.titulo.toLowerCase().includes(query.toLowerCase()) ||
            poll.descripcion.toLowerCase().includes(query.toLowerCase()) ||
            poll.categoria.toLowerCase().includes(query.toLowerCase())
        );
        this.renderPolls(filteredPolls);
    }

    renderPolls(pollsToRender = null) {
        const polls = pollsToRender || this.getFilteredPolls();
        const container = document.getElementById('pollsContainer');
        
        if (!container) return;

        if (polls.length === 0) {
            container.innerHTML = `
                <div class="col-12 text-center py-5">
                    <i class="fas fa-poll fa-3x text-muted mb-3"></i>
                    <h4 class="text-muted">No se encontraron encuestas</h4>
                    <p class="text-muted">Intenta con otros filtros o términos de búsqueda</p>
                </div>
            `;
            return;
        }

        container.innerHTML = polls.map(poll => this.createPollCard(poll)).join('');
    }

    getFilteredPolls() {
        const now = new Date();
        
        switch (this.currentFilter) {
            case 'active':
                return this.polls.filter(poll => 
                    poll.estado === 'activa' || 
                    (new Date(poll.fecha_fin) > now && new Date(poll.fecha_inicio) <= now)
                );
            case 'closed':
                return this.polls.filter(poll => 
                    poll.estado === 'cerrada' || 
                    new Date(poll.fecha_fin) <= now
                );
            case 'my_polls':
                return this.polls.filter(poll => 
                    this.currentUser && poll.creador === this.currentUser.id
                );
            default:
                return this.polls;
        }
    }

    createPollCard(poll) {
        const isActive = poll.estado === 'activa' || (new Date(poll.fecha_fin) > new Date());
        const statusBadge = isActive ? 
            '<span class="badge bg-success">Activa</span>' : 
            '<span class="badge bg-secondary">Cerrada</span>';

        const categoryIcons = {
            'academica': 'fas fa-graduation-cap',
            'servicios': 'fas fa-concierge-bell',
            'infraestructura': 'fas fa-building',
            'eventos': 'fas fa-calendar-alt',
            'general': 'fas fa-comments'
        };

        const categoryColors = {
            'academica': 'primary',
            'servicios': 'info',
            'infraestructura': 'warning',
            'eventos': 'success',
            'general': 'secondary'
        };

        return `
            <div class="col-md-6 col-lg-4 mb-4">
                <div class="card poll-card h-100">
                    <div class="card-body">
                        <div class="d-flex justify-content-between align-items-start mb-3">
                            <div class="poll-category">
                                <i class="${categoryIcons[poll.categoria] || 'fas fa-poll'} text-${categoryColors[poll.categoria] || 'primary'}"></i>
                                <span class="badge bg-${categoryColors[poll.categoria] || 'primary'} ms-1">${poll.categoria}</span>
                            </div>
                            ${statusBadge}
                        </div>
                        
                        <h5 class="card-title">${poll.titulo}</h5>
                        <p class="card-text text-muted">${poll.descripcion || 'Sin descripción'}</p>
                        
                        <div class="poll-stats mb-3">
                            <small class="text-muted">
                                <i class="fas fa-users me-1"></i>
                                ${poll.total_votos || 0} votos
                            </small>
                            <small class="text-muted ms-3">
                                <i class="fas fa-clock me-1"></i>
                                ${this.formatDate(poll.fecha_fin)}
                            </small>
                        </div>

                        <div class="poll-actions">
                            <button class="btn btn-outline-primary btn-sm me-2" onclick="pollsManager.viewPollDetail(${poll.id})">
                                <i class="fas fa-eye me-1"></i> Ver
                            </button>
                            ${isActive ? `
                                <button class="btn btn-primary btn-sm" onclick="pollsManager.votePoll(${poll.id})">
                                    <i class="fas fa-vote-yea me-1"></i> Votar
                                </button>
                            ` : ''}
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    async viewPollDetail(pollId) {
        try {
            const token = localStorage.getItem('access_token');
            const headers = {};
            if (token) {
                headers['Authorization'] = `Bearer ${token}`;
            }

            const response = await fetch(`/api/polls/${pollId}/`, { headers });
            if (response.ok) {
                const poll = await response.json();
                this.showPollDetailModal(poll);
            } else {
                throw new Error('Error cargando encuesta');
            }
        } catch (error) {
            console.error('Error:', error);
            this.showError('Error cargando encuesta');
        }
    }

    showPollDetailModal(poll) {
        const modal = new bootstrap.Modal(document.getElementById('pollDetailModal'));
        const modalBody = document.getElementById('pollDetailBody');
        
        const isActive = poll.estado === 'activa' || (new Date(poll.fecha_fin) > new Date());
        const totalVotes = poll.opciones?.reduce((sum, opcion) => sum + (opcion.votos || 0), 0) || 0;

        modalBody.innerHTML = `
            <div class="poll-detail">
                <div class="d-flex justify-content-between align-items-start mb-3">
                    <h4>${poll.titulo}</h4>
                    <span class="badge ${isActive ? 'bg-success' : 'bg-secondary'}">
                        ${isActive ? 'Activa' : 'Cerrada'}
                    </span>
                </div>
                
                <p class="text-muted mb-4">${poll.descripcion || 'Sin descripción'}</p>
                
                <div class="row mb-4">
                    <div class="col-md-6">
                        <strong>Fecha de inicio:</strong><br>
                        <small class="text-muted">${this.formatDate(poll.fecha_inicio)}</small>
                    </div>
                    <div class="col-md-6">
                        <strong>Fecha de fin:</strong><br>
                        <small class="text-muted">${this.formatDate(poll.fecha_fin)}</small>
                    </div>
                </div>

                <h5>Resultados (${totalVotes} votos totales)</h5>
                <div class="poll-results">
                    ${poll.opciones?.map(opcion => {
                        const percentage = totalVotes > 0 ? ((opcion.votos || 0) / totalVotes * 100).toFixed(1) : 0;
                        return `
                            <div class="result-item mb-3">
                                <div class="d-flex justify-content-between mb-1">
                                    <span>${opcion.texto}</span>
                                    <span class="text-muted">${opcion.votos || 0} votos (${percentage}%)</span>
                                </div>
                                <div class="progress">
                                    <div class="progress-bar" style="width: ${percentage}%"></div>
                                </div>
                            </div>
                        `;
                    }).join('') || '<p class="text-muted">No hay opciones disponibles</p>'}
                </div>
            </div>
        `;
        
        modal.show();
    }

    async votePoll(pollId) {
        try {
            const token = localStorage.getItem('access_token');
            if (!token) {
                this.showError('Debes iniciar sesión para votar');
                return;
            }

            // Obtener detalles de la encuesta para mostrar opciones
            const response = await fetch(`/api/polls/${pollId}/`, {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });

            if (response.ok) {
                const poll = await response.json();
                this.showVoteModal(poll);
            } else {
                throw new Error('Error cargando encuesta');
            }
        } catch (error) {
            console.error('Error:', error);
            this.showError('Error cargando encuesta');
        }
    }

    showVoteModal(poll) {
        const modal = new bootstrap.Modal(document.getElementById('voteModal'));
        const modalBody = document.getElementById('voteModalBody');
        
        modalBody.innerHTML = `
            <h5>${poll.titulo}</h5>
            <p class="text-muted">${poll.descripcion || ''}</p>
            
            <form id="voteForm">
                <div class="mb-3">
                    <label class="form-label">Selecciona tu opción:</label>
                    ${poll.opciones?.map((opcion, index) => `
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="opcion" value="${opcion.id}" id="opcion${index}">
                            <label class="form-check-label" for="opcion${index}">
                                ${opcion.texto}
                            </label>
                        </div>
                    `).join('') || '<p class="text-muted">No hay opciones disponibles</p>'}
                </div>
            </form>
        `;
        
        modal.show();
    }

    async submitVote(pollId) {
        try {
            const form = document.getElementById('voteForm');
            const formData = new FormData(form);
            const selectedOption = formData.get('opcion');

            if (!selectedOption) {
                this.showError('Por favor selecciona una opción');
                return;
            }

            const token = localStorage.getItem('access_token');
            const response = await fetch(`/api/polls/${pollId}/votar/`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    opcion_id: selectedOption
                })
            });

            if (response.ok) {
                this.showSuccess('Voto registrado exitosamente');
                bootstrap.Modal.getInstance(document.getElementById('voteModal')).hide();
                await this.loadPolls();
                this.renderPolls();
            } else {
                const error = await response.json();
                throw new Error(error.detail || 'Error al votar');
            }
        } catch (error) {
            console.error('Error:', error);
            this.showError('Error al registrar voto');
        }
    }

    async createPoll() {
        try {
            const form = document.getElementById('createPollForm');
            const formData = new FormData(form);

            const pollData = {
                titulo: document.getElementById('pollTitle').value,
                descripcion: document.getElementById('pollDescription').value,
                categoria: document.getElementById('pollCategory').value,
                opciones: document.getElementById('pollOptions').value.split('\n').filter(opt => opt.trim()),
                fecha_inicio: document.getElementById('pollStartDate').value || new Date().toISOString(),
                fecha_fin: document.getElementById('pollEndDate').value,
                anonima: document.getElementById('pollAnonymous').checked
            };

            if (!pollData.titulo || !pollData.categoria || pollData.opciones.length < 2) {
                this.showError('Por favor completa todos los campos requeridos');
                return;
            }

            const token = localStorage.getItem('access_token');
            if (!token) {
                this.showError('Debes iniciar sesión para crear encuestas');
                return;
            }

            const response = await fetch('/api/polls/', {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(pollData)
            });

            if (response.ok) {
                this.showSuccess('Encuesta creada exitosamente');
                bootstrap.Modal.getInstance(document.getElementById('createPollModal')).hide();
                form.reset();
                await this.loadPolls();
                this.renderPolls();
            } else {
                const error = await response.json();
                throw new Error(error.detail || 'Error al crear encuesta');
            }
        } catch (error) {
            console.error('Error:', error);
            this.showError('Error al crear encuesta');
        }
    }

    formatDate(dateString) {
        if (!dateString) return 'No especificada';
        const date = new Date(dateString);
        return date.toLocaleDateString('es-CL', {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
    }

    showSuccess(message) {
        const alertDiv = document.createElement('div');
        alertDiv.className = 'alert alert-success alert-dismissible fade show';
        alertDiv.innerHTML = `${message}<button type="button" class="btn-close" data-bs-dismiss="alert"></button>`;
        const container = document.querySelector('.container');
        container.insertBefore(alertDiv, container.firstChild);
        setTimeout(() => {
            if (alertDiv.parentNode) {
                alertDiv.remove();
            }
        }, 3000);
    }

    showError(message) {
        const alertDiv = document.createElement('div');
        alertDiv.className = 'alert alert-danger alert-dismissible fade show';
        alertDiv.innerHTML = `${message}<button type="button" class="btn-close" data-bs-dismiss="alert"></button>`;
        const container = document.querySelector('.container');
        container.insertBefore(alertDiv, container.firstChild);
        setTimeout(() => {
            if (alertDiv.parentNode) {
                alertDiv.remove();
            }
        }, 5000);
    }
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(() => {
        if (window.playSound) {
            window.playSound('pageLoad');
        }
    }, 500);

    // Inicializar el gestor de encuestas
    window.pollsManager = new PollsManager();
});