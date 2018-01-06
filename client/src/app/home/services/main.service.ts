import { Injectable } from "@angular/core";
import { HttpClient } from '@angular/common/http';
/**
 * @description
 * @class
 */
@Injectable()
export class MainService {

  constructor(private httpClient:HttpClient) {
    
  }
  getEvents(){
    return this.httpClient.get('http://localhost:8000/api/v1/events/')
  }
  getWorkshops(){
    return this.httpClient.get('http://localhost:8000/api/v1/workshops/')
  }

}
