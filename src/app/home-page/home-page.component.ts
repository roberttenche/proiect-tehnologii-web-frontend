import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css']
})
export class HomePageComponent implements OnInit {

  dialogArray : Array<boolean>;

  constructor() {
    this.dialogArray = [ false, false ];
  }

  ngOnInit(): void {
  }

  display_dialog(movie_id : number): void {
    this.dialogArray[movie_id] = true;
  }

  close_all_dialogs(): void {
    this.dialogArray.forEach( (elem) => elem = false);
  }

}
