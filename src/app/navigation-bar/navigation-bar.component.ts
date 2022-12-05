import { isNgContainer } from '@angular/compiler';
import { Component, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api';

@Component({
  selector: 'app-navigation-bar',
  templateUrl: './navigation-bar.component.html',
  styleUrls: ['./navigation-bar.component.css']
})
export class NavigationBarComponent implements OnInit {

  items: MenuItem[];

  constructor() {
    this.items = [];
  }

  ngOnInit(): void {
    this.items = [
      {
        label: 'Home',
        icon: 'pi pi-home',
        routerLink: ['/home']
      },
      {
        label: 'Login',
        icon: 'pi pi-user',
        routerLink: ['/login']
      },
      {
        label: 'About',
        icon: 'pi pi-info-circle',
        routerLink: ['/about']
      }
    ];
  }

}
