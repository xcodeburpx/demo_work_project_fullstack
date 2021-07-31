import { Component, OnInit } from '@angular/core';
import { BackendConnectService } from 'src/app/services/backend-connect.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  public user: any;

  constructor( public _bknConnService: BackendConnectService) { }

  ngOnInit() {
    this.user = {
      username: '',
      password: ''
    };
  }

  login() {
    this._bknConnService.login({'username': this.user.username, 'password': this.user.password});
  }
 
  refreshToken() {
    this._bknConnService.refreshToken();
  }
 
  logout() {
    this._bknConnService.logout();
  }
}
