import { Component } from '@angular/core';
import { DataService } from '../data.service';
import { FlashCardData } from '../flashCard';

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrl: './test.component.css',
  
})
export class TestComponent {
  constructor(private dataService: DataService) {}

  textValue = '';
  wordCount = 0;
  cardResults:FlashCardData[] = []
q="Who was the goddess that initiated the wrath mentioned in the passage?";
a='White-armed Hera';

  validateWordCount(event: any): void {
    const words = event.target.value.split(/\s+/);
    this.wordCount = words.filter((word: string) => word.length > 0).length;
  }

  submitForm(): void {
    console.log('Submitted:', this.textValue);
    const url = "http://localhost:5000/getContent"
    const body = {
      number: 10,
      text: this.textValue
    }
    // Here, you can handle the form submission, like sending the text to a server.
    this.dataService.getGeneratedContent(url,body).subscribe(data => {
      console.log(data)
      this.cardResults = data
    }, error =>{
        console.log(error)
    });
  }

}
