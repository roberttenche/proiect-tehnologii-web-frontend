import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

export interface User {
  id: number,
  name: string,
  email: string,
  password: string
};

@Component({
  selector: 'app-sign-up-page',
  templateUrl: './sign-up-page.component.html',
  styleUrls: ['./sign-up-page.component.css']
})
export class SignUpPageComponent implements OnInit {

  username: string;
  email: string;
  password: string;

  readonly sign_up_url = "http://localhost:8080/api/user/signUp"

  constructor(private http: HttpClient) {
    this.username = '';
    this.email = '';
    this.password = '';
  }

  ngOnInit(): void {
  }

  sign_up(): void {
    let user = {} as User;

    if (this.validate_input() == false) {
      alert('Username and Email must not have speical characters\nAll the data in the form must be completed.')
      throw new Error('User input is invalid')
    }

    user.id = 0;
    user.name = this.username;
    user.email = this.email;
    user.password = this.password;

    this.http.post(this.sign_up_url, user).subscribe(res => {
      alert("User " + this.username + " is created. Please log in!");
    });
  }

  validate_input(): boolean {
    const regex_usr  : RegExp = /^[a-zA-Z0-9]+$/i;
    const regex_email: RegExp = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i;

    if (
      (this.username == null || this.email == null || this.password == null) ||
      (this.username == ''   || this.email == ''   || this.password == '')
    )
      return false;

    // if input username or email has unauthorized special characters
    if (!(regex_usr.test(this.username) && regex_email.test(this.email)))
      return false;

    return true;
  }

}
