import { Component, OnInit } from "@angular/core";
import { Router, ActivatedRoute, ParamMap } from "@angular/router";
import { MainService } from "../services/main.service";


@Component({
  selector: "app-event",
  templateUrl: "./event.component.html",
  styleUrls: ["./event.component.css"]
})

export class EventComponent implements OnInit {
  event_id
  constructor(private route:ActivatedRoute, private router: Router, private __mainService:MainService) { 
    this.event_id = this.route.snapshot.paramMap.get('id');
  }

  ngOnInit() {
    this.__mainService.getEvent(this.event_id).subscribe(
      (event) => {
        console.log(event)
      },
      (error) => {
        console.log(error)
      })
  }
}
