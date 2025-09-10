// DuocPoint - Sistema de Sonidos Avanzado para Animaciones
class DuocPointSounds {
    constructor() {
        this.sounds = {};
        this.enabled = true;
        this.volume = 0.4;
        this.audioContext = null;
        this.backgroundMusic = null;
        this.backgroundMusicEnabled = true;
        this.backgroundMusicVolume = 0.3;
        this.backgroundMusicPlaying = false;
        this.init();
    }

    init() {
        // Crear sonidos usando Web Audio API
        this.createSounds();
        
        // Inicializar música de fondo
        this.initBackgroundMusic();
        
        // Verificar si el usuario ha permitido audio
        this.checkAudioPermission();
        
        // Agregar controles de volumen
        this.createVolumeControls();
    }

    createSounds() {
        // Crear contexto de audio
        this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
        
        // Función para crear tonos con efectos
        const createTone = (frequency, duration, type = 'sine', effects = {}) => {
            const oscillator = this.audioContext.createOscillator();
            const gainNode = this.audioContext.createGain();
            const filter = this.audioContext.createBiquadFilter();
            
            // Configurar filtro
            filter.type = effects.filterType || 'lowpass';
            filter.frequency.setValueAtTime(effects.filterFreq || 2000, this.audioContext.currentTime);
            
            // Conectar nodos
            oscillator.connect(filter);
            filter.connect(gainNode);
            gainNode.connect(this.audioContext.destination);
            
            oscillator.frequency.setValueAtTime(frequency, this.audioContext.currentTime);
            oscillator.type = type;
            
            // Configurar volumen con curva suave
            gainNode.gain.setValueAtTime(0, this.audioContext.currentTime);
            gainNode.gain.linearRampToValueAtTime(this.volume * (effects.volume || 1), this.audioContext.currentTime + 0.01);
            gainNode.gain.exponentialRampToValueAtTime(0.001, this.audioContext.currentTime + duration);
            
            // Efectos de modulación
            if (effects.vibrato) {
                const lfo = this.audioContext.createOscillator();
                const lfoGain = this.audioContext.createGain();
                lfo.frequency.setValueAtTime(effects.vibrato.rate || 5, this.audioContext.currentTime);
                lfoGain.gain.setValueAtTime(effects.vibrato.depth || 10, this.audioContext.currentTime);
                lfo.connect(lfoGain);
                lfoGain.connect(oscillator.frequency);
                lfo.start(this.audioContext.currentTime);
                lfo.stop(this.audioContext.currentTime + duration);
            }
            
            oscillator.start(this.audioContext.currentTime);
            oscillator.stop(this.audioContext.currentTime + duration);
        };

        // Función para crear acordes
        const createChord = (frequencies, duration, type = 'sine') => {
            frequencies.forEach((freq, index) => {
                setTimeout(() => createTone(freq, duration, type), index * 50);
            });
        };

        // Función para crear melodías
        const createMelody = (notes, durations, type = 'sine') => {
            let currentTime = 0;
            notes.forEach((note, index) => {
                setTimeout(() => {
                    createTone(note, durations[index] || 0.2, type);
                }, currentTime * 1000);
                currentTime += durations[index] || 0.2;
            });
        };

        // Sonidos para diferentes acciones
        this.sounds = {
            // Sonido de hover suave con vibrato
            hover: () => createTone(800, 0.1, 'sine', { vibrato: { rate: 8, depth: 5 } }),
            
            // Sonido de click con filtro
            click: () => createTone(1000, 0.15, 'square', { filterType: 'highpass', filterFreq: 500 }),
            
            // Sonido de éxito con acorde mayor
            success: () => createChord([523, 659, 784], 0.4, 'sine'), // Do-Mi-Sol
            
            // Sonido de error con acorde menor
            error: () => createChord([200, 237, 297], 0.5, 'sawtooth'), // Acorde menor
            
            // Sonido de notificación melódico
            notification: () => createMelody([880, 1108, 1318, 1568], [0.2, 0.2, 0.2, 0.4], 'sine'),
            
            // Sonido de carga progresivo
            loading: () => {
                const notes = [440, 554, 659, 784];
                notes.forEach((note, index) => {
                    setTimeout(() => createTone(note, 0.1, 'sine'), index * 50);
                });
            },
            
            // Sonido de transición suave
            transition: () => createMelody([330, 440, 554, 659], [0.2, 0.2, 0.2, 0.3], 'triangle'),
            
            // Sonido de login exitoso con fanfarria
            loginSuccess: () => {
                const fanfare = [523, 659, 784, 1047, 1318, 1047, 784, 1047];
                const durations = [0.2, 0.2, 0.2, 0.3, 0.4, 0.2, 0.2, 0.5];
                createMelody(fanfare, durations, 'sine');
            },
            
            // Sonido de logout descendente
            logout: () => {
                const logout = [1047, 784, 659, 523, 392];
                const durations = [0.2, 0.2, 0.2, 0.3, 0.4];
                createMelody(logout, durations, 'sine');
            },
            
            // Nuevos sonidos específicos para DuocPoint
            
            // Sonido de navegación
            navigate: () => createTone(660, 0.15, 'sine', { filterType: 'bandpass', filterFreq: 1000 }),
            
            // Sonido de formulario completado
            formComplete: () => createChord([523, 659, 784, 1047], 0.3, 'sine'),
            
            // Sonido de mensaje enviado
            messageSent: () => createMelody([784, 1047, 1318], [0.15, 0.15, 0.3], 'sine'),
            
            // Sonido de archivo subido
            fileUpload: () => createTone(440, 0.2, 'sine', { vibrato: { rate: 10, depth: 20 } }),
            
            // Sonido de búsqueda
            search: () => createMelody([880, 1108, 1318], [0.1, 0.1, 0.2], 'sine'),
            
            // Sonido de like/favorito
            like: () => createTone(1047, 0.2, 'sine', { vibrato: { rate: 15, depth: 30 } }),
            
            // Sonido de comentario
            comment: () => createMelody([659, 784, 880], [0.1, 0.1, 0.2], 'sine'),
            
            // Sonido de notificación push
            pushNotification: () => {
                createTone(880, 0.1, 'sine');
                setTimeout(() => createTone(1108, 0.1, 'sine'), 100);
                setTimeout(() => createTone(1318, 0.2, 'sine'), 200);
            },
            
            // Sonido de error de validación
            validationError: () => createTone(200, 0.3, 'sawtooth', { filterType: 'lowpass', filterFreq: 300 }),
            
            // Sonido de éxito de validación
            validationSuccess: () => createTone(800, 0.2, 'sine', { vibrato: { rate: 12, depth: 15 } }),
            
            // Sonido de carga de página
            pageLoad: () => createMelody([440, 554, 659, 784], [0.15, 0.15, 0.15, 0.3], 'sine'),
            
            // Sonido de cierre de modal
            modalClose: () => createMelody([784, 659, 523], [0.1, 0.1, 0.2], 'triangle'),
            
            // Sonido de scroll
            scroll: () => createTone(440, 0.05, 'sine', { volume: 0.3 }),
            
            // Sonido de drag and drop
            dragDrop: () => createTone(660, 0.2, 'sine', { filterType: 'highpass', filterFreq: 800 }),
            
            // Sonido de copia al portapapeles
            copy: () => createTone(1047, 0.1, 'sine', { vibrato: { rate: 20, depth: 10 } }),
            
            // Sonido de zoom
            zoom: () => createMelody([440, 554, 659], [0.1, 0.1, 0.2], 'sine'),
            
            // Sonido de menú desplegable
            dropdown: () => createTone(880, 0.15, 'sine', { filterType: 'bandpass', filterFreq: 1200 }),
            
            // Sonido de toggle switch
            toggle: () => createMelody([440, 880], [0.1, 0.1], 'square'),
            
            // Sonido de slider
            slider: () => createTone(440, 0.1, 'sine', { volume: 0.2, vibrato: { rate: 8, depth: 5 } }),
            
            // Sonido de calendario
            calendar: () => createMelody([523, 659, 784, 1047], [0.1, 0.1, 0.1, 0.2], 'sine'),
            
            // Sonido de mapa
            map: () => createTone(330, 0.2, 'triangle', { filterType: 'lowpass', filterFreq: 1000 }),
            
            // Sonido de chat
            chat: () => createMelody([659, 784, 880, 1047], [0.1, 0.1, 0.1, 0.2], 'sine'),
            
            // Sonido de video
            video: () => createTone(880, 0.2, 'sine', { vibrato: { rate: 6, depth: 20 } }),
            
            // Sonido de audio
            audio: () => createTone(440, 0.2, 'sine', { vibrato: { rate: 8, depth: 15 } }),
            
            // Sonido de imagen
            image: () => createTone(1047, 0.15, 'sine', { filterType: 'highpass', filterFreq: 600 }),
            
            // Sonido de documento
            document: () => createMelody([523, 659, 784], [0.1, 0.1, 0.2], 'sine'),
            
            // Sonido de configuración
            settings: () => createMelody([440, 554, 659, 784, 880], [0.1, 0.1, 0.1, 0.1, 0.2], 'sine'),
            
            // Sonido de perfil
            profile: () => createChord([523, 659, 784], 0.3, 'sine'),
            
            // Sonido de estadísticas
            stats: () => createMelody([440, 554, 659, 784, 880, 1047], [0.1, 0.1, 0.1, 0.1, 0.1, 0.3], 'sine'),
            
            // Sonido de reporte
            report: () => createTone(660, 0.2, 'sine', { filterType: 'bandpass', filterFreq: 800 }),
            
            // Sonido de backup
            backup: () => createMelody([523, 659, 784, 1047, 1318], [0.15, 0.15, 0.15, 0.15, 0.4], 'sine'),
            
            // Sonido de sincronización
            sync: () => {
                const sync = [440, 554, 659, 784, 880, 1047, 1175, 1318];
                sync.forEach((note, index) => {
                    setTimeout(() => createTone(note, 0.1, 'sine'), index * 50);
                });
            }
        };
    }

    initBackgroundMusic() {
        // Crear elemento de audio para la música de fondo
        this.backgroundMusic = new Audio('/static/audio/background.mp3');
        this.backgroundMusic.loop = true;
        this.backgroundMusic.volume = this.backgroundMusicVolume;
        this.backgroundMusic.preload = 'auto';
        
        // Manejar eventos de la música de fondo
        this.backgroundMusic.addEventListener('loadstart', () => {
            console.log('DuocPoint: Cargando música de fondo...');
        });
        
        this.backgroundMusic.addEventListener('canplaythrough', () => {
            console.log('DuocPoint: Música de fondo lista para reproducir');
            // Auto-reproducir si está habilitado
            if (this.backgroundMusicEnabled) {
                this.playBackgroundMusic();
            }
        });
        
        this.backgroundMusic.addEventListener('error', (e) => {
            console.warn('DuocPoint: Error cargando música de fondo:', e);
            this.backgroundMusicEnabled = false;
        });
        
        this.backgroundMusic.addEventListener('ended', () => {
            // Reiniciar automáticamente si está en loop
            if (this.backgroundMusicEnabled && this.backgroundMusicPlaying) {
                this.backgroundMusic.currentTime = 0;
                this.backgroundMusic.play().catch(e => {
                    console.log('DuocPoint: Error reiniciando música de fondo:', e);
                });
            }
        });
    }

    playBackgroundMusic() {
        if (!this.backgroundMusic || !this.backgroundMusicEnabled) return;
        
        this.backgroundMusic.play().then(() => {
            this.backgroundMusicPlaying = true;
            console.log('DuocPoint: Música de fondo iniciada');
            this.updateBackgroundMusicControls();
        }).catch(e => {
            console.log('DuocPoint: No se pudo reproducir música de fondo:', e);
            this.backgroundMusicEnabled = false;
            this.updateBackgroundMusicControls();
        });
    }

    pauseBackgroundMusic() {
        if (!this.backgroundMusic) return;
        
        this.backgroundMusic.pause();
        this.backgroundMusicPlaying = false;
        console.log('DuocPoint: Música de fondo pausada');
        this.updateBackgroundMusicControls();
    }

    stopBackgroundMusic() {
        if (!this.backgroundMusic) return;
        
        this.backgroundMusic.pause();
        this.backgroundMusic.currentTime = 0;
        this.backgroundMusicPlaying = false;
        console.log('DuocPoint: Música de fondo detenida');
        this.updateBackgroundMusicControls();
    }

    toggleBackgroundMusic() {
        if (this.backgroundMusicPlaying) {
            this.pauseBackgroundMusic();
        } else {
            this.playBackgroundMusic();
        }
    }

    setBackgroundMusicVolume(volume) {
        this.backgroundMusicVolume = Math.max(0, Math.min(1, volume));
        if (this.backgroundMusic) {
            this.backgroundMusic.volume = this.backgroundMusicVolume;
        }
        this.updateBackgroundMusicControls();
    }

    setBackgroundMusicEnabled(enabled) {
        this.backgroundMusicEnabled = enabled;
        if (!enabled) {
            this.pauseBackgroundMusic();
        } else if (enabled && !this.backgroundMusicPlaying) {
            this.playBackgroundMusic();
        }
        this.updateBackgroundMusicControls();
    }

    checkAudioPermission() {
        // Intentar reproducir un sonido silencioso para activar el contexto de audio
        try {
            if (this.audioContext && this.audioContext.state === 'suspended') {
                this.audioContext.resume();
            }
        } catch (error) {
            console.log('Audio no disponible:', error);
            this.enabled = false;
        }
    }

    createVolumeControls() {
        // Crear controles de volumen en el DOM
        const volumeControls = document.createElement('div');
        volumeControls.id = 'volume-controls';
        volumeControls.style.cssText = `
            position: fixed;
            top: 20px;
            right: 80px;
            z-index: 10000;
            background: rgba(0, 0, 0, 0.8);
            padding: 10px;
            border-radius: 8px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            color: white;
            font-size: 12px;
            min-width: 200px;
        `;
        
        // Controles de efectos de sonido
        const effectsSection = document.createElement('div');
        effectsSection.style.cssText = 'display: flex; align-items: center; gap: 10px;';
        
        const effectsLabel = document.createElement('span');
        effectsLabel.textContent = 'Efectos:';
        effectsLabel.style.fontWeight = 'bold';
        
        const volumeSlider = document.createElement('input');
        volumeSlider.type = 'range';
        volumeSlider.min = '0';
        volumeSlider.max = '1';
        volumeSlider.step = '0.1';
        volumeSlider.value = this.volume;
        volumeSlider.style.width = '80px';
        
        const muteButton = document.createElement('button');
        muteButton.innerHTML = this.enabled ? '🔊' : '🔇';
        muteButton.style.cssText = `
            background: none;
            border: none;
            color: white;
            cursor: pointer;
            font-size: 16px;
        `;
        
        // Controles de música de fondo
        const musicSection = document.createElement('div');
        musicSection.style.cssText = 'display: flex; align-items: center; gap: 10px;';
        
        const musicLabel = document.createElement('span');
        musicLabel.textContent = 'Música:';
        musicLabel.style.fontWeight = 'bold';
        
        const musicToggleButton = document.createElement('button');
        musicToggleButton.id = 'music-toggle';
        musicToggleButton.innerHTML = this.backgroundMusicEnabled ? '🎵' : '🎶';
        musicToggleButton.style.cssText = `
            background: none;
            border: none;
            color: white;
            cursor: pointer;
            font-size: 16px;
        `;
        
        const musicVolumeSlider = document.createElement('input');
        musicVolumeSlider.type = 'range';
        musicVolumeSlider.min = '0';
        musicVolumeSlider.max = '1';
        musicVolumeSlider.step = '0.1';
        musicVolumeSlider.value = this.backgroundMusicVolume;
        musicVolumeSlider.style.width = '80px';
        musicVolumeSlider.disabled = !this.backgroundMusicEnabled;
        
        // Event listeners para efectos de sonido
        volumeSlider.addEventListener('input', (e) => {
            this.setVolume(parseFloat(e.target.value));
        });
        
        muteButton.addEventListener('click', () => {
            this.toggle();
            muteButton.innerHTML = this.enabled ? '🔊' : '🔇';
        });
        
        // Event listeners para música de fondo
        musicToggleButton.addEventListener('click', () => {
            this.setBackgroundMusicEnabled(!this.backgroundMusicEnabled);
        });
        
        musicVolumeSlider.addEventListener('input', (e) => {
            this.setBackgroundMusicVolume(parseFloat(e.target.value));
        });
        
        // Construir la interfaz
        effectsSection.appendChild(effectsLabel);
        effectsSection.appendChild(muteButton);
        effectsSection.appendChild(volumeSlider);
        
        musicSection.appendChild(musicLabel);
        musicSection.appendChild(musicToggleButton);
        musicSection.appendChild(musicVolumeSlider);
        
        volumeControls.appendChild(effectsSection);
        volumeControls.appendChild(musicSection);
        document.body.appendChild(volumeControls);
        
        // Guardar referencias para actualizaciones
        this.volumeControls = {
            container: volumeControls,
            muteButton: muteButton,
            volumeSlider: volumeSlider,
            musicToggleButton: musicToggleButton,
            musicVolumeSlider: musicVolumeSlider
        };
        
        // Auto-hide después de 5 segundos
        setTimeout(() => {
            if (volumeControls && volumeControls.parentNode) {
                volumeControls.style.opacity = '0.3';
                volumeControls.style.transition = 'opacity 0.5s ease';
            }
        }, 5000);
        
        // Mostrar al hacer hover
        volumeControls.addEventListener('mouseenter', () => {
            volumeControls.style.opacity = '1';
        });
        
        volumeControls.addEventListener('mouseleave', () => {
            volumeControls.style.opacity = '0.3';
        });
    }

    play(soundName) {
        if (!this.enabled || !this.sounds[soundName]) return;
        
        try {
            // Verificar si el contexto de audio está suspendido
            if (this.audioContext && this.audioContext.state === 'suspended') {
                this.audioContext.resume();
            }
            
            this.sounds[soundName]();
        } catch (error) {
            console.log('Error reproduciendo sonido:', error);
        }
    }

    setVolume(volume) {
        this.volume = Math.max(0, Math.min(1, volume));
        // Actualizar el slider si existe
        if (this.volumeControls && this.volumeControls.volumeSlider) {
            this.volumeControls.volumeSlider.value = this.volume;
        }
    }

    updateBackgroundMusicControls() {
        if (!this.volumeControls) return;
        
        // Actualizar botón de música
        this.volumeControls.musicToggleButton.innerHTML = this.backgroundMusicEnabled ? '🎵' : '🎶';
        
        // Actualizar slider de volumen de música
        this.volumeControls.musicVolumeSlider.value = this.backgroundMusicVolume;
        this.volumeControls.musicVolumeSlider.disabled = !this.backgroundMusicEnabled;
        
        // Actualizar botón de efectos de sonido
        this.volumeControls.muteButton.innerHTML = this.enabled ? '🔊' : '🔇';
        
        // Actualizar slider de efectos de sonido
        this.volumeControls.volumeSlider.value = this.volume;
        
        // Actualizar botón del header si existe
        this.updateHeaderMusicButton();
    }

    updateHeaderMusicButton() {
        const musicButton = document.getElementById('background-music-toggle');
        if (musicButton) {
            if (this.backgroundMusicEnabled && this.backgroundMusicPlaying) {
                musicButton.innerHTML = '<i class="fas fa-pause"></i>';
                musicButton.title = 'Pausar música de fondo';
            } else if (this.backgroundMusicEnabled && !this.backgroundMusicPlaying) {
                musicButton.innerHTML = '<i class="fas fa-play"></i>';
                musicButton.title = 'Reproducir música de fondo';
            } else {
                musicButton.innerHTML = '<i class="fas fa-music"></i>';
                musicButton.title = 'Activar música de fondo';
            }
        }
    }

    toggle() {
        this.enabled = !this.enabled;
        return this.enabled;
    }

    // Método para reproducir sonidos con delay
    playDelayed(soundName, delay = 0) {
        setTimeout(() => this.play(soundName), delay);
    }

    // Método para reproducir múltiples sonidos en secuencia
    playSequence(soundNames, delays = []) {
        soundNames.forEach((soundName, index) => {
            const delay = delays[index] || index * 200;
            this.playDelayed(soundName, delay);
        });
    }

    // Método para crear efectos de sonido personalizados
    createCustomSound(frequency, duration, type = 'sine', effects = {}) {
        if (!this.enabled || !this.audioContext) return;
        
        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();
        const filter = this.audioContext.createBiquadFilter();
        
        filter.type = effects.filterType || 'lowpass';
        filter.frequency.setValueAtTime(effects.filterFreq || 2000, this.audioContext.currentTime);
        
        oscillator.connect(filter);
        filter.connect(gainNode);
        gainNode.connect(this.audioContext.destination);
        
        oscillator.frequency.setValueAtTime(frequency, this.audioContext.currentTime);
        oscillator.type = type;
        
        gainNode.gain.setValueAtTime(0, this.audioContext.currentTime);
        gainNode.gain.linearRampToValueAtTime(this.volume * (effects.volume || 1), this.audioContext.currentTime + 0.01);
        gainNode.gain.exponentialRampToValueAtTime(0.001, this.audioContext.currentTime + duration);
        
        oscillator.start(this.audioContext.currentTime);
        oscillator.stop(this.audioContext.currentTime + duration);
    }
}

// Inicializar sistema de sonidos
window.duocPointSounds = new DuocPointSounds();

// Función global para reproducir sonidos
window.playSound = (soundName) => {
    if (window.duocPointSounds) {
        window.duocPointSounds.play(soundName);
    }
};

// Función global para reproducir sonidos con delay
window.playSoundDelayed = (soundName, delay = 0) => {
    if (window.duocPointSounds) {
        window.duocPointSounds.playDelayed(soundName, delay);
    }
};

// Función global para reproducir secuencias de sonidos
window.playSoundSequence = (soundNames, delays = []) => {
    if (window.duocPointSounds) {
        window.duocPointSounds.playSequence(soundNames, delays);
    }
};

// Función global para crear sonidos personalizados
window.createCustomSound = (frequency, duration, type = 'sine', effects = {}) => {
    if (window.duocPointSounds) {
        window.duocPointSounds.createCustomSound(frequency, duration, type, effects);
    }
};

// Funciones globales para controlar la música de fondo
window.playBackgroundMusic = () => {
    if (window.duocPointSounds) {
        window.duocPointSounds.playBackgroundMusic();
    }
};

window.pauseBackgroundMusic = () => {
    if (window.duocPointSounds) {
        window.duocPointSounds.pauseBackgroundMusic();
    }
};

window.stopBackgroundMusic = () => {
    if (window.duocPointSounds) {
        window.duocPointSounds.stopBackgroundMusic();
    }
};

window.toggleBackgroundMusic = () => {
    if (window.duocPointSounds) {
        window.duocPointSounds.toggleBackgroundMusic();
    }
};

window.setBackgroundMusicVolume = (volume) => {
    if (window.duocPointSounds) {
        window.duocPointSounds.setBackgroundMusicVolume(volume);
    }
};

window.setBackgroundMusicEnabled = (enabled) => {
    if (window.duocPointSounds) {
        window.duocPointSounds.setBackgroundMusicEnabled(enabled);
    }
};
