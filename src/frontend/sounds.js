// DuocPoint - Sistema de Sonidos para Animaciones
class DuocPointSounds {
    constructor() {
        this.sounds = {};
        this.enabled = true;
        this.volume = 0.3;
        this.init();
    }

    init() {
        // Crear sonidos usando Web Audio API
        this.createSounds();
        
        // Verificar si el usuario ha permitido audio
        this.checkAudioPermission();
    }

    createSounds() {
        // Crear contexto de audio
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        
        // Función para crear tonos
        const createTone = (frequency, duration, type = 'sine') => {
            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();
            
            oscillator.connect(gainNode);
            gainNode.connect(audioContext.destination);
            
            oscillator.frequency.setValueAtTime(frequency, audioContext.currentTime);
            oscillator.type = type;
            
            gainNode.gain.setValueAtTime(0, audioContext.currentTime);
            gainNode.gain.linearRampToValueAtTime(this.volume, audioContext.currentTime + 0.01);
            gainNode.gain.exponentialRampToValueAtTime(0.001, audioContext.currentTime + duration);
            
            oscillator.start(audioContext.currentTime);
            oscillator.stop(audioContext.currentTime + duration);
        };

        // Sonidos para diferentes acciones
        this.sounds = {
            // Sonido de hover suave
            hover: () => createTone(800, 0.1, 'sine'),
            
            // Sonido de click
            click: () => createTone(1000, 0.15, 'square'),
            
            // Sonido de éxito
            success: () => {
                createTone(523, 0.2, 'sine'); // Do
                setTimeout(() => createTone(659, 0.2, 'sine'), 100); // Mi
                setTimeout(() => createTone(784, 0.3, 'sine'), 200); // Sol
            },
            
            // Sonido de error
            error: () => {
                createTone(200, 0.3, 'sawtooth');
                setTimeout(() => createTone(150, 0.3, 'sawtooth'), 150);
            },
            
            // Sonido de notificación
            notification: () => {
                createTone(880, 0.2, 'sine'); // La
                setTimeout(() => createTone(1108, 0.2, 'sine'), 100); // Re#
                setTimeout(() => createTone(1318, 0.3, 'sine'), 200); // Mi
            },
            
            // Sonido de carga
            loading: () => {
                createTone(440, 0.1, 'sine'); // La
                setTimeout(() => createTone(554, 0.1, 'sine'), 50); // Do#
                setTimeout(() => createTone(659, 0.1, 'sine'), 100); // Mi
            },
            
            // Sonido de transición
            transition: () => {
                createTone(330, 0.2, 'triangle');
                setTimeout(() => createTone(440, 0.2, 'triangle'), 100);
            },
            
            // Sonido de login exitoso
            loginSuccess: () => {
                createTone(523, 0.2, 'sine'); // Do
                setTimeout(() => createTone(659, 0.2, 'sine'), 100); // Mi
                setTimeout(() => createTone(784, 0.2, 'sine'), 200); // Sol
                setTimeout(() => createTone(1047, 0.4, 'sine'), 300); // Do alto
            },
            
            // Sonido de logout
            logout: () => {
                createTone(1047, 0.2, 'sine'); // Do alto
                setTimeout(() => createTone(784, 0.2, 'sine'), 100); // Sol
                setTimeout(() => createTone(659, 0.2, 'sine'), 200); // Mi
                setTimeout(() => createTone(523, 0.3, 'sine'), 300); // Do
            }
        };
    }

    checkAudioPermission() {
        // Intentar reproducir un sonido silencioso para activar el contexto de audio
        try {
            const audioContext = new (window.AudioContext || window.webkitAudioContext)();
            if (audioContext.state === 'suspended') {
                audioContext.resume();
            }
        } catch (error) {
            console.log('Audio no disponible:', error);
            this.enabled = false;
        }
    }

    play(soundName) {
        if (!this.enabled || !this.sounds[soundName]) return;
        
        try {
            this.sounds[soundName]();
        } catch (error) {
            console.log('Error reproduciendo sonido:', error);
        }
    }

    setVolume(volume) {
        this.volume = Math.max(0, Math.min(1, volume));
    }

    toggle() {
        this.enabled = !this.enabled;
        return this.enabled;
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
