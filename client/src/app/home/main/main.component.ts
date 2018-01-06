import { Component, OnInit } from "@angular/core";
import { MainService } from "../services/main.service";


@Component({
  selector: "app-main",
  templateUrl: "./main.component.html",
  styleUrls: ["./main.component.css"]
})

export class MainComponent implements OnInit {
  header_img = "/assets/header.svg"
  about_img = "/assets/about.svg"
  news_img = "/assets/latest_news.svg"
  events
  workshops
  constructor(private __mainService:MainService) { 

  }

  ngOnInit() {
    this.__mainService.getEvents().subscribe((events)=>{
      console.log(events['events']);
      this.events = events['events'];
    })
    this.__mainService.getWorkshops().subscribe((workshops)=>{
      console.log(workshops['workshops']);
      this.workshops = workshops['workshops']
    })
  }
}
