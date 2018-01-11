import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable,Observer } from "rxjs/Rx"
import { DOMAIN } from "../../shared/assets";
/**
 * @description
 * @class
 */
@Injectable()
export class MainService {
  domain = DOMAIN
  constructor(private httpClient:HttpClient) {
    
  }
  getEvents(){
    return this.httpClient.get(this.domain + '/api/v1/events/')
  }
  getWorkshops(){
    return this.httpClient.get(this.domain + '/api/v1/workshops/')
  }
  getMembers(){
    return this.httpClient.get(this.domain + '/api/v1/members/')
  }
  getEvent(id:number){
    return this.httpClient.get(this.domain + '/api/v1/events/detail/' + id + '/')
  }
  getWorkshop(name:string){
    return this.httpClient.get(this.domain + '/api/v1/workshops/detail/' + name + '/')
  }

  contactUs(contact){
    const headers = new HttpHeaders({'Content-Type':'application/json; charset=utf-8'});
    return this.httpClient.post(this.domain+'/api/v1/contact/',contact, {headers: headers});
  }

}
