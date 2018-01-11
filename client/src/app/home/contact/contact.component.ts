import { Component, OnInit } from "@angular/core";
import { IMAGE_CONTACT } from "../../shared/assets";
@Component({
  selector: "app-contact",
  templateUrl: "./contact.component.html",
  styleUrls: ["./contact.component.css"]
})

export class ContactComponent implements OnInit {

  contact_img = IMAGE_CONTACT
  
  constructor() { 

  }

  ngOnInit() {

  }
}
