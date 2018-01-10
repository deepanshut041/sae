import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from '@angular/common/http';
/**
 * @description
 * @class
 */
@Injectable()
export class CoreService {
  domain = "http://localhost:8000"
  authToken:any;
  email:any;
  username:any;
  constructor(private http:HttpClient) {    
  }
  logout(){
    this.authToken = null;
    this.username = null;
    this.email = null;
    localStorage.clear();
  }

  loadToken(){
    const token = localStorage.getItem('id_token');
    this.authToken = token
  }
  verifyUser(){
    this.loadToken()
    const headers = new HttpHeaders(
      {
        'Content-Type':'application/json; charset=utf-8'
      });
    const token = {
      "token":this.authToken
    }
    return this.http.post(this.domain+'/api/v1/auth/verify/',token, {headers: headers});
  }

}
