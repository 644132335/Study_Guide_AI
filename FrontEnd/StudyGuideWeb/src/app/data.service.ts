import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { FlashCardData } from './flashCard';

@Injectable({
  providedIn: 'root',
})
export class DataService {
  constructor(private http: HttpClient) {}

  submitForm(text: any):Observable<FlashCardData> {
    return this.http.get<FlashCardData>('http://localhost:5000/getContent'+'/text='+text);
  }
}
