import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';


import { MainComponent } from './main/main.component';
import { ContactComponent } from "./contact/contact.component";

@NgModule({
  declarations: [
    MainComponent, ContactComponent
  ],
  imports: [
    CommonModule
  ],
  providers: []
})
export class HomeModule { }
