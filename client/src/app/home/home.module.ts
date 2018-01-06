import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';


import { MainComponent } from './main/main.component';
import { ContactComponent } from "./contact/contact.component";
import { EventComponent } from "./event/event.component";
import { TeamComponent } from "./team/team.component";
import { WorkshopComponent } from "./workshop/workshop.component";


@NgModule({
  declarations: [
    MainComponent, ContactComponent, EventComponent, TeamComponent,WorkshopComponent
  ],
  imports: [
    CommonModule
  ],
  providers: []
})
export class HomeModule { }
