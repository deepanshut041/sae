import { NgModule } from "@angular/core"
import { RouterModule, Routes } from "@angular/router";
import { MainComponent } from "./home/main/main.component";
import { ContactComponent } from "./home/contact/contact.component";
import { TeamComponent } from "./home/team/team.component";
import { WorkshopComponent } from "./home/workshop/workshop.component";
import { EventComponent } from "./home/event/event.component";

const routes: Routes = [
     {path:'', component:MainComponent},
     {path:'contact', component:ContactComponent},
     {path:'team', component:TeamComponent},
     {path:'workshop/:name', component:WorkshopComponent},
     {path:'event/:id', component:EventComponent}
]

@NgModule({
    imports:[RouterModule.forRoot(routes)],
    exports:[RouterModule]
})

export class AppRoutingModule {

}