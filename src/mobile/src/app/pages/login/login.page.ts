import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastController, LoadingController } from '@ionic/angular';
import { ApiService } from '../../services/api';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
  standalone: false,
})
export class LoginPage implements OnInit {
  loginData = {
    email: '',
    password: ''
  };
  loading = false;

  constructor(
    private apiService: ApiService,
    private router: Router,
    private toastController: ToastController,
    private loadingController: LoadingController
  ) { }

  ngOnInit() {
    // Verificar si ya está logueado
    const token = localStorage.getItem('token');
    if (token) {
      this.router.navigate(['/tabs']);
    }
  }

  async onLogin() {
    if (!this.loginData.email || !this.loginData.password) {
      this.showToast('Por favor completa todos los campos', 'danger');
      return;
    }

    this.loading = true;
    
    try {
      const response = await this.apiService.login(this.loginData.email, this.loginData.password).toPromise();
      
      if (response.access) {
        localStorage.setItem('token', response.access);
        localStorage.setItem('refresh', response.refresh);
        localStorage.setItem('user', JSON.stringify(response.user));
        
        this.showToast('¡Bienvenido a DuocPoint!', 'success');
        this.router.navigate(['/tabs']);
      }
    } catch (error) {
      console.error('Error en login:', error);
      this.showToast('Error al iniciar sesión. Verifica tus credenciales.', 'danger');
    } finally {
      this.loading = false;
    }
  }

  goToRegister() {
    this.router.navigate(['/register']);
  }

  async showToast(message: string, color: string) {
    const toast = await this.toastController.create({
      message: message,
      duration: 3000,
      color: color,
      position: 'bottom'
    });
    toast.present();
  }
}
