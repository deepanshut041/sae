import { Component, OnInit } from "@angular/core";
import { AuthService } from "../auth.service";
import { ActivatedRoute, Router } from "@angular/router";

@Component({
  selector: "app-reset-admin",
  templateUrl: "./reset.component.html",
  styleUrls: ["./reset.component.css"]
})

export class ResetComponent implements OnInit {
  alertMsg:String="";
  token:String;
  uid:String;
  constructor(private _authService:AuthService, private route:ActivatedRoute, private router:Router) { 
    route.params.subscribe((params)=>{
      this.token = params['t']
      this.uid = params['u']
      if(!this.uid || !this.token){
        this.router.navigate([''])
      }
      console.log(this.token, this.uid)
    })
  }
  ngOnInit() {
  }
  verifyAlert() {
    this.hideVerifyBody();
    var elemIcon = document.getElementById("verifyEmailAlertIcon");
    elemIcon.className = "verify-alert-icon";
    var elemMsg = document.getElementById("verifyEmailAlertMsg");
    elemMsg.className = "verify-alert-message";
    var elem2 = document.getElementById("verifyEmailAlert");
    elem2.className = "text-center display";
    setTimeout(() => {
      this.showVerifyBody();
      elem2.className = "text-center hide";
    }, 2000);
  }

  errorAlert() {
    this.hideVerifyBody();
    var elemIcon = document.getElementById("verifyEmailAlertIcon");
    elemIcon.className = "verify-alert-error-icon";
    var elemMsg = document.getElementById("verifyEmailAlertMsg");
    elemMsg.className = "verify-alert-error-message";
    var elem2 = document.getElementById("verifyEmailAlert");
    elem2.className = "text-center display";
    setTimeout(() => {
      this.showVerifyBody();
      elem2.className = "text-center hide";
    }, 2000);
  }

  showSpinner() {
    let elem = document.getElementById("spinner")
    elem.className = "text-center spinner";
  }

  hideSpinner() {
    let elem = document.getElementById("spinner")
    elem.className = "text-center spinner hide";
  }

  showVerifyBody() {
    var elem1 = document.getElementById("resetPasswordBody");
    elem1.className = "panel-body text-center display";
  }

  hideVerifyBody() {
    var elem1 = document.getElementById("resetPasswordBody");
    elem1.className = "panel-body text-center hide";
  }

  // submitForm(Oldassword,newPassword,confirmPassword) {
  //   if (newPassword === confirmPassword) {
  //     this.hideVerifyBody();
  //     this.showSpinner();
      
  //       this._authService.getUser().updatePassword(newPassword).then(()=>{
  //         this.alertMsg = "Changed your Password";
  //         this.hideSpinner();
  //         this.verifyAlert();
  //       }).catch((err)=>{
  //         this.alertMsg = err.message;
  //         this.hideSpinner();
  //         this.errorAlert();
  //       })
  //   }
  //   else{

  //   }
  // }
}
