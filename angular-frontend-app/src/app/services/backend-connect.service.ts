import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})

export class BackendConnectService {

  private api_url: string = "http://localhost:8000/";
  
  // http options used for making API calls
  private httpOptions: any;
  
  // the actual JWT token
  public token: string;
 
  // the token expiration date
  public token_expires: Date;
 
  // the username of the logged in user
  public username: string;
 
  // error messages received from the login attempt
  public errors: any = [];
  
  constructor(private http: HttpClient) {
    this.httpOptions = {
      headers: new HttpHeaders({'Content-Type': 'application/json'})
    };
  }

  getMessage() {
    return this.http.get(this.api_url);
  }

  // Uses http.post() to get an auth token from djangorestframework-jwt endpoint
  public login(user) {
    this.http.post(this.api_url + 'api/token/', JSON.stringify(user), this.httpOptions).subscribe(
      data => {
        console.log("User authenticated");
        console.log(data);
        this.updateData(data);
      },
      err => {
        console.log("User could not authenticate");
        this.errors = err['error'];
      }
    );
  }

  // Refreshes the JWT token, to extend the time the user is logged in
  public refreshToken() {
    this.http.post(this.api_url + 'api/token/refresh/', JSON.stringify({token: this.token['refresh']}), this.httpOptions).subscribe(
      data => {
        console.log("Token has been refreshed");
        console.log(data);
        this.updateData(data);
      },
      err => {
        console.log("Token could not be refreshed");
        this.errors = err['error'];
      }
    );
  }

  public logout() {
    console.log("Nullifying token refresh");
    this.token = null;
    this.token_expires = null;
    this.username = null;
  }
 
  private updateData(token) {
    console.log("Updating data about token value");
    console.log(token);
    this.token = token;
    this.errors = [];
 
    // decode the token to read the username and expiration timestamp
    const token_parts = this.token['access'].split(/\./);
    const token_decoded = JSON.parse(window.atob(token_parts[1]));
    this.token_expires = new Date(token_decoded.exp * 1000);
    this.username = token_decoded.username;
  }
}
