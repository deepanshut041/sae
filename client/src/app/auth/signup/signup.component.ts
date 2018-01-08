import { Component, OnInit } from "@angular/core";
import { AuthService } from "../auth.service";
import { Router } from "@angular/router";


@Component({
  selector: "app-signup",
  templateUrl: "./signup.component.html",
  styleUrls: ["./signup.component.css"]
})

export class SignupComponent implements OnInit {
  msg:any;
  constructor(private _authService:AuthService, private router:Router) { 

  }

  ngOnInit() {
    // const userKey = Object.keys(window.localStorage).filter(it => it.startsWith('firebase:authUser'))[0];
    // const user = userKey ? JSON.parse(localStorage.getItem(userKey)) : undefined;
    // if(user){
    //   this.router.navigate(['provider/dashboard']);
    // }
  }
  signup(email:string,password:string){
    // var send = this._authService.signup(email,password)
    // send.then((success)=>{
    //   this._authService.getUser().sendEmailVerification().then(()=>{
    //     this.router.navigate(['/provider/auth/verify']);
    //   })
    // }).catch((err)=>{
    //   this.msg = err.message
    //   console.log(this.msg);
    // })
  }
}
