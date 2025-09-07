import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = environment.apiUrl;
  private backendUrl = environment.backendUrl;

  constructor(private http: HttpClient) { }

  private getHeaders(): HttpHeaders {
    const token = localStorage.getItem('token');
    return new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': token ? `Bearer ${token}` : ''
    });
  }

  // Autenticación
  login(email: string, password: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/auth/login/`, { email, password });
  }

  register(userData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/auth/register/`, userData);
  }

  getProfile(): Observable<any> {
    return this.http.get(`${this.apiUrl}/accounts/me/`, { headers: this.getHeaders() });
  }

  // Foros
  getForums(): Observable<any> {
    return this.http.get(`${this.apiUrl}/forum/foros/`, { headers: this.getHeaders() });
  }

  getPosts(): Observable<any> {
    return this.http.get(`${this.apiUrl}/forum/posts/`, { headers: this.getHeaders() });
  }

  createPost(postData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/forum/posts/`, postData, { headers: this.getHeaders() });
  }

  // Mercado
  getProducts(): Observable<any> {
    return this.http.get(`${this.apiUrl}/market/productos/`, { headers: this.getHeaders() });
  }

  createProduct(productData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/market/productos/`, productData, { headers: this.getHeaders() });
  }

  // Portafolio
  getPortfolio(): Observable<any> {
    return this.http.get(`${this.apiUrl}/portfolio/portafolio-completo/`, { headers: this.getHeaders() });
  }

  generatePDF(): Observable<any> {
    return this.http.post(`${this.apiUrl}/portfolio/generar-pdf/`, {}, { headers: this.getHeaders() });
  }

  // Encuestas
  getPolls(): Observable<any> {
    return this.http.get(`${this.apiUrl}/polls/encuestas/`, { headers: this.getHeaders() });
  }

  votePoll(pollId: number, optionId: number): Observable<any> {
    return this.http.post(`${this.apiUrl}/polls/encuestas/${pollId}/votar/`, { opcion: optionId }, { headers: this.getHeaders() });
  }

  // Campus
  getCampusInfo(): Observable<any> {
    return this.http.get(`${this.apiUrl}/campuses/sedes/`, { headers: this.getHeaders() });
  }
}
