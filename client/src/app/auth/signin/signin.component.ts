import { Component, OnInit } from "@angular/core";
import { AuthService } from "../auth.service";
import { Router } from "@angular/router";

@Component({
  selector: "app-signin",
  templateUrl: "./signin.component.html",
  styleUrls: ["./signin.component.css"]
})

export class SigninComponent implements OnInit {

  err: String;
  constructor(private _authService: AuthService, private router: Router) {

  }

  ngOnInit() {
    // const userKey = Object.keys(window.localStorage).filter(it => it.startsWith('firebase:authUser'))[0];
    // const user = userKey ? JSON.parse(localStorage.getItem(userKey)) : undefined;
    // if(user){
    //   this.router.navigate(['provider/dashboard']);
    // }
    document.getElementById("spinner").style.display = "none";
    document.getElementById("login-page").style.display = "block";
  }
  onSubmit(email: any, password: any) {
    this.err = null;
    console.log(email + " / " + password)
    // if (email && password) {
    //   document.getElementById("form").style.display = "none";
    //   document.getElementById("spinner").style.display = "block";
    //   let result = this._authService.login(email, password)
    //   result.then((success) => {
    //     this.router.navigate(["/provider/dashboard"])
    //   }).catch(
    //     (err) => {
    //       document.getElementById("form").style.display = "block";
    //       document.getElementById("spinner").style.display = "none";
    //       this.err = err.message;
    //     }
    //     )
    // }
    // else {
    //   this.err = "Please enter details.."
    // }
  }

}
