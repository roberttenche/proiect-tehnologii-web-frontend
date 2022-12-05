import { Component, OnInit } from '@angular/core';

export interface User {
  id: number,
  name: string,
  email: string,
  password: string
};

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent implements OnInit {

  public username: string;
  password: string;
  email: string;

  constructor() {
    this.username = '';
    this.password = '';
    this.email = '';
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
    user.email = this.email;
    user.password = this.password;

    console.log(user)

  }

  validate_input(): boolean {
    const regex_usr  : RegExp = /^[a-zA-Z0-9]+$/i;
    const regex_email: RegExp = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i;

    if (
      (this.username == null || this.email == null || this.password == null) ||
      (this.username == '' || this.email == '' || this.password == '')
    )
      return false;

    // if input username or email has special characters
    if (!(regex_usr.test(this.username) && regex_email.test(this.email)))
      return false;

    return true;
  }

}
