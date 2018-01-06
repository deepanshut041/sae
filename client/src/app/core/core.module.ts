import { CommonModule } from '@angular/common';
import { ModuleWithProviders, NgModule,Optional, SkipSelf } from '@angular/core';
import { CoreComponent } from './core.component';
import { NavbarComponent } from "./navbar/navbar.component";
import { FooterComponent } from "./footer/footer.component";


@NgModule({
  declarations: [
    CoreComponent, NavbarComponent, FooterComponent
  ],
  imports: [
    CommonModule
  ],
  providers: [],
  exports:[NavbarComponent, FooterComponent]
})
export class CoreModule { }
