import { Component, OnInit, AfterViewInit } from "@angular/core";
import { AuthService } from "../auth.service";
import { validateConfig } from "@angular/router/src/config";
import { Router } from "@angular/router";

@Component({
  selector: "app-verify-admin",
  templateUrl: "./verify.component.html",
  styleUrls: ["./verify.component.css"]
})

export class VerifyComponent implements OnInit, AfterViewInit {
  alertMsg;
  email = "";
  constructor(private _authService: AuthService, private router: Router) {
    // this.email = _authService.getUser().email;
  }
  ngOnInit() {

  }

  ngAfterViewInit() {
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

  showForm() {
    let elem1 = document.getElementById("resendVerificationButton");
    elem1.className = "verify-button-box hide";
    let elem2 = document.getElementById("verifyResetEmailButton");
    elem2.className = "verify-button-box hide";
    let elem3 = document.getElementById("verifyResetEmail");
    elem3.className = "input-group verify-button-box show";
  }

  hideForm() {
    let elem1 = document.getElementById("resendVerificationButton");
    elem1.className = "verify-button-box display";
    let elem2 = document.getElementById("verifyResetEmailButton");
    elem2.className = "verify-button-box display";
    let elem3 = document.getElementById("verifyResetEmail");
    elem3.className = "input-group verify-button-box hide";
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
    var elem1 = document.getElementById("verifyEmailBody");
    elem1.className = "panel-body text-center display";
  }

  hideVerifyBody() {
    var elem1 = document.getElementById("verifyEmailBody");
    elem1.className = "panel-body text-center hide";
  }

  sendForm(email: string) {
    if (email) {
      this.hideVerifyBody();
      this.showSpinner();
      console.log(email);
      // this._authService.getUser().updateEmail(email).then(() => {
      //   this._authService.getUser().sendEmailVerification().then(()=>{
      //     this.alertMsg = "Changed your Email";
      //     this.hideSpinner();
      //     this.verifyAlert();
      //     this.hideForm();
      //     this.email = email;
      //   }).catch((err)=>{
      //     this.alertMsg = err.message;
      //     this.hideSpinner();
      //     this.errorAlert();
      //     this.hideForm();
      //     this.email = email;
      //   })
      // }).catch((err)=>{
      //   this.alertMsg = err.message;
      //   this.hideSpinner();
      //   this.errorAlert();
      //   this.hideForm();
      //   this.email = email;
      // })
    }
    else{

    }
  }

  resendEmail() {
    this.hideVerifyBody();
    this.showSpinner();
    // this._authService.getUser().sendEmailVerification().then(() => {
    //   this.hideSpinner();
    //   this.alertMsg = "Verification Email Resend";
    //   this.verifyAlert();
    // }).catch((err)=>{
    //   this.hideSpinner();
    //   this.alertMsg = err.message;
    //   this.errorAlert();
    // });
  }

  logout(){
    // this._authService.logout();
  }

}
