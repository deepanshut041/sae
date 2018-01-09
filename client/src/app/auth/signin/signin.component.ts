import { Component, OnInit } from "@angular/core";
import { AuthService } from "../auth.service";
import { Router } from "@angular/router";
import { FormGroup, FormControl, FormBuilder, Validators, ReactiveFormsModule } from "@angular/forms";
import { AuthGaurd } from "../auth-gaurd.service";
@Component({
  selector: "app-signin",
  templateUrl: "./signin.component.html",
  styleUrls: ["./signin.component.css"]
})

export class SigninComponent implements OnInit {

  err: String;
  loginForm: FormGroup
  constructor(private _authService: AuthService, private router: Router, private _authGaurd:AuthGaurd) {

  }

  ngOnInit() {
    if(this._authGaurd.isLoggedIn){
      this.router.navigateByUrl('')
    }
    this.loginForm = new FormGroup({
      email: new FormControl(''),
      password: new FormControl('')
    });
    document.getElementById("spinner").style.display = "none";
    document.getElementById("login-page").style.display = "block";
  }
  login(email: any, password: any) {
    this.err = null;

    document.getElementById("form").style.display = "none";
    document.getElementById("spinner").style.display = "block";
    let result = this._authService.loginUser(this.loginForm.value)
    result.subscribe((response) => {
      this._authService.storeUserData(response['token'], response['username'] ,response['email'])
      this._authGaurd.changeLoginStatus(true)
      let redirect_url = this._authGaurd.redirectUrl || ''
      this.router.navigateByUrl(redirect_url)
    },
      (err) => {
        document.getElementById("form").style.display = "block";
        document.getElementById("spinner").style.display = "none";
        let error = err['error']
        let non_field_errors = error['non_field_errors']
        this.err = non_field_errors[0];
      }
    )
  }

}
