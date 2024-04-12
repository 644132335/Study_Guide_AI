import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { FlashCardData } from './flashCard';

@Injectable({
  providedIn: 'root',
})
export class DataService {
  constructor(private http: HttpClient) {}

  getGeneratedContent(url:string,data: any):Observable<[FlashCardData]> {
    return this.http.post<[FlashCardData]>(url,data);
  }




}
