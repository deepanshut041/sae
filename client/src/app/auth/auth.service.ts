import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from '@angular/common/http';

/**
 * @description
 * @class
 */
@Injectable()
export class AuthService {
  domain = "http://localhost:8000"
  authToken:any;
  email:any;
  username:any;
  constructor(private http:HttpClient) {
    
  }

  registerUser(user){
    const headers = new HttpHeaders({'Content-Type':'application/json; charset=utf-8'});
    return this.http.post(this.domain+'/api/v1/auth/register/',user, {headers: headers});
  }
  loginUser(user){
    const headers = new HttpHeaders({'Content-Type':'application/json; charset=utf-8'});
    return this.http.post(this.domain+'/api/v1/auth/login/',user, {headers: headers});
  }

  getUsers(){
    const headers = new HttpHeaders(
      {
        'Content-Type':'application/json; charset=utf-8',
        'Authorization':'JWT ' + this.authToken
      });
    return this.http.get(this.domain+'/api/v1/auth/login/', {headers: headers});
  }

  storeUserData(token,username,email){
    localStorage.setItem('id_token',token)
    localStorage.setItem('username',username)
    localStorage.setItem('email',email)
    this.authToken = token;
    this.email = email;
    this.username = username;
  }
  
  logout(){
    this.authToken = null;
    this.user = null;
    localStorage.clear();
  }

  loadToken(){
    const token = localStorage.getItem('id_token');
    this.authToken = token
  }

}
