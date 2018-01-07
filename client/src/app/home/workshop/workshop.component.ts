import { Component, OnInit } from "@angular/core";
import { Router, ActivatedRoute, ParamMap } from "@angular/router";
import { MainService } from "../services/main.service";

@Component({
  selector: "app-workshop",
  templateUrl: "./workshop.component.html",
  styleUrls: ["./workshop.component.css"]
})

export class WorkshopComponent implements OnInit {

  workshop_name
  workshop
  faqs_background='/assets/faqs.jpg'
  constructor(private route: ActivatedRoute, private router: Router, private __mainService: MainService) {
    this.workshop_name = this.route.snapshot.paramMap.get('name');
  }

  ngOnInit() {
    this.__mainService.getWorkshop(this.workshop_name).subscribe(
      (workshop) => {
        this.workshop = workshop
        console.log(workshop)
      },
      (error) => {
        console.log(error)
      })
  }
}
