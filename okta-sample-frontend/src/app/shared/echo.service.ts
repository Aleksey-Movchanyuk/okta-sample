import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';

import { environment } from '@app/../environments/environment';


const apiUrl = environment.apiUrl;
const ECHO = 'echo/';

@Injectable({
  providedIn: 'root'
})
export class EchoService {

  constructor(
    private http: HttpClient,
  ) { }

  echo() {
    return this.http.get(`${apiUrl}` + ECHO, {});
  }
}
