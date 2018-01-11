import { Injectable } from "@angular/core";
import { HttpClient } from '@angular/common/http';
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

}
