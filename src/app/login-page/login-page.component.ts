import { Component, OnInit } from '@angular/core';
import { User } from '../sign-up-page/sign-up-page.component';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent implements OnInit {

  username: string;
  password: string;

  constructor() {
    this.username = '';
    this.password = '';
  }

  ngOnInit(): void {
  }

  login(): void {
    let user = {} as User;

    if (this.validate_input() == false) {
      alert('Username and Email must not have speical characters\nAll the data in the form must be completed.')
      throw new Error('User input is invalid')
    }

    user.id = 0;
    user.name = this.username;
    user.password = this.password;

    console.log(user)

  }

  validate_input(): boolean {
    const regex_usr  : RegExp = /^[a-zA-Z0-9]+$/i;

    if (
      (this.username == null || this.password == null) ||
      (this.username == '' || this.password == '')
    )
      return false;

    // if input username has unauthorized special characters
    if (!(regex_usr.test(this.username)))
      return false;

    return true;
  }

}
