// Angular Imports
import { NgModule } from '@angular/core';
import { CommonModule } from "@angular/common";
import { FormsModule,ReactiveFormsModule } from "@angular/forms";
import {RouterModule} from "@angular/router"
import { HttpClientModule } from '@angular/common/http';
// This Module's Components
import { SigninComponent } from "./signin/signin.component";
import { SignupComponent } from "./signup/signup.component";
import { VerifyComponent } from "./verify/verify.component";
import { ResetComponent } from "./reset/reset.component";
import { AuthService } from "./auth.service";
import { AuthComponent } from "./auth.component";

@NgModule({
    imports: [CommonModule, FormsModule, RouterModule,HttpClientModule,ReactiveFormsModule],
    declarations: [
         SigninComponent, SignupComponent, VerifyComponent,
        ResetComponent, AuthComponent
    ],
    exports: [
    ],
    providers:[ AuthService]
})
export class AuthModule {
}
