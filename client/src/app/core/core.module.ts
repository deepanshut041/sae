import { CommonModule } from '@angular/common';
import { ModuleWithProviders, NgModule,Optional, SkipSelf } from '@angular/core';
import { NavbarComponent } from "./navbar/navbar.component";
import { FooterComponent } from "./footer/footer.component";


@NgModule({
  declarations: [
     NavbarComponent, FooterComponent
  ],
  imports: [
    CommonModule
  ],
  providers: [],
  exports:[NavbarComponent, FooterComponent]
})
export class CoreModule { }
