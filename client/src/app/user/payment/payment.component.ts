import { Component, OnInit } from "@angular/core";
import { IMAGE_AUTH } from "../../shared/assets";
@Component({
  selector: "app-payment",
  templateUrl: "./payment.component.html",
  styleUrls: ["./payment.component.css"]
})

export class PaymentComponent implements OnInit {
  err_404 = IMAGE_AUTH
  constructor() { 

  }

  ngOnInit() {

  }
}
