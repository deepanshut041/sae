import { Component } from '@angular/core';
import { IMAGE_FOOTER_TOWN } from "./shared/assets";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  footer_img = IMAGE_FOOTER_TOWN
}
