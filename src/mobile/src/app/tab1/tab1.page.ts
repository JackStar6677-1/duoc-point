import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss'],
  standalone: false,
})
export class Tab1Page {

  constructor(private router: Router) {}

  goToForums() {
    this.router.navigate(['/tabs/tab2']);
  }

  goToMarket() {
    this.router.navigate(['/tabs/tab3']);
  }

  goToPortfolio() {
    // TODO: Implementar página de portafolio
    console.log('Ir a portafolio');
  }

  goToCampus() {
    // TODO: Implementar página de campus
    console.log('Ir a campus');
  }

  goToPolls() {
    // TODO: Implementar página de encuestas
    console.log('Ir a encuestas');
  }

  goToNotifications() {
    // TODO: Implementar página de notificaciones
    console.log('Ir a notificaciones');
  }
}
